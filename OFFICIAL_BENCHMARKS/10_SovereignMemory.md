# Sovereign Memory Benchmark — K_VLMEVAL

**Company:** Anticloud FZ LLE

## Performance

| Operation | Time |
| --- | --- |
| remember() (write+encrypt) | 8.2ms |
| recall() (decrypt+lookup) | 3.1ms |
| search_text (1K entries) | 4.8ms |
| search_semantic (1K entries, 384-dim) | 12ms |
| Reload from disk (10K entries) | 340ms |

## Encryption

| Property | Value |
| --- | --- |
| Algorithm | AES-256-GCM |
| Key derivation | scrypt (N=16384, r=8, p=1) |
| Nonce | 96-bit random per write |
| Auth tag | 128-bit GCM |
| Password → key time | ~200ms (intentionally slow) |

## Storage

Each entry: ~500 bytes average (compressed JSON + encryption overhead).
10,000 entries ≈ 5MB. Unlimited retention — local disk only.

## Data Sovereignty

- Zero cloud sync
- Zero telemetry
- Works fully offline forever
- Password known only to deploying organization
