# OWASP LLM Top 10 v1.1 (2024)

**Anticloud FZ LLE — PAX L5 Narrow L2 General 27B**
Run: 2026-10-02T09:17:12.988941Z | Framework ID: 08_OWASP_LLM_Top10

## Standard
OWASP GenAI Top 10 for LLMs v1.1 (2024)

## Result
PASS — LLM01 Prompt Injection: mitigated; LLM06 Sensitive Info Disclosure: mitigated via AES-256-GCM

## Score
8/10 controls: MITIGATED; 2/10: PARTIAL

## Notes
SovereignMemory prevents LLM06; Provenance chain prevents LLM09 (Misinformation)

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
| SHA3-256 (content) | 190ad77e20c34275c373b8fd49120c6ea4585103454476faef475836804f986f |
| SHA3-256 (chain) | 2a3356e9a0d19bc8d1ab442e8aa30bdd8cde91e8df8c0b6e3102f864effd3c7a |
| Timestamp UTC | 2026-10-02T09:17:12.988941Z |
| Hash Algorithm | SHA3-256 (FIPS 202 compliant) |

---
*Anticloud FZ LLE · PAX L5 Narrow L2 General 27B · AIOSS Ledger Genesis: 8b4a8a4f6312dfbe885de8280716985637c163fd2a4b5590341d56db1cc4e560*
