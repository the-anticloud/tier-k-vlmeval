# Intellectual Property Assignment and Prior Art — Anticloud FZ LLE

**Maintainer:** Anticloud FZ LLE · 0-1.gg  
**Contact:** lois@0-1.gg  
**Date:** October 2026  
**Entity:** Anticloud FZ LLE, Dubai Free Zone  
**Ownership:** 100% Lois-Kleinner Alpasan → assigned to Anticloud FZ LLE

---

## Overview

All intellectual property developed under Anticloud — software, systems, formats, protocols, algorithms, documentation, research, and derived works — is assigned to Anticloud FZ LLE. The company has established prior art across its core inventions through a documented, timestamped, independently archived corpus of research, code, and specifications. USPTO prosecution is in progress for the primary novel inventions.

---

## Primary IP Assets

### 1. KANTOR K5 — Post-Quantum Archive Hash

**Description:** A novel deterministic cryptographic hash construction for AI software archives:
```
SHA3-256(archive_sha3 ‖ file_size_le64 ‖ project_name_utf8 ‖ NULL ‖ timestamp_iso)
```
The construction binds archive content, size, project identity, and timestamp in a single verifiable hash resistant to quantum computing attacks. Designed specifically for air-gap AI deployment environments where archive integrity must be verifiable offline.

**USPTO Status:** Pending. Provisional application in drafting as of 2025–2026. Prior art established and documented (see evidence below).

**Prior Art Evidence:**
- First public specification: Anticloud corpus, TIER_1_ANTICLOUD_CORE, timestamped and AIOSS-chained, 2025
- Harvard Dataverse archive: DOI 10.7910/DVN/YMJKOG — AIOSS format specification including K5 construction, archived and DOI-assigned
- Internet Archive snapshot: archive.org/details/anticloud-api-oss-fixed-10-research-index
- ORCID research profile: 0009-0009-2233-6107 — linked publications include K5 specification
- Dev.to publication record: 50 articles, multiple referencing KANTOR K5 by name and construction
- Chain hash of originating commit: `8b4a8a4f6312dfbe885de8280716985637c163fd2a4b5590341d56db1cc4e560`

**Ownership:** Lois-Kleinner Alpasan, assigned to Anticloud FZ LLE

---

### 2. AIOSS Format — AI Operating System Software Ledger

**Description:** An append-only, SHA3-256-chained cryptographic audit ledger for AI inference and software operations. Each entry is:
```
H_n = SHA3-256(H_{n-1} ‖ entry_hash_n ‖ timestamp_n)
```
The AIOSS ledger provides tamper-evident, independently verifiable proof of every AI inference, software deployment, compliance check, and audit event. Designed for air-gap environments where no external timestamping authority is available. The format specification defines entry schema, chain verification protocol, and offline verification kit.

**USPTO Status:** Pending. Covered under same prosecution umbrella as KANTOR K5. Prior art established 2025–2026.

**Prior Art Evidence:**
- AIOSS offline verification kit: Harvard Dataverse DOI 10.7910/DVN/OORKNJ — independently verifiable chain verification tool, archived and DOI-assigned
- AIOSS format specification: Harvard Dataverse DOI 10.7910/DVN/YMJKOG
- Zenodo (CERN) archive: independently timestamped copy of AIOSS specification
- OSF (Open Science Framework): linked research artifacts referencing AIOSS protocol
- Figshare: additional archival copies
- 123-project corpus: every project in the Anticloud corpus references AIOSS chain verification, all projects AIOSS-signed with HASHES.md

---

### 3. System of Things (SoT) — Proprioceptive AI Architecture

**Description:** A neurosymbolic, composable, proprioceptive AI framework where each computational component maintains a typed model of its own state, predicts its next action, produces an AIOSS-chained audit entry, and feeds output back as a proprioceptive signal to the state model. The SoT defines a formal interface language for typed AI components, a self-state representation schema, and a prediction-loop architecture. This constitutes a novel approach to AI system design distinct from nociceptive (stimulus-response) architectures.

**USPTO Status:** Pending. Included in prosecution scope for Anticloud's core architecture patent family.

**Prior Art Evidence:**
- SoT specification: documented across TIER_1_ANTICLOUD_CORE and TIER_4_INFERENCE_AGENTS, timestamped and AIOSS-chained, 2025–2026
- Dev.to publications: multiple articles describing SoT framework by name, indexed and cached
- Press release (October 2026): publicly announces SoT as proprietary architecture, syndicated via Yahoo Finance / Business Insider wire
- Harvard Dataverse: SoT architecture overview archived as part of corpus specification

---

### 4. Anticloud PAX L5 Narrow L2 General 27B — Model Architecture and Training

**Description:** A 27-billion-parameter language model fine-tuned for regulated-vertical deployment, with Q4 quantization for commodity GPU inference ($0.08/1M tokens on T4). Classification under the Morris et al. (2023) AGI taxonomy at L5 Narrow (superhuman in 5 regulated verticals) and L2 General (50th–90th percentile general). The model's training methodology, quantization pipeline, and benchmark evaluation suite constitute proprietary trade secrets and protectable IP.

**USPTO Status:** Trade secret protection in effect. Model weights are proprietary. Fine-tuning methodology and evaluation framework pending inclusion in patent prosecution.

**Prior Art Evidence:**
- Kaggle reproducible benchmark notebook: publicly timestamped, independently verifiable
- OFFICIAL_BENCHMARKS suite: TIER_6_SECURITY_EVAL/K_NANOCHAT/OFFICIAL_BENCHMARKS — run timestamps from 2026-09-30, AIOSS-chained
- 3-seed simulation methodology: seeds 944, 32281, 66480, SHA256(project_name) deterministic — documented in simulation_3seed.md
- ORCID: 0009-0009-2233-6107 — benchmark methodology linked

---

## IP Assignment Chain

| Asset | Creator | Assigned To | Date |
|---|---|---|---|
| KANTOR K5 hash construction | Lois-Kleinner Alpasan | Anticloud FZ LLE | 2025–2026 |
| AIOSS ledger format and protocol | Lois-Kleinner Alpasan | Anticloud FZ LLE | 2025–2026 |
| System of Things (SoT) architecture | Lois-Kleinner Alpasan | Anticloud FZ LLE | 2025–2026 |
| PAX L5/L2 27B model + fine-tuning pipeline | Lois-Kleinner Alpasan | Anticloud FZ LLE | 2025–2026 |
| 123-project corpus (all tiers) | Lois-Kleinner Alpasan | Anticloud FZ LLE | 2025–2026 |
| Anticommons Enterprise License 1.0 | Lois-Kleinner Alpasan | Anticloud FZ LLE | 2025–2026 |

All assignments are to Anticloud FZ LLE as the legal entity. No third-party IP is incorporated into any core Anticloud invention. All open-source dependencies are Apache 2.0 or MIT licensed with no copyleft provisions that affect commercial deployment.

---

## Prior Art Summary

Anticloud's prior art position is strong across all primary inventions. The prior art is:

1. **Timestamped independently** — Harvard Dataverse DOIs are immutable records with independent timestamps assigned by Harvard University Libraries infrastructure
2. **Publicly accessible** — Internet Archive, Zenodo, OSF, Figshare, Dev.to, and ORCID provide independent public access points not controlled by Anticloud
3. **Cryptographically chained** — Every corpus artifact is AIOSS-signed and K5-hashed, providing tamper-evident evidence of when each invention was documented
4. **Cross-platform corroborated** — The same inventions appear across 8+ independent archival platforms, making retroactive manipulation of dates computationally and institutionally infeasible

**The prior art position as of October 2026 is sufficient to support USPTO prosecution and to defend against third-party claims on any of the four primary IP assets.**

---

## Third-Party IP Risk Assessment

| Risk | Assessment |
|---|---|
| Base model (27B parameter foundation) | Open-weight base model used under permissive license. Fine-tuning weights are original. No IP risk. |
| AIOSS chain construction (SHA3-256) | SHA3-256 is a NIST standard. The construction and protocol are novel. No IP risk on underlying primitive. |
| Apache 2.0 corpus dependencies | All 123 projects audited for license compliance. Apache 2.0 / MIT only. No copyleft. No IP risk. |
| K5 hash construction primitives | Uses standard cryptographic primitives (SHA3-256, POSIX primitives). Construction is novel. No IP risk on primitives. |

---

**Prepared by:** Anticloud FZ LLE Internal  
**USPTO counsel:** Engaged, drafting in progress  
**AIOSS chain hash:** `8b4a8a4f6312dfbe885de8280716985637c163fd2a4b5590341d56db1cc4e560`
