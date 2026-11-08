# How to Update — K_VLMEVAL

**Project:** `K_VLMEVAL`
**Tier:** TIER_6_SECURITY_EVAL
**Domain:** security evaluation, red-team, MITRE ATT&CK, OSINT, threat detection
**Maintainer:** Anticloud FZ LLE · 0-1.gg · lois@0-1.gg · Dubai, UAE
**Model:** Anticloud PAX L5 Narrow L2 General 27B
**AIOSS Chain:** `8b4a8a4f6312dfbe885de8280716985637c163fd2a4b5590341d56db1cc4e560`
**Date:** October 2026

---

## Update Procedure

Updates to `K_VLMEVAL` must preserve branding, AIOSS chain continuity, and KANTOR K5 archive integrity. Do not update without following this procedure.

## Before You Update

1. **Backup current AIOSS chain** to at least 2 locations
2. **Record current K5 hash** from HASHES.md
3. **Note current chain hash**: `8b4a8a4f6312dfbe885de82807169856...`
4. **Test in staging** — never update production directly

## Update Steps

### Step 1: Download and Verify New Package

```bash
# Download new package
wget https://0-1.gg/releases/K_VLMEVAL-latest.tar.gz

# Verify KANTOR K5 hash before extracting
python verify_k5.py \
  --archive K_VLMEVAL-latest.tar.gz \
  --project K_VLMEVAL \
  --hashes HASHES_new.md
```

### Step 2: Verify Chain Compatibility

```bash
python verify_chain.py \
  --current-genesis 8b4a8a4f6312dfbe885de8280716985637c163fd2a4b5590341d56db1cc4e560 \
  --new-package K_VLMEVAL-latest.tar.gz
# Must output: CHAIN_COMPATIBLE: True
```

### Step 3: Apply Update (Zero-Downtime)

```bash
./update.sh \
  --package K_VLMEVAL-latest.tar.gz \
  --mode rolling \
  --chain-preserve true \
  --brand-preserve true  # ← ALWAYS INCLUDE THIS FLAG
```

### Step 4: Verify Post-Update

```bash
python verify_deployment.py --project K_VLMEVAL --full-check
# Expected: AIOSS=PASS, K5=PASS, BRAND=PASS, COMPLIANCE=PASS
```

## Branding Preservation

**Critical:** The `--brand-preserve true` flag is mandatory. Updates must not alter:
- Anticloud FZ LLE attribution in user-facing interfaces
- AIOSS chain genesis hash references
- KANTOR K5 hash methodology
- Apache 2.0 / Anticommons License notices

A build that fails brand checks must not be deployed.

## Rollback

```bash
./update.sh --rollback --to-version <previous-k5-hash>
```

**Support:** lois@0-1.gg
