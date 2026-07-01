# Board tests

This directory is the intended single home for **on-board tests** — tests that
require a real PYNQ board (they load actual overlays/bitstreams, need `root`, and
some prompt the user). They are distinct from the host tests in `tests/host/`,
which run without hardware in CI using mocks.

## Status

This PR establishes the `tests/host` and `tests/board` split and moves the existing
host suite into `tests/host/`. The board tests themselves are **intentionally left
in place for now** and have not been moved, because relocating them affects
packaging and on-device behavior (see the open question below).

The existing on-board tests currently live at:

- `pynq/tests/test_pl.py`, `pynq/tests/test_su.py`
- `pynq/lib/tests/` (audio, button, led, rgbled, switch, video)
- `pynq/lib/arduino/tests/`
- `pynq/lib/logictools/tests/`
- `pynq/lib/pmod/tests/`

The shared interactive helper `pynq/tests/util.py` is imported by many of these
(`from pynq.tests.util import ...`).

## Open question for maintainers

Before migrating the board tests here, one decision drives everything:

**Do the on-board tests still need to ship to end-user boards?**
They are currently installed onto the device via `setup.py` package data.

- If **yes**, they should remain inside the `pynq/` package (shipped), and this
  `tests/board/` directory would hold only host-side board-test tooling/markers.
- If **no** (developer-only), they can be moved here under `tests/board/` and
  dropped from packaging — cleaner, but it removes the ability for users to
  self-test an installed board.

Happy to follow up with whichever direction is preferred. Guidance welcome.
