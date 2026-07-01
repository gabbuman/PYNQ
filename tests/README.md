# Tests

Tests are split by whether they need a real board.

- **`host/`** — run on any machine, no hardware. The board is replaced by the mocks in
  `host/mock_devices.py` and `host/mock_ip.py`. These are the tests CI runs.
- **`board/`** — run only on a PYNQ board. They load real overlays, touch real registers, and
  need `root`. They skip automatically when no board is detected, so the same `pytest` command
  is safe to run anywhere.

## Running

```bash
pytest            # any machine: runs host tests, skips board tests
```

On a board the same command runs everything, because the board tests detect the hardware and
no longer skip.

## Adding a test

- Needs no hardware → put it in `host/`.
- Needs a board → put it in `board/` and take the `board` fixture, which skips the test when
  no board is present:

```python
def test_reads_a_register(board):
    ...
```

The `board` fixture lives in `board/conftest.py`. It detects a board via the FPGA/PL device
nodes and can be forced on with `PYNQ_BOARD=1`.

## Legacy board tests

Older on-board tests still live under `pynq/tests/` and `pynq/lib/**/tests/`. They are being
migrated into `board/` and updated to use the `board` skip fixture. New board tests go straight
into `board/`.
