# Anticloud Scaffold

{GENERATED}
## {name} ({pkg})

### What we added

| Path | Role |
|---|---|
| `src/{pkg}/` | Anticloud adapter. Original code; drives the vendored upstream. |
| `src/{pkg}/cli.py` | Subcommands; each writes an AIOSS ledger block. |
| `src/{pkg}/provenance.py` | Loads the recorded upstream commit and licence. |
| `ledger/ledger.aioss` | Append-only hash chain of actual operations. |
| `tests/test_contract.py` | Cross-cutting guarantees, not project-specific claims. |
| `UPSTREAM/` | Unmodified shallow clone. |
| `LICENSE.md` / `NOTICE.md` | Anticommons 0.1.0 text, and our notice of changes. |

### Guarantees the contract tests enforce

1. `UPSTREAM/.git` exists, so the provenance record is backed by a real clone.
2. A licence was detected at vendor time; it is not a placeholder.
3. The ledger round-trips through init, append, and verify.
4. No frontier API key appears in this project tree.
5. The CLI entry point imports and responds to `--help`.

### Run it

```
pip install -e .
{pkg} provenance     # what upstream is vendored, at which commit
{pkg} notice        # the licence split: ours vs upstream's
{pkg} offline check # assert no frontier dependency
{pkg} ledger verify # check the hash chain
pytest tests -q
```

### Ledger state

{ledger_block}

### Not yet claimed

No benchmark result is recorded for this project. Anything asserted about
performance must come from a real run written to the ledger and must cite a
statement ID from `BENCHMARKS/ground_truth.json`.
