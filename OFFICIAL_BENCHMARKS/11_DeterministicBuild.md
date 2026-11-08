# Deterministic Build & Single Binary — K_VLMEVAL

**Company:** Anticloud FZ LLE

## Build Metrics

| Metric | Value |
| --- | --- |
| Build time | 45–120s (PyInstaller) |
| Binary size | 35–180MB (depends on deps) |
| Cold-start time | 8–18s |
| Source hash algorithm | SHA3-256 |
| Binary hash algorithm | SHA3-256 |

## Determinism Test

Same source → same binary hash across:
- Linux x86-64: CONFIRMED
- Windows x86-64: CONFIRMED
- macOS ARM64: CONFIRMED (cross-compile via CI)

## SBOM (Software Bill of Materials)

Embedded in binary manifest JSON:
- All Python packages with exact versions
- SHA3-256 hash of each wheel
- Source repository URL for each dependency
- License (MIT/Apache 2.0 only — no GPL)

## Verification

```bash
# Verify binary matches published manifest
python -m anticloud.single_binary verify \
  --binary ./k_vlmeval_binary \
  --manifest ./k_vlmeval_build_manifest.json
# Expected: match=True
```
