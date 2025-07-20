# {{ cookiecutter.project_name }}

- supports [pre-commit](https://gist.github.com/cyx-1/938dd1793b4da06012cf143587b5dd27) so that quality checks are part of commit routine
    - installed via [pipx](https://gist.github.com/cyx-1/33cee67d33e46873e35617abe5e0ad7f)
    - black, flake8, package sort, single-quotes, json, yaml, trailing-white-spaces
    - can add more here: https://pre-commit.com/hooks.html
- uses [uv](https://gist.github.com/cyx-1/6a2055ef453ca1bd54f8fd125fd19e6b) to manage project
- uses [AWS CLI](https://gist.github.com/cyx-1/d5231ea8270415f18d2319f08c27c3f5) to interact with AWS


## Setup
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
        black....................................................................Passed
        check for merge conflicts................................................Passed
        fix double quoted strings................................................Passed
        check json...........................................(no files to check)Skipped
        check yaml...............................................................Passed
        trim trailing whitespace.................................................Passed
        flake8...................................................................Passed
        seed isort known_third_party.............................................Passed
        isort....................................................................Passed
        ```
- use uv to set up virtual environment and retrieve library dependencies
    ```
    uv sync
    ```
- use aws.py to manage the lambda AWS resources
    ```
    uv run aws.py       
    Usage: uv run aws.py [update, invoke, delete-stack, deploy-stack]
    uv run aws.py update -> to update the Lambda function by zipping and uploading the code to S3
    uv run aws.py invoke -> to invoke the Lambda function
    uv run aws.py delete -> to delete the CloudFormation stack and associated resources
    uv run aws.py deploy -> to deploy the CloudFormation stack from scratch
    ```
    - Use deploy if starting the project for the first time
    - Use update if making incremental changes (not updating the entire CF stack, so it is much faster)
    - Creates a Cloudformation stack called: {{ cookiecutter.lambda_function_name }}
    - Creates a Lambda function called: {{ cookiecutter.lambda_function_name }}
