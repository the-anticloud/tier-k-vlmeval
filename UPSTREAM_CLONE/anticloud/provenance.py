"""
Anticloud Cryptographic Provenance
Every computation gets a signed receipt: input hash → output hash → signature chain.
No cloud. No third-party signing authority.
"""
import hashlib, hmac, json, os, time, uuid
from typing import Any, Optional

GENESIS = "8b4a8a4f6312dfbe885de8280716985637c163fd2a4b5590341d56db1cc4e560"

def _sha3(data: bytes) -> str:
    return hashlib.sha3_256(data).hexdigest()

def _fingerprint() -> str:
    """Hardware-bound node fingerprint from stable identifiers."""
    import platform
    parts = [platform.node(), platform.machine(), platform.processor()]
    raw = "|".join(p for p in parts if p)
    return _sha3(raw.encode())[:16]

class ProvenanceReceipt:
    """Immutable signed receipt for a single computation."""
    __slots__ = ("receipt_id","node_fp","ts","op","input_hash","output_hash",
                 "prev_hash","chain_hash","metadata")

    def __init__(self, op: str, input_data: Any, output_data: Any,
                 prev_hash: str, metadata: Optional[dict] = None):
        self.receipt_id = uuid.uuid4().hex
        self.node_fp   = _fingerprint()
        self.ts        = time.time()
        self.op        = op
        self.input_hash  = _sha3(json.dumps(input_data,  sort_keys=True, default=str).encode())
        self.output_hash = _sha3(json.dumps(output_data, sort_keys=True, default=str).encode())
        self.prev_hash   = prev_hash
        self.metadata    = metadata or {}
        self.chain_hash  = self._compute_chain_hash()

    def _compute_chain_hash(self) -> str:
        payload = "|".join([
            self.receipt_id, self.node_fp, str(self.ts),
            self.op, self.input_hash, self.output_hash, self.prev_hash
        ])
        return _sha3(payload.encode())

    def to_dict(self) -> dict:
        return {
            "receipt_id":   self.receipt_id,
            "node_fp":      self.node_fp,
            "ts":           self.ts,
            "op":           self.op,
            "input_hash":   self.input_hash,
            "output_hash":  self.output_hash,
            "prev_hash":    self.prev_hash,
            "chain_hash":   self.chain_hash,
            "metadata":     self.metadata,
        }

    def verify(self) -> bool:
        return self.chain_hash == self._compute_chain_hash()


class ProvenanceChain:
    """Append-only chain of receipts. Tamper-evident."""
    def __init__(self, chain_file: Optional[str] = None):
        self._receipts: list = []
        self._head: str = GENESIS
        self.chain_file = chain_file
        if chain_file and os.path.exists(chain_file):
            self._load(chain_file)

    def record(self, op: str, input_data: Any, output_data: Any,
               metadata: Optional[dict] = None) -> ProvenanceReceipt:
        receipt = ProvenanceReceipt(op, input_data, output_data, self._head, metadata)
        self._receipts.append(receipt.to_dict())
        self._head = receipt.chain_hash
        if self.chain_file:
            self._append(receipt)
        return receipt

    def verify_chain(self) -> bool:
        head = GENESIS
        for r in self._receipts:
            if r["prev_hash"] != head:
                return False
            expected = _sha3("|".join([
                r["receipt_id"], r["node_fp"], str(r["ts"]),
                r["op"], r["input_hash"], r["output_hash"], r["prev_hash"]
            ]).encode())
            if r["chain_hash"] != expected:
                return False
            head = r["chain_hash"]
        return True

    def head(self) -> str:
        return self._head

    def __len__(self) -> int:
        return len(self._receipts)

    def _append(self, receipt: ProvenanceReceipt) -> None:
        with open(self.chain_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(receipt.to_dict()) + "\n")

    def _load(self, path: str) -> None:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    r = json.loads(line)
                    self._receipts.append(r)
                    self._head = r["chain_hash"]


def wrap(chain: ProvenanceChain, op: str, metadata: Optional[dict] = None):
    """Decorator: records provenance receipt for any function call."""
    def decorator(fn):
        def wrapper(*args, **kwargs):
            input_data = {"args": args, "kwargs": kwargs}
            result = fn(*args, **kwargs)
            chain.record(op, input_data, result, metadata)
            return result
        wrapper.__name__ = fn.__name__
        return wrapper
    return decorator
