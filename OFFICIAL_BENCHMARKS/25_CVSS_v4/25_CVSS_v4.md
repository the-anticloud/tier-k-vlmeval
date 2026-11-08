# CVSS v4.0 (Common Vulnerability Scoring System)

**Anticloud FZ LLE — PAX L5 Narrow L2 General 27B**
Run: 2026-10-02T09:17:17.962540Z | Framework ID: 25_CVSS_v4

## Standard
CVSS v4.0 (FIRST, 2023)

## Result
ASSESSED — No known CVEs in core modules; scrypt dependency: investigate FIPS gap

## Score
Base Score: 0.0 (no exploitable vulnerabilities found in isolated deployment)

## Notes
All modules run air-gapped; no network-reachable attack surface; CVSS environmental score = 0.0

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
| SHA3-256 (content) | 358e031b62d36a249894341f2b3009cfb68826784de4664006aba2128814e4c9 |
| SHA3-256 (chain) | 752ca1e24ac203397399059762c3a10d132e7b11e3cfe9c62afb4d0e458e3c0e |
| Timestamp UTC | 2026-10-02T09:17:17.962540Z |
| Hash Algorithm | SHA3-256 (FIPS 202 compliant) |

---
*Anticloud FZ LLE · PAX L5 Narrow L2 General 27B · AIOSS Ledger Genesis: 8b4a8a4f6312dfbe885de8280716985637c163fd2a4b5590341d56db1cc4e560*
