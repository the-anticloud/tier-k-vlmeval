# Technical Handoff — K_VLMEVAL

**Project:** `K_VLMEVAL`
**Tier:** TIER_6_SECURITY_EVAL
**Domain:** security evaluation, red-team, MITRE ATT&CK, OSINT, threat detection
**Maintainer:** Anticloud FZ LLE · 0-1.gg · lois@0-1.gg · Dubai, UAE
**Model:** Anticloud PAX L5 Narrow L2 General 27B
**AIOSS Chain:** `8b4a8a4f6312dfbe885de8280716985637c163fd2a4b5590341d56db1cc4e560`
**Date:** October 2026

---

## Handoff Overview

This document provides the complete technical handoff package for `K_VLMEVAL` — everything a new engineer, integration partner, or enterprise customer needs to take ownership of this component.

## System Context

`K_VLMEVAL` is a security evaluation, red-team, MITRE ATT&CK, OSINT, threat detection component within the Anticloud 9-tier sovereign AI infrastructure. It integrates with the PAX L5 Narrow L2 General 27B inference engine via the AIOSS audit chain.

## Deployment Package Contents

Each `K_VLMEVAL` deployment package includes:

```
K_VLMEVAL/
├── *.tar.gz          # Main archive (SHA3-256 verified)
├── *.zip             # Zip archive (SHA3-256 verified)
├── *.7z              # 7-zip archive (SHA3-256 verified)
├── HASHES.md         # KANTOR K5 post-quantum hashes
├── AIOSS chain hash  # 8b4a8a4f6312dfbe885de82807169856...
├── 00_README.md      # Entry point
└── [document subfolders 01-28]
```

## Environment Requirements

| Requirement | Minimum | Recommended |
|---|---|---|
| GPU | NVIDIA T4 (15.64GB VRAM) | A100 80GB |
| CPU | 8-core x86_64 | 32-core |
| RAM | 32GB | 128GB |
| Storage | 100GB SSD | 1TB NVMe |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |
| CUDA | 12.0+ | 12.8 |
| Python | 3.10+ | 3.11 |

## Verification Steps

1. Verify KANTOR K5 hash against HASHES.md before deployment
2. Confirm AIOSS chain starts from genesis block or a valid parent hash
3. Run offline verification kit: `python verify.py --chain 8b4a8a4f6312dfbe...`
4. Confirm TLS 1.3 is active on all inbound endpoints
5. Validate Ed25519 signing key fingerprint with Anticloud FZ LLE: lois@0-1.gg

## Key Contacts

| Role | Contact |
|---|---|
| Technical lead | lois@0-1.gg |
| Compliance handoff | lois@0-1.gg |
| Emergency | lois@0-1.gg |

**0-1.gg · Anticloud FZ LLE · Dubai, UAE**
