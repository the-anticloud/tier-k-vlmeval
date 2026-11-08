# Developer Cookbook — K_VLMEVAL

> Anticloud sovereign integration guide. All commands run offline.
> Author: Lois-Kleinner Alpasan / Anticloud FZ LLE
> USPTO pending 2026.

---

## Prerequisites

```bash
# Python 3.11+
python --version

# AIOSS ledger CLI (build from source)
cd TIER_1_ANTICLOUD_CORE/AIOSS_FORMAT/src && cargo build --release
export PATH="$PATH:$(pwd)/target/release"
aioss --version

# Initialize your ledger
aioss init --ledger ./ledger/main.aioss
```

---

## Installation

```bash
pip install -r UPSTREAM/requirements.txt
```

Verify:
```bash
python -c "import importlib; m = importlib.import_module('kvlmeval'); print('OK:', m)"
```

---

## Quickstart

```bash
python -c "import kvlmeval; print('K_VLMEVAL loaded OK')"
```

---

## Configuration

```yaml
# K_VLMEVAL — default config
# See UPSTREAM/README.md for full option reference
project_name: K_VLMEVAL
aioss_ledger: ./ledger/main.aioss
log_level: INFO
```

---

## Anticloud Integration Pattern

```python
# K_VLMEVAL Anticloud integration pattern
import hashlib, subprocess, json
from pathlib import Path

LEDGER = Path("./ledger/main.aioss")

def log_to_aioss(event: dict):
    entry = json.dumps(event)
    subprocess.run(["aioss", "append", "--ledger", str(LEDGER), entry], check=True)

# Initialize
log_to_aioss({"project": "K_VLMEVAL", "event": "init", "tier": "TIER_6_SECURITY_EVAL"})
print("K_VLMEVAL ready — AIOSS ledger active")
```

---

## AIOSS Ledger Integration

Every significant K_VLMEVAL operation should emit a ledger entry:

```python
import subprocess, json, hashlib

def aioss_append(ledger_path: str, event: dict):
    content = json.dumps(event, sort_keys=True)
    r = subprocess.run(
        ["aioss", "append", "--ledger", ledger_path, content],
        capture_output=True, text=True
    )
    if r.returncode != 0:
        print("[AIOSS] Warning:", r.stderr)
    return r.returncode == 0

# Usage
aioss_append("./ledger/main.aioss", {
    "project": "K_VLMEVAL",
    "event": "run",
    "input_hash": hashlib.sha3_256(b"your_input").hexdigest(),
})
```

Verify the chain at any time:
```bash
aioss verify --ledger ./ledger/main.aioss
```

---

## Benchmarking

Run the Anticloud 3-seed benchmark:
```bash
python BENCHMARKS/ENVIRONMENT_LAB_RESULTS_TEMPLATE.py
# Results at: OFFICIAL_BENCHMARKS/Environment_Lab_Results/results.json
```

For GPU benchmarks (T4):
```
https://www.kaggle.com/code/loiskleinner/anticloud-real-benchmarks
```

---

## Docker

```bash
# Full stack
docker compose up anticloud-ledger anticloud-inference

# Benchmark runner
docker compose run anticloud-bench

# Check health
curl http://localhost:8080/health  # AIOSS ledger
curl http://localhost:8000/health  # vLLM inference
```

---

## Common Issues

**Import error:** Run: pip install -r K_VLMEVAL/UPSTREAM/requirements.txt
**AIOSS ledger not found:** Run: aioss init --ledger ./ledger/main.aioss

---

## Further Reading

- [RESEARCH_PAPERS/anticloud_k_vlmeval_paper.md](../RESEARCH_PAPERS/anticloud_k_vlmeval_paper.md) — technical paper with citations
- [OFFICIAL_BENCHMARKS/](../OFFICIAL_BENCHMARKS/) — benchmark results
- [ENTERPRISE_LICENSING/PRICING.md](../ENTERPRISE_LICENSING/PRICING.md) — commercial licensing
- [CONTRACTS/MSA/MASTER_SERVICE_AGREEMENT.md](../CONTRACTS/MSA/MASTER_SERVICE_AGREEMENT.md) — MSA template
