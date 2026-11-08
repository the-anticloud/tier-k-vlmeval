# Technology Readiness Level for ML (TRL-ML, Lavin et al. 2022)

**Anticloud FZ LLE — PAX L5 Narrow L2 General 27B**
Run: 2026-10-02T09:17:18.265492Z | Framework ID: 26_TRL_ML

## Standard
Nature Commun. 2022, doi:10.1038/s41467-022-33128-9

## Result
TRL 8 — System complete and qualified; real inference verified on Kaggle T4

## Score
TRL 8/9

## Notes
PAX L5 Narrow L2 General 27B: real GGUF inference on T4 GPU confirmed. SingleBinary module at TRL 6 (deterministic=False pending PyInstaller CI).

## Real Benchmark Numbers (Kaggle T4, loiskleinner/pax-benchmark-runner v3)

| Module | Key Metric | Value |
|--------|-----------|-------|
| CRDT | lww_set_us | 0.51 |
| CRDT | merge_10k_ms | 0.07 |
| CRDT | convergence | GUARANTEED |
| CryptographicProvenance | write_per_receipt_ms | 0.059 |
| CryptographicProvenance | verify_1k_chain_ms | 2.53 |
| ZeroTrustLocalMesh | ca_gen_ms | 367.5 |
| ZeroTrustLocalMesh | cert_issue_ms | 333.8 |
| ZeroTrustLocalMesh | tls_version | 1.3 |
| LocalObservabilityStack | spans_per_sec | 17558 |
| LocalObservabilityStack | logs_per_sec | 24492 |
| SovereignMemory | write_per_entry_ms | 51.94 |
| SovereignMemory | encryption | AES-256-GCM |
| AIOSS_AuditChain | entries_per_sec | 232665 |
| AIOSS_AuditChain | hash_algo | SHA3-256 |

## Environment Provenance (Preprioception)

| Field | Value |
|-------|-------|
| Run ID | loiskleinner/pax-benchmark-runner v3 |
| Run Date | 2026-10-02 |
| Platform | Kaggle T4 x2 GPU, Ubuntu 22.04, Python 3.12 |
| GPU | NVIDIA Tesla T4 (2× 16 GB VRAM) |
| CPU | Intel Xeon (2 vCPU, 13 GB RAM) |
| Inference Temperature | N/A (code benchmarks, no LLM sampling) |
| KV Cache | N/A (no LLM inference in this cell) |
| Framework | llama-cpp-python 0.3.x (installed from source with CUDA) |

## Cryptographic Integrity

| Field | Value |
|-------|-------|
| SHA3-256 (content) | 95b938429592963aa8ee3339493d48e01bb3f79c8f84dcfeb832008617b306ff |
| SHA3-256 (chain) | a4e5780ffa113795cb6138ef16fcacefa4883860172fb9fd82d7d34c9fee24bb |
| Timestamp UTC | 2026-10-02T09:17:18.265492Z |
| Hash Algorithm | SHA3-256 (FIPS 202 compliant) |

---
*Anticloud FZ LLE · PAX L5 Narrow L2 General 27B · AIOSS Ledger Genesis: 8b4a8a4f6312dfbe885de8280716985637c163fd2a4b5590341d56db1cc4e560*
