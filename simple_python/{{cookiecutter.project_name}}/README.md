# About this project
- this project uses [uv](https://gist.github.com/cyx-1/6a2055ef453ca1bd54f8fd125fd19e6b) extensively to manage tools, libraries, and python version
- the following tools should be already installed via ```uv tool install``` with versions greater or equal to:
    - pre-commit v4.3.0, cookiecutter v2.6.0, ruff v0.12.11
- python should be already installed via ```uv python install 3.10, 3.11, 3.12, 3.13```
- this project's [pre-commit](https://gist.github.com/cyx-1/938dd1793b4da06012cf143587b5dd27) uses: ruff, json, yaml, trailing-white-spaces
- this project uses python version: {{ cookiecutter.python_version }}
    - to use a different python version, change the version in .python-version and then verify via ```uv run python --version```
- supports pytest so that unit test runs during development
- supports a simple version numbering scheme

# Setup Information
- setup git
    - initialize git locally: ```git init```
    - attach the remote repository: ```git remote add origin git@github.com:user/repo.git```
    - create local branch: ```git branch -M main```
- setup pre-commit to maintain code quality prior to commiting code
    - Assuming that pre-commit is installed via pipx
    - right after the project is connected to git, run the following command
        ```
        pre-commit install

        output should say: pre-commit installed at .git\hooks\pre-commit
        ```
    - you will see the following checks next time:
        - prior to committing code via git
        - or after running this command ```pre-commit run --all-files```
        ```
        ruff check...............................................................Passed
        ruff format..............................................................Passed
        check for merge conflicts................................................Passed
        check json...............................................................Passed
        check yaml...............................................................Passed
        trim trailing whitespace.................................................Passed
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
    - version kept at ```__init__.py```

# TODO
- add ability to turn into a package and deal with version information via setup.cfg