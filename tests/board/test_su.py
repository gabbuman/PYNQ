# Copyright (C) 2026 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: BSD-3-Clause

"""Precondition for the on-board suite: it must run with root privileges."""

import os


def test_superuser(board):
    """On-board tests need root to reach the hardware device nodes."""
    assert os.geteuid() == 0, "on-board tests must be run as root"
