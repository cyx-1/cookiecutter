# {{ cookiecutter.project_name }}

## Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) installed
- AWS CLI configured

## Setup

```

uv sync

uv run aws.py       
Usage: uv run aws.py [update, invoke, delete-stack, deploy-stack]
uv run aws.py update -> to update the Lambda function by zipping and uploading the code to S3
uv run aws.py invoke -> to invoke the Lambda function
uv run aws.py delete -> to delete the CloudFormation stack and associated resources
uv run aws.py deploy -> to deploy the CloudFormation stack from scratch
```
- Use deploy if starting the project for the first time
- Use update if making incremental changes
- Creates a Cloudformation stack called: {{ cookiecutter.lambda_function_name }}
- Creates a Lambda function called: {{ cookiecutter.lambda_function_name }}

## Update Lambda Code

```
uv run aws.py update
```

- Packages code and dependencies, uploads to S3, updates Lambda code, waits for update, and invokes the function.
- This is faster than deploying the entire cloud formation

## Invoke Lambda

```
uv run aws.py invoke
```

- Invokes the Lambda function and prints the output.

## Delete CloudFormation Stack

```
uv run aws.py delete
```

- Deletes the CloudFormation stack and waits for deletion.

## Deploy CloudFormation Stack

```
uv run aws.py deploy
```

- Deploys the CloudFormation stack from the template.


