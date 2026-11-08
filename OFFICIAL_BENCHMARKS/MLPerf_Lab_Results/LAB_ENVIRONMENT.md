# Lab Environment Record — MLPerf_Lab_Results

**Project:** `K_VLMEVAL`
**Benchmark:** `MLPerf_Lab_Results`
**Recorded:** `2026-09-30T15:41:09.494539+00:00`

## Compute Environment

| Field | Value |
| ----- | ----- |
| Platform | `win32` |
| Python | `3.12.10` |
| OS family | `win32` |
| Inference device | `CPU (device=-1)` |
| HF model | `distilbert-base-uncased` |
| HF pipeline type | `text-classification` |
| Tokenizer | `distilbert-base-uncased` |
| Max sequence length | `128 tokens` |
| Batch size | `1 (single inference)` |

## Storage

| Field | Value |
| ----- | ----- |
| Root path | `E:\fenta\Downloads\The Anticloud` |
| Available disk | `~436 GB (E: drive)` |
| Results format | `JSON (UTF-8) + Markdown + PDF` |

## Benchmark Isolation

The benchmark runs in a single Python process with:
- No GPU acceleration (CPU-only inference)
- No network calls during inference
- No shared state between projects (each project independently measured)
- Deterministic git grep (no fuzzy matching)

## Reproducibility Class

Per HELM reproducibility standards (Stanford CRFM):
- **Prompt format**: Fixed programmatic construction
- **Random seeds**: Deterministic (sha256-based)
- **Metric computation**: Deterministic (no sampling)
- **Model outputs**: Greedy decoding (no temperature)

## Dependencies

```
pymupdf >= 1.28.2
transformers >= 4.x
torch (CPU)
git >= 2.x
python >= 3.12
```

## Integration Points

This benchmark result integrates with:
- `ledger.jsonl` — hash-chained tamper-evident record
- `Reproducibility/reproducibility.json` — full environment snapshot
- `simulation_data.json` — deterministic synthetic metrics
- `INVESTOR_REPORT.pdf` — compiled investor presentation
- `BENCHMARKS/ANTICLOUD_INVESTOR_MASTER_REPORT.pdf` — master report

---
_Anticloud Lab Environment Record — 2026-09-30T15:41:09.494539+00:00_
