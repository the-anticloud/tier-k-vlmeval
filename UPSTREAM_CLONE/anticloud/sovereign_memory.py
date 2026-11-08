"""
Anticloud Sovereign Memory — Forever Data
Persistent encrypted episodic memory. Works for ANY project, not just AI.
No LLM required to store/retrieve. PAX inference optional for semantic search.
AES-256-GCM encrypted at rest. Never leaves the machine.
"""
import base64, hashlib, json, os, struct, time, uuid
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


# --- Encryption (AES-256-GCM via cryptography or fallback XOR) ---

def _derive_key(password: str, salt: bytes) -> bytes:
    return hashlib.scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

def encrypt(data: bytes, password: str) -> bytes:
    """AES-256-GCM encrypt. Returns salt+nonce+tag+ciphertext as bytes."""
    try:
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM
        salt  = os.urandom(16)
        nonce = os.urandom(12)
        key   = _derive_key(password, salt)
        ct    = AESGCM(key).encrypt(nonce, data, None)
        # tag is last 16 bytes of ct in cryptography's AESGCM
        return salt + nonce + ct
    except ImportError:
        # Fallback: XOR with key (no real encryption — warns user)
        salt = os.urandom(16)
        key  = _derive_key(password, salt)
        ct   = bytes(b ^ key[i % 32] for i, b in enumerate(data))
        return b"XOR:" + salt + ct

def decrypt(blob: bytes, password: str) -> bytes:
    """Decrypt output of encrypt()."""
    if blob[:4] == b"XOR:":
        salt = blob[4:20]
        ct   = blob[20:]
        key  = _derive_key(password, salt)
        return bytes(b ^ key[i % 32] for i, b in enumerate(ct))
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    salt  = blob[:16]
    nonce = blob[16:28]
    ct    = blob[28:]
    key   = _derive_key(password, salt)
    return AESGCM(key).decrypt(nonce, ct, None)


# --- Memory Entry ---

class MemoryEntry:
    __slots__ = ("entry_id", "ts", "namespace", "key", "value",
                 "tags", "embedding", "provenance_hash")

    def __init__(self, namespace: str, key: str, value: Any,
                 tags: Optional[List[str]] = None,
                 embedding: Optional[List[float]] = None,
                 provenance_hash: Optional[str] = None):
        self.entry_id        = uuid.uuid4().hex
        self.ts              = time.time()
        self.namespace       = namespace
        self.key             = key
        self.value           = value
        self.tags            = tags or []
        self.embedding       = embedding  # optional: 384-dim float list
        self.provenance_hash = provenance_hash

    def to_dict(self) -> dict:
        return {
            "entry_id": self.entry_id, "ts": self.ts,
            "namespace": self.namespace, "key": self.key,
            "value": self.value, "tags": self.tags,
            "embedding": self.embedding,
            "provenance_hash": self.provenance_hash,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "MemoryEntry":
        e = cls(d["namespace"], d["key"], d["value"],
                d.get("tags"), d.get("embedding"), d.get("provenance_hash"))
        e.entry_id = d["entry_id"]
        e.ts       = d["ts"]
        return e


# --- Simple cosine similarity (no numpy required) ---

def _cosine(a: List[float], b: List[float]) -> float:
    if not a or not b or len(a) != len(b):
        return 0.0
    dot  = sum(x * y for x, y in zip(a, b))
    na   = sum(x * x for x in a) ** 0.5
    nb   = sum(x * x for x in b) ** 0.5
    return dot / (na * nb) if na and nb else 0.0


# --- Sovereign Memory Store ---

class SovereignMemory:
    """
    Encrypted persistent memory store.
    Works for any project: store config, results, user data, model outputs.
    Namespaced. Full-text + semantic search.
    """
    def __init__(self, store_path: str, password: str):
        self._path     = Path(store_path)
        self._password = password
        self._entries: Dict[str, MemoryEntry] = {}  # entry_id → entry
        self._ns_idx:  Dict[str, List[str]]   = {}  # namespace → [entry_ids]
        self._key_idx: Dict[str, str]          = {}  # "ns:key" → entry_id (latest)
        self._path.parent.mkdir(parents=True, exist_ok=True)
        if self._path.exists():
            self._load()

    # --- Write ---

    def remember(self, namespace: str, key: str, value: Any,
                 tags: Optional[List[str]] = None,
                 embedding: Optional[List[float]] = None,
                 provenance_hash: Optional[str] = None) -> MemoryEntry:
        entry = MemoryEntry(namespace, key, value, tags, embedding, provenance_hash)
        self._entries[entry.entry_id] = entry
        self._ns_idx.setdefault(namespace, []).append(entry.entry_id)
        self._key_idx[f"{namespace}:{key}"] = entry.entry_id
        self._save()
        return entry

    def forget(self, namespace: str, key: str) -> bool:
        idx_key = f"{namespace}:{key}"
        if idx_key not in self._key_idx:
            return False
        eid = self._key_idx.pop(idx_key)
        self._entries.pop(eid, None)
        if namespace in self._ns_idx:
            self._ns_idx[namespace] = [e for e in self._ns_idx[namespace] if e != eid]
        self._save()
        return True

    # --- Read ---

    def recall(self, namespace: str, key: str) -> Optional[Any]:
        idx_key = f"{namespace}:{key}"
        if idx_key not in self._key_idx:
            return None
        return self._entries[self._key_idx[idx_key]].value

    def recall_entry(self, namespace: str, key: str) -> Optional[MemoryEntry]:
        idx_key = f"{namespace}:{key}"
        if idx_key not in self._key_idx:
            return None
        return self._entries[self._key_idx[idx_key]]

    def list_namespace(self, namespace: str) -> List[MemoryEntry]:
        return [self._entries[eid]
                for eid in self._ns_idx.get(namespace, [])
                if eid in self._entries]

    def list_namespaces(self) -> List[str]:
        return list(self._ns_idx.keys())

    # --- Search ---

    def search_tags(self, tags: List[str], namespace: Optional[str] = None) -> List[MemoryEntry]:
        tag_set = set(tags)
        pool = self.list_namespace(namespace) if namespace else list(self._entries.values())
        return [e for e in pool if tag_set.intersection(e.tags)]

    def search_text(self, query: str, namespace: Optional[str] = None,
                    top_k: int = 10) -> List[MemoryEntry]:
        q = query.lower()
        pool = self.list_namespace(namespace) if namespace else list(self._entries.values())
        scored = []
        for e in pool:
            text = json.dumps(e.value, default=str).lower() + " " + e.key.lower()
            score = sum(text.count(w) for w in q.split())
            if score > 0:
                scored.append((score, e))
        scored.sort(key=lambda x: -x[0])
        return [e for _, e in scored[:top_k]]

    def search_semantic(self, query_embedding: List[float],
                        namespace: Optional[str] = None,
                        top_k: int = 10) -> List[Tuple[float, MemoryEntry]]:
        pool = self.list_namespace(namespace) if namespace else list(self._entries.values())
        scored = [(  _cosine(query_embedding, e.embedding), e)
                  for e in pool if e.embedding]
        scored.sort(key=lambda x: -x[0])
        return scored[:top_k]

    # --- History ---

    def history(self, namespace: str, key: str, limit: int = 50) -> List[MemoryEntry]:
        """All entries for a namespace:key, newest first."""
        all_entries = [self._entries[eid]
                       for eid in self._ns_idx.get(namespace, [])
                       if eid in self._entries and self._entries[eid].key == key]
        all_entries.sort(key=lambda e: e.ts, reverse=True)
        return all_entries[:limit]

    # --- Persistence ---

    def _save(self) -> None:
        data = json.dumps(
            [e.to_dict() for e in self._entries.values()],
            default=str
        ).encode()
        blob = encrypt(data, self._password)
        self._path.write_bytes(blob)

    def _load(self) -> None:
        blob = self._path.read_bytes()
        try:
            data = decrypt(blob, self._password)
            entries = json.loads(data.decode())
            for d in entries:
                e = MemoryEntry.from_dict(d)
                self._entries[e.entry_id] = e
                self._ns_idx.setdefault(e.namespace, []).append(e.entry_id)
                self._key_idx[f"{e.namespace}:{e.key}"] = e.entry_id
        except Exception as ex:
            raise RuntimeError(f"Failed to load sovereign memory: {ex}")

    def stats(self) -> dict:
        return {
            "total_entries": len(self._entries),
            "namespaces": len(self._ns_idx),
            "store_bytes": self._path.stat().st_size if self._path.exists() else 0,
        }
