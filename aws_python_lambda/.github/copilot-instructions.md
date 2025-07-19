# Copilot Instructions for this Repository

## Python Environment
- Use [uv](https://github.com/astral-sh/uv) for dependency management and virtual environment creation. Do not use pip or venv directly.
- All Python code should be compatible with Python 3.11 or higher.

## Formatting and Linting
- Format all Python code with [black](https://black.readthedocs.io/en/stable/).
- Lint code with [flake8](https://flake8.pycqa.org/en/latest/). Fix all reported issues unless explicitly ignored in the config.
- Type-check code with [mypy](http://mypy-lang.org/). All code should pass mypy unless otherwise noted.

## General Guidelines
- Write clear, type-annotated Python code.
- Keep code style and quality consistent with black, flake8, and mypy.
- Use uv for all dependency and environment management tasks.

