# About this project
- supports [pre-commit](https://gist.github.com/cyx-1/938dd1793b4da06012cf143587b5dd27) so that quality checks are part of commit routine
    - installed via [pipx](https://gist.github.com/cyx-1/33cee67d33e46873e35617abe5e0ad7f)
    - ruff, json, yaml, trailing-white-spaces
    - can add more here: https://pre-commit.com/hooks.html
- uses [uv](https://gist.github.com/cyx-1/6a2055ef453ca1bd54f8fd125fd19e6b) to manage project
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
    - next time prior to committing code via git, you will see the following checks
        ```
        ruff check...............................................................Passed
        ruff format..............................................................Passed
        check for merge conflicts................................................Passed
        check json...........................................(no files to check)Skipped
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