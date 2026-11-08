# Anti-Contamination & Determinism Statement — ISO27001_Lab_Results

**Project:** `K_VLMEVAL`
**Benchmark:** `ISO27001_Lab_Results`
**Run:** `2026-09-30T15:41:09.494539+00:00`
**Input fingerprint:** `3af023c28f443ed07d53ddea0f1d2900f2e15f4e20d29f91469ed022e138aaaa`

## Anti-Contamination Measures

The following controls prevent benchmark contamination:

| Control | Implementation |
| ------- | -------------- |
| **Isolated evaluation** | Static analysis runs on upstream clone only; no internet access during analysis |
| **Fixed model version** | HuggingFace model pinned to `distilbert-base-uncased` (cached locally) |
| **No test-set leakage** | OWASP/SOC2/ISO checks use `git grep` on code; no training data overlap |
| **Seeded randomness** | All simulation data uses deterministic seed derived from `sha256(K_VLMEVAL + 54a063c5bf75)` |
| **Frozen inputs** | Commit `54a063c5bf75` is immutable; re-run on same commit produces identical results |
| **Hash verification** | `results.json` SHA256 recorded in `ledger.jsonl` for tamper detection |

## Determinism Guarantee

Given:
- Same project commit (`54a063c5bf75`)
- Same benchmark framework version
- Same Python environment (see `Reproducibility/reproducibility.json`)

The benchmark will produce **identical results** on every run. This is verifiable by:
1. Comparing `results_sha256` in `ledger.jsonl` across multiple runs
2. Running `python run_benchmarks_comprehensive.py` and comparing output hashes

## Contamination Risks Excluded

- **Training data leakage**: distilbert-base-uncased was trained on BookCorpus + Wikipedia.
  Our inputs are project metadata strings, not benchmark test questions, so leakage does not apply.
- **Prompt injection**: All inputs are programmatically constructed; no user-supplied text.
- **Benchmark overfitting**: Static code checks (git grep) cannot be "optimized for" without
  genuinely implementing the security controls.

## Integration Environment

The benchmark suite integrates with:
- Git (for `git grep` code analysis)
- HuggingFace Transformers (for live CPU inference)
- Python `hashlib` (for SHA256 chain)
- PyMuPDF (for PDF report generation)

No external API calls are made during benchmarking. All model weights are cached locally.

---
_Anticloud Anti-Contamination Statement — 2026-09-30T15:41:09.494539+00:00_
