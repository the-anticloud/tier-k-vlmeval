# SOC 2 Type II Readiness Guide

**Source:** [https://soc2auditors.org/insights/soc-2-for-ai-companies/](https://soc2auditors.org/insights/soc-2-for-ai-companies/)

**Last Updated:** 2026-09-30T15:17:39.312703+00:00

## SOC 2 Type II — AI Company Readiness Guide (2026)

### Five Trust Service Criteria
1. **Security (CC6-CC9)** — Access controls, encryption, monitoring
2. **Availability (A1)** — Uptime SLAs, disaster recovery, capacity planning
3. **Processing Integrity (PI1)** — Data processing accuracy, completeness, timeliness
4. **Confidentiality (C1)** — Data classification, encryption at rest/transit
5. **Privacy (P1-P8)** — GDPR alignment, data minimization, consent management

### AI-Specific Controls (2026)
- **LLM Subprocessors**: Obtain SOC 2 or ISO 27001 from all model providers
- **Model Governance**: Drift monitoring dashboards with alerting
- **Change Management**: Every model deployment needs approval ticket + rollback plan
- **Training Data**: Data lineage documentation for all training datasets
- **ISO 42001**: AI governance layer — implement in parallel with SOC 2

### Readiness Score Interpretation
- 100%: Ready for Type II audit engagement
- 80-99%: Minor gaps — address within 30 days
- 60-79%: Moderate gaps — 60-90 day remediation plan needed
- <60%: Major gaps — do not claim SOC 2 compliance

### Evidence Required for Audit
- CI/CD workflow logs (at least 6 months)
- Access review records
- Incident response logs
- Vendor risk assessments (for HuggingFace, Kaggle, etc.)
- Model deployment approval records
