"""Contract tests. These must pass in every Anticloud project.

They assert the three cross-cutting guarantees rather than anything
project-specific, so a scaffolded project is correct before it has content.
"""

import os
import subprocess
import sys

from k_vlmeval_anticloud.provenance import is_vendored, load_provenance, upstream_dir


def test_provenance_readable():
    pr = load_provenance()
    assert pr["name"]
    assert pr["url"].startswith("https://")


def test_upstream_present():
    assert is_vendored(), "UPSTREAM/.git missing; run anticloud.vendor"


def test_licence_recorded():
    pr = load_provenance()
    assert pr["licence"] != "not vendored", "licence never detected at vendor time"


def test_ledger_roundtrip(tmp_path):
    from anticloud.ledger import Ledger
    led = Ledger.init(str(tmp_path / "t.aioss"))
    led.append("t", {"a": 1})
    assert led.verify().ok


def test_no_frontier_keys():
    from anticloud.offline import NoFrontierKeyGuard
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    rep = NoFrontierKeyGuard().scan_tree(root)
    assert rep.ok, str(rep)


def test_cli_help_runs():
    # Pass the source root explicitly. pytest's `pythonpath` setting only
    # affects the in-process interpreter; a child process does not inherit it,
    # so without this the test would fail unless the package was installed.
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env = dict(os.environ)
    src = os.path.join(root, "src")
    env["PYTHONPATH"] = src + (os.pathsep + env["PYTHONPATH"]
                               if env.get("PYTHONPATH") else "")
    r = subprocess.run(
        [sys.executable, "-m", "k_vlmeval_anticloud", "--help"],
        capture_output=True, text=True, env=env, cwd=root,
    )
    assert r.returncode == 0, r.stderr
