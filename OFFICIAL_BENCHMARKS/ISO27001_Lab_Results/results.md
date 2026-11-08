# ISO27001_Lab_Results

**Project:** `K_VLMEVAL`  
**Tier:** `TIER_6_SECURITY_EVAL`  
**Slug:** `open-compass/VLMEvalKit`  
**Commit:** `54a063c5bf75`  
**Run:** `2026-09-30T15:07:07.146295+00:00`  

## Isolation Environment

| Field | Value |
| ----- | ----- |
| Platform | `win32` |
| Python | `3.12.10` |
| HF model | `distilbert-base-uncased` |
| HF load time | `4.42s` |
| Inference device | `cpu` |

## Results

**Framework:** [ISO 27001:2022 + ISO/IEC 42001 AI Governance](https://gruve.ai/blog/soc-2-and-iso-27001-compliance-ai-powered-audit-trails/)

Conformance: **100%** (6/6 controls)

| Control | Name | Status | Method |
| ------- | ---- | ------ | ------ |
| `A.5.1` | Policies for information security | **PASS** | COMPLIANCE/ folder exists |
| `A.8.8` | Management of technical vulnerabilities | **PASS** | Vulnerability management doc exists |
| `A.5.12` | Classification of information | **PASS** | Licence classification present |
| `A.8.25` | Secure development lifecycle | **PASS** | CI/CD workflows (SDLC automation) |
| `A.5.37` | Documented operating procedures | **PASS** | TECHNICAL/ documentation folder exists |
| `AI-42001` | AI Governance (ISO/IEC 42001 supplement) | **PASS** | GOVERNANCE/ folder exists |

---
_Anticloud Benchmark Suite — isolation log — 2026-09-30T15:07:07.146295+00:00_