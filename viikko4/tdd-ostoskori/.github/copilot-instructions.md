# Copilot instructions

## Project commands

- Use Python 3.14 or newer; the repository pins the development interpreter to
  3.14 in `.python-version`.
- Install the project and development dependencies with `uv sync`.
- Run the full test suite from the repository root with `uv run pytest`.
- Run one test with
  `uv run pytest src/tests/ostoskori_test.py::TestOstoskori::test_ostoskorin_hinta_ja_tavaroiden_maara_alussa`.
- There are no configured build or lint commands in `pyproject.toml`.

## Architecture

This is a small Finnish-language shopping-cart domain model:

- `src/tuote.py` defines `Tuote`, a product with a name and unit price.
- `src/ostos.py` defines `Ostos`, a cart line that wraps a `Tuote`, tracks its
  quantity, and calculates the line total.
- `src/ostoskori.py` defines `Ostoskori`, the aggregate that owns cart lines
  and exposes cart quantity, total price, add/remove, empty, and listing
  operations. Its implementation is the primary TDD exercise.
- `src/tests/ostoskori_test.py` contains `unittest.TestCase` tests executed by
  pytest. The flat imports (`from tuote import Tuote`, `from ostoskori import
  Ostoskori`) assume the existing source/test layout and should be preserved.

## Repository-specific conventions

- Keep public names and domain terminology in Finnish, matching the existing
  API (`lisaa_tuote`, `poista_tuote`, `tyhjenna`, `ostokset`, etc.).
- Implement the smallest behavior needed by the tests. Preserve the existing
  public method signatures and use `Ostos` for quantity and line-price
  behavior rather than duplicating that logic in `Ostoskori`.
- Do not change `src/ostos.py` or `src/tuote.py`.
- Do not edit tests unless the user explicitly asks for test changes.
- Add or change production behavior in `src/ostoskori.py`; avoid unrelated
  refactors and dependency changes.
