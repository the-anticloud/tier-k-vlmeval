# OWASP_Lab_Results

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

**Framework:** [OWASP LLM Top 10 v1.1 (2024)](https://genai.owasp.org/resource/llm-top-10-for-llms-v1-1/)

Pass rate: **4/5** (80%)

| Check ID | Name | Status | Method |
| -------- | ---- | ------ | ------ |
| `LLM01` | Prompt Injection | **PASS** | grep for input sanitization patterns |
| `LLM02` | Insecure Output Handling | **UNVERIFIED** | grep for output escaping/sanitization |
| `LLM06` | Sensitive Information Disclosure | **PASS** | grep for env-var based secret management |
| `LLM09` | Overreliance | **PASS** | grep for confidence thresholds or human review gates |
| `LLM10` | Model Theft | **PASS** | grep for rate limiting or endpoint auth |

---
_Anticloud Benchmark Suite — isolation log — 2026-09-30T15:07:07.146295+00:00_