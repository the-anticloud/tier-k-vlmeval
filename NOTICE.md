# NOTICE

K_VLMEVAL
Copyright 2026 Anticloud FZ LLE. Author: Lois-Kleinner Alpasan.

## Licencing

This work is licensed under **Anticommons 0.1.0**, a dual licence:

- **Apache License 2.0** (open source path, fully permissive), or
- **Anticloud Enterprise License** (support, warranty, indemnification,
  capped liability).

Full text: see `LICENSE.md` in this directory. Canonical source of the
licence text: `Anticommons_0.1.0/01_LICENSE.md` in the Anticloud corpus root.
Legal entity: **Anticloud FZ LLE** (Limited Liability Establishment).

## Required attribution

As required by Anticommons 0.1.0 condition 3:

> Portions of this software are based on Anticommons by Lois-Kleinner Alpasan

## Notice of changes (Anticommons 0.1.0 condition 2)

This project is **not** a fork and contains **no** modifications to the
vendored upstream source. Specifically:

- `UPSTREAM/` is an unmodified shallow clone (`--depth 1`) of
  https://github.com/open-compass/VLMEvalKit
  - commit `0`
  - committed `-`
  - upstream licence: **Apache-2.0** (permissive)
  - Retained verbatim: `LICENSE`

  The upstream project is copyright its own authors and is separately
  licensed under Apache-2.0. No Anticloud code is placed inside `UPSTREAM/`,
  and no upstream file is edited.

- `src/k_vlmeval_anticloud/` is original Anticloud code. It is an **adapter** that drives
  the vendored upstream and adds:
  - AIOSS tamper-evident ledger recording on every operation
  - offline enforcement (no frontier API dependency)
  - provenance loading from the recorded upstream commit and licence

- Changes made to the upstream project, if any are later proposed upstream,
  will be submitted as separate patches and will not be silently applied to
  the vendored copy.

## Third-party notice

Vendored upstream dependencies retain their own licences. Each vendored
component records its licence in `UPSTREAM/.anticloud-provenance.json`.
