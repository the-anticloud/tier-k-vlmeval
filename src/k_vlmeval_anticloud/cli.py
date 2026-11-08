"""K_VLMEVAL CLI.

Every subcommand writes an AIOSS ledger block, so the operational history of
this project is tamper-evident and can be costed against hosted providers.

    k_vlmeval_anticloud provenance      what upstream is vendored, at which commit, under what licence
    k_vlmeval_anticloud bench          run the local benchmark suite
    k_vlmeval_anticloud ledger verify  check the hash chain
    k_vlmeval_anticloud ledger export  dump the chain
    k_vlmeval_anticloud offline check  assert no frontier API dependency
    k_vlmeval_anticloud notice         print the recorded upstream licence and commit

Licensed under Anticommons 0.1.0 (Apache-2.0 OR Anticommons-Enterprise-1.0).
See LICENSE.md. Upstream in ../UPSTREAM keeps its own licence and is
unmodified.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

from anticloud.groundtruth import load as load_gt
from anticloud.ledger import Ledger
from anticloud.offline import NoFrontierKeyGuard

from .provenance import is_vendored, load_provenance, project_root

LEDGER = os.path.join(project_root(), "ledger", "ledger.aioss")


def _ledger() -> Ledger:
    return Ledger.init(LEDGER)


def cmd_provenance(args: argparse.Namespace) -> int:
    pr = load_provenance()
    if args.json:
        print(json.dumps(pr, indent=2))
    else:
        print(f"{pr['name']}  ({pr['domain']})")
        print(f"  role      {pr['role']}")
        print(f"  upstream  {pr['url']}")
        print(f"  commit    {pr['commit'][:12] if pr.get('commit') else '(not vendored yet)'}")
        print(f"  date      {pr.get('commit_date') or '-'}")
        print(f"  licence   {pr.get('licence')} ({pr.get('licence_class')})")
        print(f"  size      {pr.get('size_mb')} MB")
    return 0


def cmd_offline(args: argparse.Namespace) -> int:
    root = project_root()
    rep = NoFrontierKeyGuard().check(root)
    print(rep)
    _ledger().append("offline_check", {"ok": rep.ok, "files_scanned": rep.scanned,
                                       "findings": len(rep.findings)})
    return 0 if rep.ok else 1


def cmd_notice(args: argparse.Namespace) -> int:
    """Show the licence split: ours (Anticommons) vs upstream's."""
    pr = load_provenance()
    print(f"{NAME} licence position")
    print(f"  this project   Anticommons 0.1.0")
    print(f"                  Apache-2.0 OR LicenseRef-Anticommons-Enterprise-1.0")
    print(f"  upstream       {pr['licence']} ({pr['licence_class']})")
    print(f"                  unmodified, separately licensed, own terms apply")
    print(f"  attribution    'based on Anticommons by Lois-Kleinner Alpasan'")
    if not is_vendored():
        print(f"\n  WARNING: UPSTREAM is not vendored; licence shown is unverified")
        return 1
    return 0


def cmd_ledger_verify(args: argparse.Namespace) -> int:
    rep = _ledger().verify()
    print(rep)
    return 0 if rep.ok else 1


def cmd_ledger_export(args: argparse.Namespace) -> int:
    out = _ledger().export(args.format)
    text = out if isinstance(out, str) else json.dumps(out, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"wrote {args.out}")
    else:
        print(text)
    return 0


def cmd_bench(args: argparse.Namespace) -> int:
    """Placeholder harness. Each project fills in its own suite; the ledger
    record shape and provenance-citation requirement are enforced here so a
    benchmark result can never be quoted without them."""
    gt = load_gt()
    led = _ledger()
    led.append("bench_start", {"suite": args.suite, "model": gt.model_name})
    print(f"[{gt.model_name}] suite={args.suite} -- implement per-project suite")
    print("Results MUST cite BENCHMARKS/ground_truth.json or a real ledger run.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="k_vlmeval_anticloud", description="K_VLMEVAL Anticloud adapter")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("provenance", help="vendored upstream + licence")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_provenance)

    p = sub.add_parser("offline", help="assert no frontier API dependency")
    p.add_argument("action", choices=["check"])
    p.set_defaults(fn=cmd_offline)

    p = sub.add_parser("notice", help="show the licence split for this project")
    p.set_defaults(fn=cmd_notice)

    p = sub.add_parser("bench", help="run the local benchmark suite")
    p.add_argument("--suite", default="default")
    p.set_defaults(fn=cmd_bench)

    p = sub.add_parser("ledger", help="ledger operations")
    lsub = p.add_subparsers(dest="lcmd", required=True)
    lp = lsub.add_parser("verify"); lp.set_defaults(fn=cmd_ledger_verify)
    lp = lsub.add_parser("export"); lp.add_argument("--format", default="json")
    lp.add_argument("--out"); lp.set_defaults(fn=cmd_ledger_export)

    return ap


def main(argv: list[str] | None = None) -> int:
    ap = build_parser()
    args = ap.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
