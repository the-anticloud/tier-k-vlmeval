# Integrations and SDK — K_VLMEVAL

**Project:** `K_VLMEVAL`
**Tier:** TIER_6_SECURITY_EVAL
**Domain:** security evaluation, red-team, MITRE ATT&CK, OSINT, threat detection
**Maintainer:** Anticloud FZ LLE · 0-1.gg · lois@0-1.gg · Dubai, UAE
**Model:** Anticloud PAX L5 Narrow L2 General 27B
**AIOSS Chain:** `8b4a8a4f6312dfbe885de8280716985637c163fd2a4b5590341d56db1cc4e560`
**Date:** October 2026

---

## SDK Overview

`K_VLMEVAL` ships with a Python SDK and integration packages for common platforms.

## Python SDK

```bash
pip install anticloud-k-vlmeval
```

### Core SDK Usage

```python
from anticloud.k_vlmeval import KVlmevalClient

client = KVlmevalClient(
    api_key="your-license-key",
    chain_genesis="8b4a8a4f6312dfbe885de8280716985637c163fd2a4b5590341d56db1cc4e560",
    compliance_mode="hipaa",  # or gdpr, fedramp, pci-dss
)

result = client.run(prompt="Your query here")
print(result.text)
print(f"Chain entry: {result.aioss_hash}")
```

## REST API

```
POST /v1/infer
Authorization: Bearer <license-key>
Content-Type: application/json

{
  "prompt": "Your query",
  "max_tokens": 512,
  "compliance_mode": "gdpr",
  "project": "K_VLMEVAL"
}
```

**Response:**
```json
{
  "text": "...",
  "aioss_entry_hash": "sha3-256-hash",
  "latency_ms": 508,
  "tokens_used": 312,
  "compliance_checks": {"gdpr": "PASS", "pii_detected": false}
}
```

## Platform Integrations

| Platform | Integration | Status |
|---|---|---|
| GitHub Actions | `.github/workflows/anticloud-ci.yml` | Available |
| Slack | api-oss-integrations-slack | Available |
| Zapier | api-oss-integrations-zapier | Available |
| Kubernetes | `kubernetes-manifests/` | Available |
| Terraform (AWS) | `terraform-aws/` | Available |
| Docker Compose | `docker-compose/` | Available |

## WebHook Integration

```python
from anticloud.webhooks import AIAOSSWebhook

hook = AIAOSSWebhook(
    endpoint="https://your-system.example.com/aioss",
    secret="your-webhook-secret",
    events=["inference.complete", "chain.update", "compliance.alert"],
)
hook.register()
```

## SDK Reference Documentation

Full SDK reference is auto-generated from type stubs and published at 0-1.gg/docs/k-vlmeval.

**Support:** lois@0-1.gg · 0-1.gg
