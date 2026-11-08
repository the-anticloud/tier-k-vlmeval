"""
Anticloud CRDT — Conflict-Free Replicated Data Types
LWW-Register, OR-Set, G-Counter, PN-Counter
No coordination server. Works across air-gapped nodes.
"""
import json, time, uuid, hashlib
from typing import Any, Dict, Set, Tuple, Optional

NodeID = str

class LWWRegister:
    """Last-Write-Wins Register. Merges by highest timestamp."""
    def __init__(self, node_id: NodeID):
        self.node_id = node_id
        self._value: Any = None
        self._ts: float = 0.0
        self._origin: NodeID = ""

    def set(self, value: Any) -> None:
        self._ts = time.time()
        self._value = value
        self._origin = self.node_id

    def get(self) -> Any:
        return self._value

    def state(self) -> dict:
        return {"value": self._value, "ts": self._ts, "origin": self._origin}

    def merge(self, remote: dict) -> None:
        if remote["ts"] > self._ts:
            self._value = remote["value"]
            self._ts = remote["ts"]
            self._origin = remote["origin"]

    def __repr__(self):
        return f"LWWRegister({self._value!r} @ {self._ts:.3f} from {self._origin})"


class ORSet:
    """Observed-Remove Set. Add wins over concurrent remove."""
    def __init__(self, node_id: NodeID):
        self.node_id = node_id
        # {element: {unique_tag, ...}}
        self._added: Dict[Any, Set[str]] = {}
        self._removed: Dict[Any, Set[str]] = {}

    def add(self, element: Any) -> None:
        tag = f"{self.node_id}:{uuid.uuid4().hex}"
        self._added.setdefault(element, set()).add(tag)

    def remove(self, element: Any) -> None:
        tags = self._added.get(element, set())
        self._removed.setdefault(element, set()).update(tags)

    def contains(self, element: Any) -> bool:
        added = self._added.get(element, set())
        removed = self._removed.get(element, set())
        return bool(added - removed)

    def value(self) -> set:
        return {e for e in self._added if self.contains(e)}

    def state(self) -> dict:
        return {
            "added": {str(k): list(v) for k, v in self._added.items()},
            "removed": {str(k): list(v) for k, v in self._removed.items()},
        }

    def merge(self, remote: dict) -> None:
        for k, tags in remote.get("added", {}).items():
            self._added.setdefault(k, set()).update(tags)
        for k, tags in remote.get("removed", {}).items():
            self._removed.setdefault(k, set()).update(tags)


class GCounter:
    """Grow-only counter. Each node increments its own slot."""
    def __init__(self, node_id: NodeID):
        self.node_id = node_id
        self._counts: Dict[NodeID, int] = {node_id: 0}

    def increment(self, amount: int = 1) -> None:
        self._counts[self.node_id] = self._counts.get(self.node_id, 0) + amount

    def value(self) -> int:
        return sum(self._counts.values())

    def state(self) -> dict:
        return dict(self._counts)

    def merge(self, remote: dict) -> None:
        for node, count in remote.items():
            self._counts[node] = max(self._counts.get(node, 0), count)


class PNCounter:
    """Positive-Negative counter = two GCounters."""
    def __init__(self, node_id: NodeID):
        self.node_id = node_id
        self._pos = GCounter(node_id)
        self._neg = GCounter(node_id)

    def increment(self, amount: int = 1) -> None:
        self._pos.increment(amount)

    def decrement(self, amount: int = 1) -> None:
        self._neg.increment(amount)

    def value(self) -> int:
        return self._pos.value() - self._neg.value()

    def state(self) -> dict:
        return {"pos": self._pos.state(), "neg": self._neg.state()}

    def merge(self, remote: dict) -> None:
        self._pos.merge(remote["pos"])
        self._neg.merge(remote["neg"])


class CRDTDocument:
    """Composite CRDT document: named registers + sets + counters."""
    def __init__(self, node_id: Optional[str] = None):
        self.node_id = node_id or str(uuid.uuid4())[:8]
        self._registers: Dict[str, LWWRegister] = {}
        self._sets: Dict[str, ORSet] = {}
        self._counters: Dict[str, PNCounter] = {}

    def set(self, key: str, value: Any) -> None:
        if key not in self._registers:
            self._registers[key] = LWWRegister(self.node_id)
        self._registers[key].set(value)

    def get(self, key: str) -> Any:
        return self._registers[key].get() if key in self._registers else None

    def add_to_set(self, key: str, element: Any) -> None:
        if key not in self._sets:
            self._sets[key] = ORSet(self.node_id)
        self._sets[key].add(element)

    def remove_from_set(self, key: str, element: Any) -> None:
        if key in self._sets:
            self._sets[key].remove(element)

    def get_set(self, key: str) -> set:
        return self._sets[key].value() if key in self._sets else set()

    def increment(self, key: str, amount: int = 1) -> None:
        if key not in self._counters:
            self._counters[key] = PNCounter(self.node_id)
        self._counters[key].increment(amount)

    def decrement(self, key: str, amount: int = 1) -> None:
        if key not in self._counters:
            self._counters[key] = PNCounter(self.node_id)
        self._counters[key].decrement(amount)

    def count(self, key: str) -> int:
        return self._counters[key].value() if key in self._counters else 0

    def export_state(self) -> dict:
        return {
            "node_id": self.node_id,
            "registers": {k: v.state() for k, v in self._registers.items()},
            "sets": {k: v.state() for k, v in self._sets.items()},
            "counters": {k: v.state() for k, v in self._counters.items()},
        }

    def merge_state(self, remote: dict) -> None:
        for k, s in remote.get("registers", {}).items():
            if k not in self._registers:
                self._registers[k] = LWWRegister(self.node_id)
            self._registers[k].merge(s)
        for k, s in remote.get("sets", {}).items():
            if k not in self._sets:
                self._sets[k] = ORSet(self.node_id)
            self._sets[k].merge(s)
        for k, s in remote.get("counters", {}).items():
            if k not in self._counters:
                self._counters[k] = PNCounter(self.node_id)
            self._counters[k].merge(s)

    def checksum(self) -> str:
        raw = json.dumps(self.export_state(), sort_keys=True)
        return hashlib.sha3_256(raw.encode()).hexdigest()[:16]
