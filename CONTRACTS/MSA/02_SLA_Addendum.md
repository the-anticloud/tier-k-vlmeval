# SLA Addendum — K_VLMEVAL
**Addendum to MSA** | 2026-09-30

## Uptime Commitment

AIOSS Ledger Verification API: **99.5% monthly uptime**

Exclusions: scheduled maintenance (announced 48h in advance),
force majeure, Customer-caused outages.

## Performance Benchmarks (Contractual)

| Metric | Commitment | Measurement |
|--------|-----------|-------------|
| AIOSS verify latency | < 200ms p99 | 30-day rolling |
| Ledger append throughput | > 1,000 entries/sec | Peak load test |
| Chain hash verification | < 50ms | Per-call |

## Monitoring

- Status page: status.anticloud.dev (when available)
- Incident notifications via email within 30 minutes of P1 detection
- Post-incident report within 5 business days of P1 resolution

## Credits

| Monthly Uptime | Credit |
|----------------|--------|
| 99.0–99.5% | 10% |
| 95.0–99.0% | 25% |
| < 95.0% | 50% |

Credits applied to next invoice; no cash refunds.
