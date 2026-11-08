# Dependencies — K_VLMEVAL

**Project:** `K_VLMEVAL`
**Tier:** TIER_6_SECURITY_EVAL
**Domain:** security evaluation, red-team, MITRE ATT&CK, OSINT, threat detection
**Maintainer:** Anticloud FZ LLE · 0-1.gg · lois@0-1.gg · Dubai, UAE
**Model:** Anticloud PAX L5 Narrow L2 General 27B
**AIOSS Chain:** `8b4a8a4f6312dfbe885de8280716985637c163fd2a4b5590341d56db1cc4e560`
**Date:** October 2026

---

## Dependency Manifest

All dependencies for `K_VLMEVAL` are listed here with license information. All dependencies are permissively licensed (Apache 2.0, MIT, BSD) unless otherwise noted.

## Runtime Dependencies

| Package | Version | License | Purpose |
|---|---|---|---|
| transformers | ≥4.40.0 | Apache 2.0 | PAX 27B model loading and inference |
| accelerate | ≥0.30.0 | Apache 2.0 | Multi-GPU and device mapping |
| bitsandbytes | ≥0.43.0 | MIT | Q4 quantization |
| torch | ≥2.2.0 | BSD-3 | Core tensor operations |
| numpy | ≥1.26.0 | BSD-3 | Numerical computation |
| scipy | ≥1.12.0 | BSD-3 | Scientific computation |
| requests | ≥2.31.0 | Apache 2.0 | HTTP client for API integration |
| cryptography | ≥42.0.0 | Apache 2.0 / BSD | SHA3-256, Ed25519, AES-256-GCM |
| pydantic | ≥2.5.0 | MIT | Typed data validation for SoT |

## Development Dependencies

| Package | License | Purpose |
|---|---|---|
| pytest | MIT | Unit and integration testing |
| black | MIT | Code formatting |
| mypy | MIT | Static type checking |
| ruff | MIT | Linting |
| reportlab | BSD | PDF generation |
| python-docx | MIT | DOCX generation |
| python-pptx | MIT | PPTX generation |

## License Compatibility Matrix

All dependencies are compatible with Apache 2.0 and the Anticommons Enterprise License 1.0. No GPL, LGPL, or copyleft dependencies are included.

| License Type | Count | Compatibility |
|---|---|---|
| Apache 2.0 | Primary | ✓ Fully compatible |
| MIT | Common | ✓ Fully compatible |
| BSD-3-Clause | Common | ✓ Fully compatible |
| GPL/LGPL | 0 | N/A — excluded |

## Dependency Security

Dependencies are scanned via OpenSSF Scorecard (current score: 6.28/10) and audited quarterly via:
```bash
pip-audit --requirement requirements.txt
safety check
```

**Dependency enquiries:** lois@0-1.gg
