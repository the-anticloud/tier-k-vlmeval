# 3-Seed Simulation — K_VLMEVAL

**Seeds:** `97595` · `28932` · `63131`

**Seed method:** `sha256("K_VLMEVAL")[:8]` as hex→int, offsets +0 / +31337 / +65536

> These seeds are deterministic and documented. Any researcher can reproduce this simulation exactly by running `write_three_seed_simulation.py` with project name `K_VLMEVAL`.

## Confidence Intervals (mean ± σ across 3 seeds)

| Metric | Mean | σ | 95% CI |
|--------|------|---|--------|
| trl_score | 6.9667 | 0.1591 | ±0.3118 |
| throughput_tokens_per_sec | 3487.0 | 31.7409 | ±62.2122 |
| p50_latency_ms | 45.54 | 4.5467 | ±8.9115 |
| p99_latency_ms | 120.7867 | 7.8918 | ±15.4679 |
| ttft_ms | 28.5367 | 4.0048 | ±7.8494 |
| mmlu_proxy | 0.7239 | 0.0305 | ±0.0598 |
| hellaswag_proxy | 0.7894 | 0.0328 | ±0.0643 |
| truthfulqa_proxy | 0.5857 | 0.0446 | ±0.0874 |
| arc_proxy | 0.6741 | 0.0352 | ±0.069 |
| complexity_cyclomatic | 3.84 | 0.3269 | ±0.6407 |
| maintainability_index | 70.0833 | 4.337 | ±8.5005 |
| security_issues_high | 1.3333 | 0.4714 | ±0.9239 |
| dependency_freshness_pct | 81.5667 | 2.9948 | ±5.8698 |
| test_coverage_pct | 51.5667 | 10.5607 | ±20.699 |
| doc_coverage_pct | 68.9667 | 8.695 | ±17.0422 |
| memory_mb | 95.5667 | 3.3718 | ±6.6087 |
| gpu_util_pct | 67.8667 | 3.2294 | ±6.3296 |
| openssf_score | 6.7633 | 0.2963 | ±0.5807 |
| eu_ai_act_compliance_pct | 79.9 | 6.0272 | ±11.8133 |
| slsa_level | 1.0 | 0.0 | ±0.0 |

## Per-Seed Raw Results

| Metric | Seed 97595 | Seed 28932 | Seed 63131 |
|--------|------------|------------|------------|
| trl_score | 7.191 | 6.87 | 6.839 |
| throughput_tokens_per_sec | 3455.1 | 3475.6 | 3530.3 |
| p50_latency_ms | 39.86 | 50.99 | 45.77 |
| p99_latency_ms | 109.78 | 127.89 | 124.69 |
| ttft_ms | 30.79 | 22.91 | 31.91 |
| mmlu_proxy | 0.767 | 0.7024 | 0.7024 |
| hellaswag_proxy | 0.8173 | 0.8076 | 0.7434 |
| truthfulqa_proxy | 0.5823 | 0.6419 | 0.5328 |
| arc_proxy | 0.6735 | 0.7175 | 0.6312 |
| complexity_cyclomatic | 4.3 | 3.57 | 3.65 |
| maintainability_index | 73.12 | 63.95 | 73.18 |
| security_issues_high | 1 | 1 | 2 |
| dependency_freshness_pct | 78.7 | 85.7 | 80.3 |
| test_coverage_pct | 66.5 | 43.9 | 44.3 |
| doc_coverage_pct | 57.0 | 77.4 | 72.5 |
| memory_mb | 92.7 | 93.7 | 100.3 |
| gpu_util_pct | 64.7 | 66.6 | 72.3 |
| openssf_score | 6.71 | 6.43 | 7.15 |
| eu_ai_act_compliance_pct | 88.4 | 76.2 | 75.1 |
| slsa_level | 1 | 1 | 1 |

---
_Anticloud 3-Seed Simulation — 2026-09-30T16:01:40.704491+00:00_
_Citation: Lois-Kleinner. (2026). The Anticloud. DOI: pending._