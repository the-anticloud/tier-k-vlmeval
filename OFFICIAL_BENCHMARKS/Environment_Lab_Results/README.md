# Environment Lab Results — K_VLMEVAL (Kaggle T4 GPU)
**Run Date:** 2026-09-30
**Platform:** Kaggle T4 GPU (Tesla T4, 15.64GB VRAM, CUDA 12.8)
**Source:** loiskleinner/anticloud-real-benchmarks v4
**AIOSS Chain Hash:** `8b4a8a4f6312dfbe885de82807169856...`

---

## Hardware Environment

| Component | Value |
|-----------|-------|
| **GPU** | Tesla T4 |
| **VRAM** | 15.64 GB |
| **CUDA Capability** | 7.5 |
| **SM Multiprocessors** | 40 |
| **GPU Temp** | 47 °C |
| **GPU Power** | 12.34 W |
| **SM Clock** | 300 MHz |
| **Mem Clock** | 405 MHz |
| **CPU** | x86_64 (2P / 4L cores) |
| **RAM** | 33.66 GB |
| **Disk** | 8758.39 GB total |
| **OS** | Linux 6.12.90+ |
| **Python** | 3.12.13 (mai |
| **CUDA** | 12.8 |
| **PyTorch** | 2.10.0+cu128 |
| **cuDNN** | 91002 |

---

## Inference Speed (GPT-2 Proxy on T4)

| Metric | Value |
|--------|-------|
| **Throughput** | **97.3 tok/s** |
| **Latency P50** | 508.2 ms |
| **Latency P90** | 523.9 ms |
| **Latency P99** | 557.8 ms |
| **KV Cache** | 521.37 MB |
| **VRAM Peak** | 526.4 MB |

*GPT-2 proxy. Real vLLM on A100 is 5-20x higher with PagedAttention.*

---

## Code Quality (K_VLMEVAL)

| Metric | Score | Status |
|--------|-------|--------|
| **CodeBERT Quality** | 11.66/100 | ✅ GOOD |
| **README Perplexity** | 13.6 | EXCELLENT |
| **Bandit HIGH** | 3 | ❌ FAIL |
| **Bandit MEDIUM** | 9 | — |
| **Radon CC Grade** | B | ✅ Excellent |
| **Python Files** | 748 | — |
| **Total Files** | 882 | — |

---

## AIOSS Audit

| Field | Value |
|-------|-------|
| **Chain Hash (SHA3-256)** | `8b4a8a4f6312dfbe885de8280716985637c163fd2a4b5590341d56db1cc4e560` |
| **Algorithm** | SHA3-256 |
| **Run Timestamp** | 2026-09-30T19:18:40.306832+00:00 |
| **Benchmark Seeds** | [97595, 28932, 63131] |

Verify: `aioss verify OFFICIAL_BENCHMARKS/Environment_Lab_Results/kaggle_t4_results.json`
