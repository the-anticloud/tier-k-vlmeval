# SBOM (Software Bill of Materials) — NTIA/CISA Minimum Elements

**Anticloud FZ LLE — PAX L5 Narrow L2 General 27B**
Run: 2026-10-02T09:17:17.304586Z | Framework ID: 23_SBOM

## Standard
NTIA SBOM Minimum Elements (2021), EO 14028 (2021), CISA SBOM guidance

## Result
PASS — Supplier, Component, Version, Hash, Relationship all captured in manifest

## Score
MINIMUM ELEMENTS: ALL PRESENT

## Notes
SingleBinary.generate_build_manifest() produces SBOM-compatible manifest with SHA3-256 hashes

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
| SHA3-256 (content) | acf71857d6ede6b7ab48884a3ee83c58e351f0bd84e2cbb984d5a7440d0800c8 |
| SHA3-256 (chain) | 7bef7533599a425627a07e8aebe03129234ee560cb476641754e388a0f94837d |
| Timestamp UTC | 2026-10-02T09:17:17.304586Z |
| Hash Algorithm | SHA3-256 (FIPS 202 compliant) |

---
*Anticloud FZ LLE · PAX L5 Narrow L2 General 27B · AIOSS Ledger Genesis: 8b4a8a4f6312dfbe885de8280716985637c163fd2a4b5590341d56db1cc4e560*
