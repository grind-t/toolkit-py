# grind-t-toolkit

Natural problem solver's toolkit.
Python port of [`@grind-t/toolkit`](https://github.com/grind-t/toolkit).

## Installation

```sh
uv add grind-t-toolkit
```

## Structure

Utilities are grouped into category subpackages, mirroring the subpath exports
of the TypeScript package:

```python
from toolkit.array import ...
from toolkit.string import ...
```

Tests live in `tests/<category>/test_<name>.py`. Tests that hit external
services are marked with `@pytest.mark.e2e`.

## Development

| Task | Command |
| --- | --- |
| Format | `uv run ruff format` |
| Lint | `uv run ruff check --fix` |
| Type check | `uv run ty check` |
| Unit tests | `uv run pytest -m "not e2e"` |
| E2E tests | `uv run pytest -m e2e` |
| All tests | `uv run pytest` |
| Build | `uv build` |
