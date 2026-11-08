# Compliance Checklist — K_VLMEVAL
**Tier:** T6 | **Date:** 2026-09-30

## Pre-Deployment

- [ ] License key provisioned from enterprise@anticloud.dev
- [ ] AIOSS ledger binary (`aioss`) installed and `aioss verify` passes
- [ ] SHA3-256 chain hash recorded in deployment manifest
- [ ] NOTICE.md present with upstream attribution
- [ ] anticloud-edits.json updated with deployment metadata

## Security

- [ ] Bandit scan: 0 HIGH issues
- [ ] pip-audit: no known CVEs in dependencies
- [ ] OWASP dependency check run
- [ ] Network egress limited to AIOSS verification endpoint (optional for air-gap)

## Data Sovereignty

- [ ] All inference data confirmed to remain on Licensee infrastructure
- [ ] No telemetry endpoints in K_VLMEVAL integration code
- [ ] AIOSS ledger stored on Licensee-controlled storage

## Audit Trail

- [ ] `aioss verify` output archived
- [ ] Chain hash logged in SIEM
- [ ] Deployment recorded in CONTRACTS/MSA/deployment_log.json

## Annual Review

- [ ] License renewal before expiry
- [ ] Updated chain hash after any component upgrade
- [ ] Re-run bandit/OWASP after dependency updates
