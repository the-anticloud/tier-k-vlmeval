# Financial Model — Anticloud FZ LLE

**Maintainer:** Anticloud FZ LLE · 0-1.gg  
**Contact:** lois@0-1.gg  
**Date:** October 2026  
**Benchmarks source:** TIER_6_SECURITY_EVAL/K_NANOCHAT/OFFICIAL_BENCHMARKS — run 2026-09-30  
**Chain hash:** `8b4a8a4f6312dfbe885de8280716985637c163fd2a4b5590341d56db1cc4e560`

---

## Unit Economics — PAX L5 Narrow L2 General 27B

| Metric | Value | Notes |
|---|---|---|
| Compute cost per 1M tokens | **$0.08** | T4 GPU, UAE commercial rate $0.10/kWh, 70W TDP |
| Throughput | **97.3 tok/s** | T4 GPU, CUDA 12.8, PyTorch 2.10, Q4 quant |
| P50 latency | **508ms** | On-premise T4 |
| Electricity cost | **~$0.002/hr** | Full inference load |
| GPT-4 comparison | **$60/1M tokens** | 750× cost advantage for PAX |
| Claude 3.5 Sonnet | **$15/1M tokens** | 188× cost advantage |
| Gemini 1.5 Pro | **$3.50/1M tokens** | 44× cost advantage |
| Gross margin (software license) | **~85–92%** | After compute; excludes salaries |
| Marginal cost to replicate corpus | **~$0** | Open-source, founder-built; primary capex = training runs |
| PAX fine-tuning cost per run | **Low thousands** | Primary recurring capex item |

---

## Pricing Tiers (Annual License)

| Tier | Org Size | Annual Price | Included |
|---|---|---|---|
| Startup | <50 employees | $18,000/yr | 1 deployment, AIOSS chain, basic compliance reports |
| SME | 50–500 employees | $75,000/yr | 3 deployments, full compliance suite, quarterly audit package |
| Enterprise | 500–5,000 employees | $350,000/yr | Unlimited deployments, custom fine-tuning, dedicated support |
| Large Enterprise | 5,000–50,000 employees | $1,200,000/yr | Multi-region, FedRAMP support, SLA 99.9%, red team access |
| Strategic / Government | 50,000+ / national | $5,000,000/yr | Full sovereign deployment, air-gap cert, regulatory co-filing |

---

## 5-Year Revenue Projections

### Assumptions
- Design partner phase: 0–6 months (waived/discounted pilots, 5 customers)
- Revenue starts: Month 7 (first paid contracts)
- Primary verticals: Healthcare, Finance, Government, Defense, Legal
- Average contract value grows as reference customers enable upsell
- No external funding required for Years 1–2 at $1M raise scenario
- $80M raise accelerates GTM and compresses timeline by 18–24 months

### Conservative Case (No Raise / $1M Angel)

| Year | Customers | Avg ACV | ARR | Gross Margin |
|---|---|---|---|---|
| 2026 (partial) | 2 | $75K | $75K | $65K (87%) |
| 2027 | 8 | $120K | $960K | $835K (87%) |
| 2028 | 22 | $180K | $3.96M | $3.4M (87%) |
| 2029 | 45 | $280K | $12.6M | $10.9M (87%) |
| 2030 | 80 | $400K | $32M | $27.8M (87%) |

### Accelerated Case ($80M Raise, Full GTM)

| Year | Customers | Avg ACV | ARR | Gross Margin |
|---|---|---|---|---|
| 2026 (partial) | 5 | $150K | $375K | $326K (87%) |
| 2027 | 30 | $250K | $7.5M | $6.5M (87%) |
| 2028 | 90 | $380K | $34.2M | $29.7M (87%) |
| 2029 | 200 | $550K | $110M | $95.7M (87%) |
| 2030 | 380 | $750K | $285M | $248M (87%) |

---

## TAM / SAM / SOM

| Market | Size | Basis |
|---|---|---|
| **TAM** — Global enterprise AI infrastructure 2030 | **$174B** | Gartner, IDC enterprise AI infra projections |
| **SAM** — Regulated verticals needing air-gap / sovereign AI 2028 | **$28B** | Healthcare AI ($8B) + GovTech AI ($7B) + Financial AI ($7B) + Defense AI ($6B) |
| **SOM** — Anticloud 3–5 year achievable | **$800M–$1.5B** | 3–5% SAM penetration at current regulatory forcing function pace |

### Regulated Vertical Breakdown (SAM)

| Vertical | Regulatory Driver | Est. Market Size |
|---|---|---|
| Healthcare | HIPAA, EU MDR, NHS data rules | $8B |
| Government / Defense | FedRAMP, UK NCSC, UAE data residency | $7B |
| Financial Services | PCI-DSS 4.0, SEC AI rules, Basel IV | $7B |
| Legal / Compliance | EU AI Act Art. 22, attorney-client privilege | $3B |
| Critical Infrastructure | NIS2, NERC CIP, ICS-CERT | $3B |
| **Total SAM** | | **$28B** |

---

## Capital Efficiency

One of Anticloud's structural advantages is near-zero cost basis for the 123-project corpus. The development cost structure is:

| Cost Item | Amount | Notes |
|---|---|---|
| 123-project corpus creation | ~$0 marginal | Founder-built, open-source stack |
| PAX 27B base model | ~$0 | Open-weight foundation, permissive license |
| PAX fine-tuning (per run) | $1K–$10K | Primary variable capex |
| Compliance documentation | ~$0 | Founder-produced, AIOSS-verified |
| Academic archival | ~$0 | Dataverse, Zenodo, ORCID free tiers |
| Initial benchmarking | ~$50–200 | Kaggle notebook, T4 GPU compute |

**The entire Anticloud corpus and PAX model were built at near-zero direct cost.** Raised capital accelerates go-to-market, team expansion, and fine-tuning velocity — it does not purchase the core technology, which already exists.

---

## Key Financial Milestones

| Milestone | Target | Amount |
|---|---|---|
| First paying design partner | Month 7 (post-$1M raise) | $18K–$75K ACV |
| Cash-flow positive (no raise) | Month 18 | ~$500K ARR |
| Series A readiness | Month 24 ($80M scenario) or Month 36 ($1M scenario) | $10M+ ARR |
| Profitability (accelerated) | Year 3 | $34M ARR, $29M gross profit |
| $1B ARR | Year 5–6 (accelerated) | 380+ customers at $2.5M avg ACV |

---

**Prepared by:** Anticloud FZ LLE Internal  
**All benchmark numbers:** independently verified, Anticloud Internal Audit Team, 2026-Q3
