"""
K_VLMEVAL — AIOSS Integration Layer
Anticloud FZ LLE | Apache-2.0 OR LicenseRef-Anticommons-Enterprise-1.0

Wraps VLMEvalKit multimodal evaluation with AIOSS ledger audit.
"""
import hashlib
import json
import shlex
import subprocess
import tarfile
import time
from pathlib import Path


class AIossVLMEvalWrapper:
    """Wraps VLMEvalKit eval runs with AIOSS ledger."""

    def __init__(self, ledger_path: str = "./vlmeval.aioss"):
        self.ledger_path = ledger_path
        self._prev_hash = "0" * 64
        subprocess.run(["aioss", "init", ledger_path], capture_output=True)

    def log_eval_result(self, model: str, dataset: str, score: float) -> str:
        payload = f"{model}:{dataset}:{score:.4f}:{time.time()}"
        entry_hash = hashlib.sha3_256(payload.encode()).hexdigest()
        chain_hash = hashlib.sha3_256(
            (self._prev_hash + entry_hash).encode()
        ).hexdigest()
        entry = {
            "model": model, "dataset": dataset, "score": score,
            "timestamp": time.time(), "chain_hash": chain_hash,
        }
        subprocess.run(
            ["aioss", "append", self.ledger_path, json.dumps(entry)],
            capture_output=True,
        )
        self._prev_hash = chain_hash
        return chain_hash

    @property
    def chain_hash(self) -> str:
        return self._prev_hash


# SECURITY_PATCH — B605 + B202 (CWE-78 shell injection, CWE-22 path traversal)
# Applied: 2026-09-30 | Anticloud FZ LLE
# Upstream: scripts/auto_run.py:44 (shell=True), build_mmlongbench_tsv.py:83 (tarfile.extractall)

def safe_run(cmd) -> subprocess.CompletedProcess:
    """Anticloud patch for B605: list-based subprocess, no shell injection."""
    parts = shlex.split(cmd) if isinstance(cmd, str) else list(cmd)
    return subprocess.run(parts, shell=False, capture_output=True, text=True, timeout=60)


def safe_extract(tar_path: str, extract_to: str) -> None:
    """Anticloud patch for B202: extract member-by-member (never extractall) to block CWE-22."""
    extract_dir = Path(extract_to).resolve()
    extract_dir.mkdir(parents=True, exist_ok=True)
    with tarfile.open(tar_path) as tf:
        for member in tf.getmembers():
            member_path = (extract_dir / member.name).resolve()
            if not str(member_path).startswith(str(extract_dir)):
                raise ValueError(f"Path traversal blocked: {member.name}")
            # Extract one member at a time — avoids B202 entirely
            tf.extract(member, path=str(extract_dir))
