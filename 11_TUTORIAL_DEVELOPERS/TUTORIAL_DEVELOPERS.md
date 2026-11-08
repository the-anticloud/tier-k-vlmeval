# Developer Tutorial — K_VLMEVAL

**Project:** `K_VLMEVAL`
**Tier:** TIER_6_SECURITY_EVAL
**Domain:** security evaluation, red-team, MITRE ATT&CK, OSINT, threat detection
**Maintainer:** Anticloud FZ LLE · 0-1.gg · lois@0-1.gg · Dubai, UAE
**Model:** Anticloud PAX L5 Narrow L2 General 27B
**AIOSS Chain:** `8b4a8a4f6312dfbe885de8280716985637c163fd2a4b5590341d56db1cc4e560`
**Date:** October 2026

---

## Who This Is For

This tutorial is for software engineers integrating `K_VLMEVAL` into their stack. It assumes familiarity with Python, REST APIs, and basic DevOps. No prior Anticloud experience required.

## Prerequisites

```bash
# Python 3.10+
python --version

# CUDA 12.0+ (for GPU inference)
nvcc --version

# Install core dependencies
pip install anticloud-pax transformers accelerate bitsandbytes
pip install huggingface_hub requests
```

## Quick Start: 5 Minutes to First Inference

### Step 1: Configure AIOSS Chain

```python
from anticloud.aioss import AIAOSSLedger

# Initialize chain from published genesis
ledger = AIAOSSLedger(
    genesis_hash="8b4a8a4f6312dfbe885de8280716985637c163fd2a4b5590341d56db1cc4e560",
    project="K_VLMEVAL",
    signing_key_path="./keys/deployment.ed25519"
)
```

### Step 2: Load PAX 27B

```python
from anticloud.pax import PAXInference

pax = PAXInference(
    model_id="kleinnner/pax-l5-narrow-l2-general-27b-q4",
    device="cuda",
    ledger=ledger,  # AIOSS chain auto-logs every inference
)
```

### Step 3: Run Inference

```python
result = pax.generate(
    prompt="Summarize patient record for HIPAA audit trail",
    max_tokens=512,
    compliance_mode="hipaa",  # Enforces PII redaction
)

print(result.text)
print(f"AIOSS entry: {result.chain_entry_hash}")
print(f"Latency: {result.latency_ms}ms")
```

## Architecture Reference

`K_VLMEVAL` participates in the Anticloud security evaluation, red-team, MITRE ATT&CK, OSINT, threat detection layer. Key integration points:

1. **AIOSS Ledger** — All operations log to the append-only chain
2. **KANTOR K5** — Deployment archives are K5-hashed before loading
3. **SoT Layer** — Proprioceptive typed state model for self-aware operation
4. **Compliance Engine** — GDPR/HIPAA/FedRAMP controls are structural, not bolt-on

## Existing Documentation in This Project

- `00_README.md`
- `01_INVESTOR_PACKAGE\FINANCIAL_MODEL.md`
- `01_INVESTOR_PACKAGE\GTM_STRATEGY.md`
- `01_INVESTOR_PACKAGE\HIRING_PLAN.md`
- `01_INVESTOR_PACKAGE\IP_ASSIGNMENT.md`
- `01_INVESTOR_PACKAGE\USE_OF_FUNDS.md`
- `02_COMMITMENT_TO_SOCIETY\COMMITMENT_TO_SOCIETY.md`
- `03_COMMITMENT_TO_HUMANITY\COMMITMENT_TO_HUMANITY.md`

## Error Codes

| Code | Meaning | Resolution |
|---|---|---|
| `AIOSS_CHAIN_BREAK` | Chain hash mismatch | Verify genesis hash, check for tampering |
| `K5_VERIFY_FAIL` | Archive integrity failure | Re-download, verify HASHES.md |
| `COMPLIANCE_BLOCK` | PII/PHI detected, blocked | Use compliance_mode parameter |
| `VRAM_OOM` | GPU memory exceeded | Use Q4 quantization or smaller batch |

**Support:** lois@0-1.gg · 0-1.gg
