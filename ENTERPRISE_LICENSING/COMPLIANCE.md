# K_VLMEVAL — Compliance & Regulatory Posture

## Security
- **Bandit** static analysis run on every release (target: 0 HIGH findings)
- **Radon** cyclomatic complexity maintained at B or better
- **AIOSS SHA3-256 ledger** provides cryptographic audit trail for all operations
- **OWASP Top 10** mitigations documented in SECURITY/ folder

## Data Sovereignty
K_VLMEVAL is designed to operate with zero data egress:
- All model weights stored locally
- No telemetry transmitted to Anticloud FZ LLE or upstream vendors
- AIOSS ledger is local-first; export is opt-in

## Standards Alignment
| Standard | Status |
|----------|--------|
| NIST SP 800-53 | Aligned (controls mapped in NIST_CONTROLS.md) |
| SOC 2 Type II | Roadmap Q4 2026 |
| ISO 27001 | Roadmap 2027 |
| GDPR Art. 25 (Privacy by Design) | Implemented — no personal data processing by default |
| UAE PDPL | Compliant — data resident in-country |

## Export Control
K_VLMEVAL does not include cryptographic key generation functionality subject to EAR/ITAR.
AIOSS SHA3-256 is a hash function (EAR §742.15 exception applies).
Consult your export control officer before deploying in restricted jurisdictions.
