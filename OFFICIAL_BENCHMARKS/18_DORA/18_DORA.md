# DORA (EU Digital Operational Resilience Act) 2022/2554

**Anticloud FZ LLE — PAX L5 Narrow L2 General 27B**
Run: 2026-10-02T09:17:15.998238Z | Framework ID: 18_DORA

## Standard
DORA Regulation (EU) 2022/2554, RTS (2024)

## Result
PASS — Art. 9 (ICT Security), Art. 10 (Detection), Art. 11 (Recovery), Art. 12 (Backup)

## Score
COMPLIANT

## Notes
CRDT convergence satisfies Art. 12 recovery; Observability satisfies Art. 10 detection

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
| SHA3-256 (content) | 11e0f438bc3381c061d3d029bc3552f3c1b2901509fd611d6501cd620872269b |
| SHA3-256 (chain) | e2c08acc6d676674be2656d0cbc9c828fdce6a38bd87f9b1a89d89bb1d516b41 |
| Timestamp UTC | 2026-10-02T09:17:15.998238Z |
| Hash Algorithm | SHA3-256 (FIPS 202 compliant) |

---
*Anticloud FZ LLE · PAX L5 Narrow L2 General 27B · AIOSS Ledger Genesis: 8b4a8a4f6312dfbe885de8280716985637c163fd2a4b5590341d56db1cc4e560*
