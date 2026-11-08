# TRL Best Practices & Guidelines

**Source:** [https://www.nature.com/articles/s41467-022-33128-9](https://www.nature.com/articles/s41467-022-33128-9)

**Last Updated:** 2026-09-30T15:17:39.312703+00:00

## TRL Best Practices for AI/ML Systems

### What TRL Measures
Technology Readiness Level (TRL) for ML (Lavin et al. 2022, Nature Communications) uses a 1–9 scale:
- TRL 1–3: Research (concept, feasibility, proof-of-concept)
- TRL 4–6: Development (prototype, validation, demo)
- TRL 7–9: Deployment (pre-production, qualified, operational)

### TRL 8 Requirements (Target)
1. **System complete and qualified** via test and demonstration
2. **CI/CD pipelines** for continuous integration
3. **A/B testing, shadow testing, canary testing** conducted
4. **Stakeholder sign-off** (go/no-go decision documented)
5. **Stress testing** under operational conditions

### TRL 9 Path (Beyond Target)
- Deploy in production with real users
- Monitor for drift, degradation, bias
- Document operational incidents and recovery
- Achieve >99.9% uptime SLA

### Implementation Strategy
1. Run `run_benchmarks_comprehensive.py` monthly
2. Address failing TRL factors in priority order: tests > CI/CD > docs > licence
3. Track TRL progression in `ledger.jsonl`
4. Gate releases at TRL 7+ minimum

### Common Gaps
- Missing `.github/workflows/` = no CI/CD = TRL cap at 6
- Missing `tests/` = no automated validation = TRL cap at 5
- Unlicensed code = undeployable = TRL cap at 4
