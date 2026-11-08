# Cryptographic Provenance Benchmark — K_VLMEVAL

**Company:** Anticloud FZ LLE

## Receipt Generation Performance

| Operation | Time |
| --- | --- |
| Single receipt creation | 0.8ms |
| Chain verify (100 entries) | 2.1ms |
| Chain verify (10K entries) | 198ms |
| File hash (1MB) | 4.2ms |
| File hash (1GB) | 4,200ms |

## Chain Integrity Tests

| Test | Result |
| --- | --- |
| Sequential append | PASS |
| Tamper detection (modify entry 50 of 100) | PASS — detected at entry 50 |
| Reload from disk | PASS — head matches |
| Cross-node receipt verification | PASS — node fingerprint stable |

## Hash Algorithm

SHA3-256 (NIST FIPS 202). Collision resistance: 2^128.
No MD5, no SHA1, no SHA2-256 (SHA3 only).
