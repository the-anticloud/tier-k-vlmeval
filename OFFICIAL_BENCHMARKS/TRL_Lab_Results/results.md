# TRL_Lab_Results

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

**Framework:** [ML-TRL (Lavin et al. 2022 - Nature Communications)](https://www.nature.com/articles/s41467-022-33128-9)

| Field | Value |
| ----- | ----- |
| Measured TRL | **8** / 9 |
| Target TRL | 8 |
| Meets Target | YES |
| Score Ratio | 1.0 |

### Factor Breakdown

| Factor | Pass | Weight |
| ------ | ---- | ------ |
| `has_upstream` | YES | 2 |
| `tracked_files_100+` | YES | 1 |
| `has_tests` | YES | 1 |
| `has_ci_cd` | YES | 1 |
| `has_official_docs` | YES | 1 |
| `open_licence` | YES | 1 |
| `source_lines_1000+` | YES | 1 |

> **Note:** TRL score is a static code-structure proxy (Lavin et al. 2022).
> It measures presence of upstream code, tests, CI/CD, docs, licence — NOT runtime performance.

---
_Anticloud Benchmark Suite — isolation log — 2026-09-30T15:07:07.146295+00:00_