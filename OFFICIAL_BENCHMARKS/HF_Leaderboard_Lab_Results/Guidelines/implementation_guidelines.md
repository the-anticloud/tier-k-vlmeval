# Implementation Guidelines: HF_Leaderboard_Lab_Results

> Source: [https://huggingface.co/docs/leaderboards/en/open_llm_leaderboard/archive](https://huggingface.co/docs/leaderboards/en/open_llm_leaderboard/archive)

## HuggingFace Open LLM Leaderboard — Benchmarking Guide

### Full Benchmark Suite (requires GPU)
| Benchmark | Metric | What It Tests |
| --------- | ------ | ------------- |
| **MMLU** (5-shot) | Accuracy across 57 subjects | Knowledge breadth |
| **HellaSwag** (10-shot) | Accuracy | Commonsense inference |
| **TruthfulQA** (0-shot) | MC accuracy | Truthfulness vs. falsehoods |
| **ARC** (25-shot) | Accuracy | Science reasoning |
| **Winogrande** (5-shot) | Accuracy | Coreference resolution |
| **GSM8K** (5-shot) | Accuracy | Math word problems |

### Open LLM Leaderboard v2 (Oct 2024) — Additional Benchmarks
- **IFEval**: Instruction following
- **BBH (BIG-Bench Hard)**: Complex reasoning
- **MATH Level 5**: Competition math
- **GPQA**: Graduate-level science
- **MuSR**: Multi-step reasoning
- **MMLU-Pro**: Extended MMLU

### CPU Proxy Metrics (this suite)
Since full benchmarks require GPU:
- **Inference latency (avg/p50/p99)** via distilbert
- **Tokenization speed** (tokens/ms)
- **Classification consistency** across 3 seeds (HELM-style)
- **Throughput** (samples/second)

### Roadmap to Full HF Benchmarks
1. Set up Kaggle notebook with T4 GPU (free tier)
2. Use `lm-evaluation-harness` from EleutherAI
3. Run MMLU + HellaSwag + ARC at minimum
4. Submit results to HF Leaderboard for public visibility
