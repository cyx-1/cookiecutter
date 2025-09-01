# About this project
- this project uses [uv](https://gist.github.com/cyx-1/6a2055ef453ca1bd54f8fd125fd19e6b) extensively to manage tools, libraries, and python version
- the following tools should be already installed via ```uv tool install``` with versions greater or equal to:
    - [pre-commit v4.3.0](https://gist.github.com/cyx-1/938dd1793b4da06012cf143587b5dd27)
    - [cookiecutter v2.6.0](https://gist.github.com/cyx-1/1f54b5b273db41f62850b58d7cf11964)
    - [ruff v0.12.11](https://gist.github.com/cyx-1/b24a878c2876ce6ba4c4ff0f8ab1e22f)
- python should be already installed via ```uv python install 3.10, 3.11, 3.12, 3.13```
- this project's [pre-commit](https://gist.github.com/cyx-1/938dd1793b4da06012cf143587b5dd27) uses: ruff, json, yaml, trailing-white-spaces
    - pre-commit has pre and post hook logic to validate and activate git, uv, pre-commit and so on
- this project uses python version: {{ cookiecutter.python_version }}

# Useful command
- To run pre-commit explicitly: ```pre-commit run --all-files```
- To run ruff explicitly: ```uv run ruff check``` and ```uv run ruff format```
- To use uv to add library dependencies: ```uv add <pkg>```
- To run pytest and watch folder for changes: ```uv run pytest -f```
- To update project version, modify ```__init__.py```
- To update pre-commit packages: ```pre-commit autoupdate```
- To switch to a different python version, update ```.python-version``` then run ```uv run python --version```

# TODO
- add ability to turn into a package and deal with version information via setup.cfg