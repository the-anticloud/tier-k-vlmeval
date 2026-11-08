# PAX_Results_Lab_Results

**Project:** `K_VLMEVAL` | **Tier:** `TIER_6_SECURITY_EVAL` | **Run:** `2026-09-30T15:11:19.033679+00:00`

**Framework:** Anticloud PAX (Patch/Apply/Xvalidate) Ledger Protocol

**Source:** [Internal — anticloud-edits.json + LEDGERS/ chain](Internal — anticloud-edits.json + LEDGERS/ chain)

**Status:** `PASS`

```json
{
  "checks": [
    {
      "check": "upstream_exists",
      "pass": true,
      "desc": "UPSTREAM/ directory present"
    },
    {
      "check": "git_index_exists",
      "pass": true,
      "desc": ".git/index present (not corrupted)"
    },
    {
      "check": "ledger_dir_exists",
      "pass": true,
      "desc": "LEDGERS/ directory present"
    },
    {
      "check": "anticloud_edits_exists",
      "pass": true,
      "desc": "anticloud-edits.json present"
    },
    {
      "check": "edits_not_empty",
      "pass": true,
      "desc": "anticloud-edits.json non-empty"
    }
  ],
  "passed": 5,
  "total": 5,
  "pax_score": 1.0,
  "edits_count": 1,
  "status": "PASS"
}
```

---
_Anticloud Benchmark Suite — 2026-09-30T15:11:19.033679+00:00_