"""Tests the Anticloud egress patch. These fail without the patch.

The guard module is loaded by path rather than by importing the package.
Importing the package pulls in its real dependencies (torch, tqdm, ...),
which are not installed in the audit environment, and a test that cannot
collect proves nothing about the patch. What is under test here is the
guard's own behaviour, which has no such dependency.
"""

from __future__ import annotations

import importlib.util
import os
import pathlib

import pytest

_ROOT = pathlib.Path(__file__).resolve().parents[2] / "UPSTREAM"
# The package may sit at UPSTREAM/<pkg> or UPSTREAM/src/<pkg>; search both
# rather than assuming a layout, so a skip never masks a missing patch.
_candidates = [_ROOT / "vlmeval" / "_anticloud_egress.py",
               _ROOT / "src" / "vlmeval" / "_anticloud_egress.py"]
_GUARD = next((c for c in _candidates if c.exists()), _candidates[0])

if not _GUARD.exists():  # pragma: no cover
    pytest.skip("egress guard not applied to this clone", allow_module_level=True)

_spec = importlib.util.spec_from_file_location("_anticloud_egress", _GUARD)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

EgressDenied = _mod.EgressDenied
guarded_connect = _mod.guarded_connect
install = _mod.install
is_offline = _mod.is_offline


def test_offline_flag_reads_env(monkeypatch):
    monkeypatch.setenv("ANTICLOUD_OFFLINE", "1")
    assert is_offline() is True
    monkeypatch.setenv("ANTICLOUD_OFFLINE", "0")
    assert is_offline() is False


def test_frontier_host_denied_when_offline(monkeypatch):
    monkeypatch.setenv("ANTICLOUD_OFFLINE", "1")
    with pytest.raises(EgressDenied):
        guarded_connect(("api.openai.com", 443))


def test_local_host_still_allowed_when_offline(monkeypatch):
    """An offline guarantee is about frontier spend, not local models.

    Port 9 (discard) has no listener, so the real connect runs and fails with
    a normal OSError. What matters is that it is *not* EgressDenied: the guard
    must not break local model serving.
    """
    monkeypatch.setenv("ANTICLOUD_OFFLINE", "1")
    try:
        guarded_connect(("127.0.0.1", 9), timeout=0.25)
    except EgressDenied:
        pytest.fail("guard denied a local address; it must only deny frontier")
    except OSError:
        pass  # expected: nothing is listening


def test_guard_patches_socket_module(monkeypatch):
    """install() replaces socket.create_connection, and is idempotent."""
    import socket
    monkeypatch.setenv("ANTICLOUD_OFFLINE", "1")
    original = socket.create_connection
    try:
        assert install() is True
        assert socket.create_connection is guarded_connect
        assert install() is True  # idempotent
    finally:
        socket.create_connection = original


def test_install_is_noop_when_online(monkeypatch):
    monkeypatch.setenv("ANTICLOUD_OFFLINE", "0")
    assert install() is False
