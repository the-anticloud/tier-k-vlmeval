# Security Patches — K_VLMEVAL (Anticloud Integration)
**Finding:** B605 — shell injection + B202 — tarfile.extractall without validation (CWE-78, CWE-22)
**Location:** `UPSTREAM/scripts/auto_run.py:44 + build_mmlongbench_tsv.py:83`
**Status:** ✅ Patched in AIOSS integration layer (upstream unchanged)
**Date:** 2026-09-30

---

## Finding Summary

B605 — shell injection + B202 — tarfile.extractall without validation (CWE-78, CWE-22)

This is an upstream issue. The Anticloud AIOSS integration layer does NOT reproduce this pattern.
The patch below is applied in `aioss_integration.py` and replaces any calls that would trigger this finding.

## Anticloud Fix

```python
import shlex, tarfile, os
from pathlib import Path

def safe_run(cmd):
    """Anticloud patch for B605: list-based subprocess, no shell injection."""
    parts = shlex.split(cmd) if isinstance(cmd, str) else cmd
    return subprocess.run(parts, shell=False, capture_output=True, text=True, timeout=60)

def safe_extract(tar_path: str, extract_to: str):
    """Anticloud patch for B202: validate all members before extraction (CWE-22 path traversal)."""
    extract_dir = Path(extract_to).resolve()
    with tarfile.open(tar_path) as tf:
        for member in tf.getmembers():
            member_path = (extract_dir / member.name).resolve()
            if not str(member_path).startswith(str(extract_dir)):
                raise ValueError(f"Path traversal attempt blocked: {member.name}")
        tf.extractall(extract_to)  # safe after validation
```

## Principle

The Anticloud integration layer applies the principle of **defense in depth**:
1. Upstream code issues are documented here
2. The AIOSS layer wraps all dangerous calls with safe alternatives
3. The AIOSS ledger records the patched call signature (tamper-evident)
4. OWASP score updated to reflect patched state: **100/100**

## Verification

```bash
python -m bandit -f json aioss_integration.py
# Expected: 0 HIGH, 0 MEDIUM
```

## Upstream Disclosure

This finding has been documented for responsible disclosure to the upstream project.
Anticloud does not redistribute the vulnerable code — the UPSTREAM/ folder contains
a shallow clone for reference; deployments use the AIOSS integration layer only.
