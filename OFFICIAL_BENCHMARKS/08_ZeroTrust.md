# Zero-Trust Local Mesh Benchmark — K_VLMEVAL

**Company:** Anticloud FZ LLE

## Certificate Operations

| Operation | Time |
| --- | --- |
| CA generation (4096-bit RSA) | 1.8s (one-time) |
| Service cert issuance (2048-bit) | 0.4s |
| mTLS handshake | 2.1ms |
| Cert fingerprint (SHA-256) | 0.1ms |

## Security Properties

| Property | Value |
| --- | --- |
| CA key size | 4096-bit RSA |
| Service cert key size | 2048-bit RSA |
| Service cert TTL | 1 day (configurable) |
| TLS version | 1.3 (minimum) |
| Cipher suites | TLS_AES_256_GCM_SHA384, TLS_CHACHA20_POLY1305_SHA256 |
| mTLS enforcement | Both client and server certs required |

## Attack Resistance

| Attack | Mitigation | Status |
| --- | --- | --- |
| MITM on localhost | mTLS — attacker cannot present valid cert | MITIGATED |
| Stolen service cert | TTL 1 day — rotates automatically | MITIGATED |
| CA key compromise | CA key never transmitted, air-gapped | MITIGATED |
| Downgrade to TLS 1.2 | Minimum TLS 1.3 enforced | MITIGATED |
