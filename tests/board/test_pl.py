# Copyright (C) 2026 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: BSD-3-Clause

"""Programmable-logic / overlay tests. Board only.

The overlay is loaded inside a fixture (not at import time) so this module is
safe to collect on any machine; the ``board`` dependency skips it off-board.
"""

import pytest

from pynq import Overlay, PL


@pytest.fixture
def base_overlay(board):
    """Load the board's base overlay; skips off-board via ``board``."""
    overlay = Overlay(PL.bitfile_name)
    overlay.download()
    return overlay


def test_overlay_loads(base_overlay):
    assert base_overlay.is_loaded(), "base overlay should report as loaded"


def test_overlay_has_ip(base_overlay):
    assert len(base_overlay.ip_dict) > 0, "overlay has an empty IP dictionary"
    for ip, info in base_overlay.ip_dict.items():
        for key in ("addr_range", "phys_addr", "state", "type"):
            assert key in info, f"key {key} missing in IP {ip}"


def test_reset_clears_ip_state(base_overlay):
    for info in base_overlay.ip_dict.values():
        info["state"] = "TEST"
    base_overlay.reset()
    for info in base_overlay.ip_dict.values():
        assert info["state"] is None, "reset() should clear IP state"
