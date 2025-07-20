# About this project
- supports pre-commit installed via pipx so that quality checks run prior to commit
    - black, flake8, package sort, single-quotes, json, yaml, trailing-white-spaces
    - can add more here: https://pre-commit.com/hooks.html
- uses uv to manage project
- supports pytest so that unit test runs during development
- supports a simple version numbering scheme

# Setup Information
- setup pre-commit to auto-improve on code quality
    - Assuming that pre-commit is installed via pipx
    - right after the project is connected to git, run the following command
        ```
        pre-commit install
        ```
- use uv to set up virtual environment and retrieve library dependencies
    ```
    uv sync
    ```
- use pytest to run tests right after making changes
    ```
    uv run pytest -f
    ```
- useful reference information
    - Update pre-commit packages: pre-commit autoupdate
    - version kept at __init__.py

# TODO
- add ability to turn into a package and deal with version information via setup.cfg