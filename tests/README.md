# Tests

Tests are split by whether they need a real board.

- **`host/`** — no hardware dependencies. The board is replaced by the mocks in
  `host/mock_devices.py` and `host/mock_ip.py`. CI tests.
- **`board/`** — hardware dependencies. Are skipped automatically when no board is detected.

## Running

```bash
pytest
```

On a board the same command runs all tests, because the board tests detect the hardware and
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

Older on-board tests still live under `pynq/tests/` and `pynq/lib/**/tests/`.