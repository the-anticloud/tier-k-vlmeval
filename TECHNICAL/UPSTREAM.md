# Vendored Upstream

{GENERATED}
## {name}

| Field | Value |
|---|---|
| Domain | {domain} |
| Role | {role} |
| Upstream | <{url}> |
| Commit | `{commit}` |
| Commit date | {commit_date} |
| Licence | {licence} ({licence_class}) |
| Licence file | {licence_file} |
| Size on disk | {size} MB |
| Verified | {updated} |

## Provenance

`UPSTREAM/` is a shallow clone (`--depth 1 --single-branch`) of the repository
above. The commit recorded here is the exact `HEAD` that was fetched; the
clone is never re-fetched, so this record stays true for the copy on disk.

To confirm the vendored copy still matches the record:

```
git -C UPSTREAM rev-parse HEAD
```

## Licensing position

The vendored upstream keeps **its own licence** ({licence}). Anticommons
0.1.0 covers only our `src/` code and is *not* applied to `UPSTREAM/`. No
upstream file is edited. See `NOTICE.md` for the attribution and notice of
changes, and `LICENSE.md` for the Anticommons text.
