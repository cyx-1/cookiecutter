# About this project
- supports pre-commit installed via pipx so that quality checks run prior to commit
    - black, flake8, package sort, single-quotes, json, yaml, trailing-white-spaces
    - can add more here: https://pre-commit.com/hooks.html
- supports pytest so that unit test runs during development
- requires venv way of handling virtual environment
- supports a simple version numbering scheme
- follows pip-tools convention of generating requirements.txt
# Setup Information
- setup pre-commit to auto-improve on code quality
    - Assuming that pre-commit is installed via pipx
    - pre-commit install
- setup virtual environment with a folder called env
    - Run "python -m venv env"
- enter virtual environment
    - Run ". ./env/bin/activate" on Mac OS
    - Run ".\env\Scripts\activate" on Windows
- exit virtual environment
    - Run "deactivate" on Mac OS
    - Run ".\env\Scripts\deactivate" on Windows
- test driven development
    - Run "pytest -f" to watch any changes in this project
- useful reference information
    - Install packages using requirements.txt: "python -m pip install -r requirements.txt"
    - Uninstall all packages mentioned in requirements.txt: "python -m pip uninstall -r requirements.txt -y"
    - Don't use this
        - Freeze package version into requirements.txt: "python -m pip freeze > requirements.txt"
    - Use this instead
        - install pip-tools via pipx
        - run pip-compile in a folder that contains requirements.in
            - this would use the top-level packages mentioned in requirements.in to generate an annotated requirements.txt
    - Update pre-commit packages: pre-commit autoupdate
    - version kept at __init__.py

# TODO
- add ability to turn into a package and deal with version information via setup.cfg