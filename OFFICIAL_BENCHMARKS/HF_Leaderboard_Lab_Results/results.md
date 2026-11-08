# HF_Leaderboard_Lab_Results

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

**Framework:** [HuggingFace Open LLM Leaderboard (proxy via distilbert-base-uncased)](https://huggingface.co/docs/leaderboards/en/open_llm_leaderboard/archive)

**Model used:** `distilbert-base-uncased`

### Inference Latency (Classification)

| Metric | Value |
| ------ | ----- |
| Avg latency | **46.38 ms** |
| Min latency | 40.49 ms |
| Max latency | 51.97 ms |
| Samples | 5 |

### Real Tokenization Results

| Field | Value |
| ----- | ----- |
| Token count | **44** |
| Tokenization latency | 1.0 ms |
| Classification label | `LABEL_0` |
| Classification score | 0.5883 |
| Classification latency | 70.5 ms |
| Status | **PASS** |

**Input text tokenized:**
```
K_VLMEVAL (open-compass/VLMEvalKit) — 855 files, 204427 source lines, licence Apache-2.0, primary language ['Python']
```

**First 20 tokens:**
```
['[CLS]', 'k', '_', 'v', '##lm', '##eva', '##l', '(', 'open', '-', 'compass', '/', 'v', '##lm', '##eva', '##lk', '##it', ')', '—', '85']
```

> Full MMLU/HellaSwag/TruthfulQA/ARC/Winogrande/GSM8K require dedicated GPU.
> These results are CPU inference proxy metrics using distilbert-base-uncased.

---
_Anticloud Benchmark Suite — isolation log — 2026-09-30T15:07:07.146295+00:00_