"""
Anticloud Local Observability Stack
OpenTelemetry-compatible traces, metrics, logs — stored locally, never transmitted.
Queryable offline. No Datadog, no Grafana Cloud.
"""
import json, os, time, uuid, threading
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional


class Span:
    def __init__(self, name: str, trace_id: str, parent_id: Optional[str] = None):
        self.span_id   = uuid.uuid4().hex[:16]
        self.trace_id  = trace_id
        self.parent_id = parent_id
        self.name      = name
        self.start_ns  = time.time_ns()
        self.end_ns: Optional[int] = None
        self.attrs: Dict[str, Any] = {}
        self.events: List[dict] = []
        self.status   = "OK"

    def set_attr(self, key: str, value: Any) -> "Span":
        self.attrs[key] = value
        return self

    def add_event(self, name: str, attrs: Optional[dict] = None) -> "Span":
        self.events.append({"name": name, "ts_ns": time.time_ns(), "attrs": attrs or {}})
        return self

    def set_error(self, message: str) -> "Span":
        self.status = "ERROR"
        self.attrs["error.message"] = message
        return self

    def end(self) -> None:
        self.end_ns = time.time_ns()

    def duration_ms(self) -> float:
        if self.end_ns is None:
            return 0.0
        return (self.end_ns - self.start_ns) / 1e6

    def to_dict(self) -> dict:
        return {
            "span_id": self.span_id, "trace_id": self.trace_id,
            "parent_id": self.parent_id, "name": self.name,
            "start_ns": self.start_ns, "end_ns": self.end_ns,
            "duration_ms": self.duration_ms(), "attrs": self.attrs,
            "events": self.events, "status": self.status,
        }


class Tracer:
    def __init__(self, service: str, store: "LocalStore"):
        self.service = service
        self._store  = store
        self._local  = threading.local()

    def start_trace(self, name: str) -> Span:
        trace_id = uuid.uuid4().hex
        span = Span(name, trace_id)
        span.set_attr("service", self.service)
        self._local.current = span
        return span

    def start_span(self, name: str) -> Span:
        parent = getattr(self._local, "current", None)
        trace_id = parent.trace_id if parent else uuid.uuid4().hex
        parent_id = parent.span_id if parent else None
        span = Span(name, trace_id, parent_id)
        span.set_attr("service", self.service)
        self._local.current = span
        return span

    def finish(self, span: Span) -> None:
        span.end()
        self._store.write_span(span)


class Metric:
    def __init__(self, name: str, labels: Optional[dict] = None):
        self.name   = name
        self.labels = labels or {}
        self._lock  = threading.Lock()
        self._value = 0.0
        self._count = 0
        self._sum   = 0.0
        self._min   = float("inf")
        self._max   = float("-inf")

    def record(self, value: float) -> None:
        with self._lock:
            self._value  = value
            self._count += 1
            self._sum   += value
            self._min    = min(self._min, value)
            self._max    = max(self._max, value)

    def increment(self, amount: float = 1.0) -> None:
        with self._lock:
            self._value += amount
            self._count += 1

    def snapshot(self) -> dict:
        with self._lock:
            return {
                "name": self.name, "labels": self.labels,
                "value": self._value, "count": self._count,
                "sum": self._sum,
                "min": self._min if self._count else 0,
                "max": self._max if self._count else 0,
                "avg": self._sum / self._count if self._count else 0,
                "ts": time.time(),
            }


class LocalStore:
    """Write traces/metrics/logs to local JSONL files. Query offline."""
    def __init__(self, data_dir: str):
        self._dir = Path(data_dir)
        self._dir.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()

    def write_span(self, span: Span) -> None:
        self._write("traces.jsonl", span.to_dict())

    def write_metric(self, metric: Metric) -> None:
        self._write("metrics.jsonl", metric.snapshot())

    def write_log(self, level: str, message: str, attrs: Optional[dict] = None) -> None:
        self._write("logs.jsonl", {
            "ts": time.time(), "level": level,
            "message": message, "attrs": attrs or {}
        })

    def _write(self, filename: str, record: dict) -> None:
        path = self._dir / filename
        with self._lock:
            with open(path, "a", encoding="utf-8") as f:
                f.write(json.dumps(record) + "\n")

    def query_spans(self, trace_id: Optional[str] = None,
                    service: Optional[str] = None,
                    last_n: int = 100) -> List[dict]:
        return self._query("traces.jsonl", {
            "trace_id": trace_id, "attrs.service": service
        }, last_n)

    def query_logs(self, level: Optional[str] = None, last_n: int = 100) -> List[dict]:
        return self._query("logs.jsonl", {"level": level}, last_n)

    def _query(self, filename: str, filters: dict, last_n: int) -> List[dict]:
        path = self._dir / filename
        if not path.exists():
            return []
        results = []
        with open(path, encoding="utf-8") as f:
            for line in f:
                try:
                    r = json.loads(line)
                    if all(v is None or r.get(k) == v for k, v in filters.items()):
                        results.append(r)
                except Exception:
                    pass
        return results[-last_n:]

    def stats(self) -> dict:
        out = {}
        for fname in ["traces.jsonl", "metrics.jsonl", "logs.jsonl"]:
            p = self._dir / fname
            out[fname] = {"lines": sum(1 for _ in open(p)) if p.exists() else 0,
                          "bytes": p.stat().st_size if p.exists() else 0}
        return out


class Observability:
    """Top-level handle: get tracers, metrics, log."""
    def __init__(self, service: str, data_dir: str):
        self.service = service
        self.store   = LocalStore(data_dir)
        self._metrics: Dict[str, Metric] = {}

    def tracer(self) -> Tracer:
        return Tracer(self.service, self.store)

    def metric(self, name: str, labels: Optional[dict] = None) -> Metric:
        key = f"{name}:{json.dumps(labels or {}, sort_keys=True)}"
        if key not in self._metrics:
            self._metrics[key] = Metric(name, labels)
        return self._metrics[key]

    def flush_metrics(self) -> None:
        for m in self._metrics.values():
            self.store.write_metric(m)

    def log(self, level: str, message: str, **attrs) -> None:
        self.store.write_log(level, message, attrs)

    def info(self, msg: str, **attrs):  self.log("INFO",    msg, **attrs)
    def warn(self, msg: str, **attrs):  self.log("WARN",    msg, **attrs)
    def error(self, msg: str, **attrs): self.log("ERROR",   msg, **attrs)
    def debug(self, msg: str, **attrs): self.log("DEBUG",   msg, **attrs)
