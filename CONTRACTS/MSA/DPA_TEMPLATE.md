# Data Processing Addendum (DPA) — K_VLMEVAL

This DPA supplements the MSA and governs processing of Personal Data
by K_VLMEVAL in connection with Customer's use of optional cloud-connected features.

## Applicability
This DPA applies ONLY if Customer opts into features that transmit data
outside Customer's infrastructure. By default, K_VLMEVAL operates fully
offline — this DPA is not applicable.

## Data Categories
If opted in, the following may be processed:
- Inference metadata (token counts, latency, model name) — no prompt or output content
- AIOSS ledger export hashes — SHA3-256 only, no raw data
- System telemetry (CPU/GPU utilization, error rates)

## Sub-processors
Provider uses no sub-processors for K_VLMEVAL by default.
Any future sub-processors will be notified 30 days in advance.

## Data Subject Rights
Customer is the Data Controller. Provider will assist Customer in
responding to data subject requests within 72 hours of Customer's request.

## Security Measures
Provider implements: TLS 1.3 in transit, AES-256 at rest,
SHA3-256 chain-hash integrity, SOC 2 Type II (roadmap Q4 2026).

## Deletion
Upon termination, Provider will delete or return all Customer Data
within 30 days, confirmed in writing.

## Governing Law
UAE Federal Decree-Law No. 45 of 2021 (PDPL) and GDPR Article 28.
