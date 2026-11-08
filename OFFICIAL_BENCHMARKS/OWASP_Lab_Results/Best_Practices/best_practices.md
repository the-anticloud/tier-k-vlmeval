# OWASP LLM Top 10 Implementation Strategy

**Source:** [https://genai.owasp.org/resource/llm-top-10-for-llms-v1-1/](https://genai.owasp.org/resource/llm-top-10-for-llms-v1-1/)

**Last Updated:** 2026-09-30T15:17:39.312703+00:00

## OWASP LLM Top 10 v1.1 (2024) — Implementation Guide

### The 10 Risks
1. **LLM01 Prompt Injection** — Sanitize and validate all user inputs before passing to model
2. **LLM02 Insecure Output Handling** — Escape model outputs before rendering; never eval() raw output
3. **LLM03 Training Data Poisoning** — Audit training data sources; use data provenance tracking
4. **LLM04 Model Denial of Service** — Rate limit inference endpoints; set max token limits
5. **LLM05 Supply Chain Vulnerabilities** — Pin model versions; verify checksums (this SLSA ties in)
6. **LLM06 Sensitive Information Disclosure** — Never log user prompts containing PII
7. **LLM07 Insecure Plugin Design** — Validate all plugin inputs and outputs
8. **LLM08 Excessive Agency** — Principle of least privilege for agent tool access
9. **LLM09 Overreliance** — Always present model uncertainty; require human review for high-stakes
10. **LLM10 Model Theft** — Auth all model endpoints; rate limit; monitor for extraction attempts

### Implementation Checklist per Project
- [ ] Input sanitization before model calls
- [ ] Output escaping before rendering
- [ ] Rate limiting on inference endpoints
- [ ] Secret management via env vars (not hardcoded)
- [ ] Confidence thresholds before autonomous action
- [ ] Auth on all model-serving endpoints
- [ ] Regular dependency scanning (pip-audit, safety)

### Scoring Guide
- 5/5 PASS: Production-ready security posture
- 3-4/5: Acceptable, address gaps in next sprint
- 1-2/5: HIGH RISK — block deployment until resolved
- 0/5: CRITICAL — immediate remediation required
