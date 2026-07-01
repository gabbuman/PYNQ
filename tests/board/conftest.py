# Copyright (C) 2026 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: BSD-3-Clause

"""Shared setup for the on-board test suite.

Board tests need a real PYNQ board. The ``board`` fixture skips them when no
board is present, so the full suite stays runnable on a laptop and in CI.
"""

import os

import pytest


def board_present():
    """Return True only when running on a real PYNQ board.

    Detection uses the FPGA / programmable-logic device nodes that exist on a
    board but not on a development machine. Set ``PYNQ_BOARD=1`` to force it on.
    """
    if os.environ.get("PYNQ_BOARD") == "1":
        return True
    return os.path.exists("/dev/xlnk") or os.path.isdir("/sys/class/fpga_manager")


@pytest.fixture
def board():
    """Skip the requesting test unless it runs on a PYNQ board."""
    if not board_present():
        pytest.skip("requires a PYNQ board")
