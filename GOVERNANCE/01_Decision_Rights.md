# Governance

**Project:** `K_VLMEVAL`  
**Tier:** TIER_6_SECURITY_EVAL  
**Identity:** Upstream `open-compass/VLMEvalKit` @ `54a063c5bf75` (Apache-2.0)

## What is authoritative here

| Artifact | Authority | Notes |
| --- | --- | --- |
| `ledger/ledger.aioss` | append-only record of what was done | 0 blocks, chain verified |
| `UPSTREAM/.anticloud-provenance.json` | upstream identity | written at clone time, not editable afterwards |
| `anticloud-edits.json` | every change to the vendored tree | one record per patch, with its test |
| `ground_truth.json` | which claims are permitted | frozen |

## Decision rights

Nothing in this project is decided by majority preference. A change lands
when its effect is recorded in the ledger and, if it touches the vendored
tree, when its patch carries a test that fails before it and passes after.
A change with no test is treated as a claim, not a change.

## Change control

1. Propose the behaviour change in one sentence.
2. Show the test that currently fails.
3. Apply, then show the same test passing.
4. Record the patch in `anticloud-edits.json`.
5. Re-verify the chain with `anticloud verify`.

Steps 2 and 3 are not optional. A patch whose only effect is to write to
the ledger is rejected by `anticloud audit-edits`, which is the mechanism
that stops this project from reporting bookkeeping as improvement.
