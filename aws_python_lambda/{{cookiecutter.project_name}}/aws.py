import os
import zipfile
import subprocess

import boto3  # type: ignore
import time
import sys
import json

LAMBDA_FUNCTION_NAME = "{{ cookiecutter.lambda_function_name }}"
TEMPLATE_FILE = "template.yaml"
S3_BUCKET = 'cyx-lambda-binary'
S3_KEY = f'{LAMBDA_FUNCTION_NAME}.zip'
ZIP_NAME = "lambda_package.zip"
region = "us-east-1"


def delete_file(filename: str):
    try:
        os.remove(filename)
    except FileNotFoundError:
        print(f"{filename} not found, nothing to delete.")


def delete_s3_object():
    s3 = boto3.client("s3")
    try:
        s3.delete_object(Bucket=S3_BUCKET, Key=S3_KEY)
    except Exception as e:
        print(f"Error deleting S3 object: {e}")


def zip_lambda():
    with zipfile.ZipFile(ZIP_NAME, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write("index.py")
        # Add dependencies from uv venv if needed
        site_packages = os.path.join(".venv", "Lib", "site-packages")
        if os.path.exists(site_packages):
            for root, _, files in os.walk(site_packages):
                for file in files:
                    full_path = os.path.join(root, file)
                    arcname = os.path.relpath(full_path, site_packages)
                    zf.write(full_path, arcname)


def upload_to_s3():
    s3 = boto3.client("s3")
    s3.upload_file(ZIP_NAME, S3_BUCKET, S3_KEY)


def update_lambda_code() -> None:
    subprocess.run(
        [
            "aws",
            "lambda",
            "update-function-code",
            "--function-name",
            LAMBDA_FUNCTION_NAME,
            "--s3-bucket",
            S3_BUCKET,
            "--s3-key",
            S3_KEY,
            "--region",
            region,
        ],
        check=True,
        stderr=subprocess.STDOUT,
        stdout=subprocess.DEVNULL,
    )


def wait_for_lambda_update(timeout: int = 60) -> None:
    """Wait until Lambda LastUpdateStatus is 'Successful' or timeout (seconds)."""

    start = time.time()
    while True:
        result = subprocess.run(
            [
                "aws",
                "lambda",
                "get-function-configuration",
                "--function-name",
                LAMBDA_FUNCTION_NAME,
                "--region",
                region,
            ],
            capture_output=True,
            text=True,
        )
        try:
            conf = json.loads(result.stdout)
            status = conf.get("LastUpdateStatus")
            if status == "Successful":
                break
            elif status == "Failed":
                raise RuntimeError("Lambda update failed!")
        except Exception as e:
            print(f"Error checking update status: {e}")
        if time.time() - start > timeout:
            raise TimeoutError("Timed out waiting for Lambda update to complete.")
        time.sleep(1)


def update_lambda():
    start = time.time()
    zip_lambda()
    print(f"Zipped project file into {ZIP_NAME} in {time.time() - start:.2f} seconds")

    start = time.time()
    upload_to_s3()
    print(f"Uploaded {ZIP_NAME} to s3://{S3_BUCKET}/{S3_KEY} in {time.time() - start:.2f} seconds")

    delete_file(ZIP_NAME)

    start = time.time()
    update_lambda_code()
    print(f"Updated Lambda function code in {time.time() - start:.2f} seconds")

    start = time.time()
    wait_for_lambda_update()
    print(f"Waited for Lambda update in {time.time() - start:.2f} seconds")

    start = time.time()
    invoke_lambda()
    print(f"Invoked Lambda function in {time.time() - start:.2f} seconds")


def invoke_lambda() -> None:
    start = time.time()
    output_file = "out.json"
    subprocess.run(
        [
            "aws",
            "lambda",
            "invoke",
            "--function-name",
            LAMBDA_FUNCTION_NAME,
            output_file,
            "--region",
            region,
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    print(f"Invoked Lambda function in {time.time() - start:.2f} seconds")
    with open(output_file, "r") as f:
        print(f.read())

    delete_file(output_file)


def delete_lambda():
    start = time.time()
    delete_s3_object()
    print(f"Deleted S3 object s3://{S3_BUCKET}/{S3_KEY} in {time.time() - start:.2f} seconds")

    start = time.time()
    subprocess.run(
        ["aws", "cloudformation", "delete-stack", "--stack-name", LAMBDA_FUNCTION_NAME, "--region", region],
        check=True,
    )
    print(f"Deleted Lambda function in {time.time() - start:.2f} seconds")

    start = time.time()
    while True:
        result = subprocess.run(
            ["aws", "cloudformation", "describe-stacks", "--stack-name", LAMBDA_FUNCTION_NAME, "--region", region],
            capture_output=True,
            text=True,
        )
        if "does not exist" in result.stderr:
            break
        time.sleep(5)
    print(f"Stack deleted.  Waited for deletion in {time.time() - start:.2f} seconds")


def deploy_lambda():
    start = time.time()
    delete_lambda()
    print(f"Deleted previous Lambda function in {time.time() - start:.2f} seconds")

    start = time.time()
    zip_lambda()
    print(f"Zipped project file into {ZIP_NAME} in {time.time() - start:.2f} seconds")

    start = time.time()
    upload_to_s3()
    print(f"Uploaded {ZIP_NAME} to s3://{S3_BUCKET}/{S3_KEY} in {time.time() - start:.2f} seconds")

    delete_file(ZIP_NAME)
    start = time.time()
    subprocess.run(
        [
            "aws",
            "cloudformation",
            "deploy",
            "--stack-name",
            LAMBDA_FUNCTION_NAME,
            "--template-file",
            TEMPLATE_FILE,
            "--parameter-overrides",
            f"LambdaS3Bucket={S3_BUCKET}",
            f"LambdaS3Key={S3_KEY}",
            f"LambdaFunctionName={LAMBDA_FUNCTION_NAME}",
            "--capabilities",
            "CAPABILITY_NAMED_IAM",
            "--region",
            region,
        ],
        check=True,
    )
    print(f"Deployed Lambda function in {time.time() - start:.2f} seconds")

    start = time.time()
    wait_for_lambda_update()
    print(f"Waited for Lambda update in {time.time() - start:.2f} seconds")

    start = time.time()
    invoke_lambda()
    print(f"Invoked Lambda function in {time.time() - start:.2f} seconds")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: uv run aws.py [update, invoke, delete, deploy]")
        print("uv run aws.py update -> to quickly update the Lambda function by zipping and uploading the code to S3")
        print("uv run aws.py invoke -> to invoke the Lambda function")
        print("uv run aws.py delete -> to delete the entire stack and associated resources")
        print("uv run aws.py deploy -> to completely delete and deploy the entire stack from scratch")
        sys.exit(1)
    if sys.argv[1] == "update":
        start = time.time()
        update_lambda()
        print(f"Total time taken for update: {time.time() - start:.2f} seconds")
    elif sys.argv[1] == "invoke":
        start = time.time()
        invoke_lambda()
        print(f"Total time taken for invoke: {time.time() - start:.2f} seconds")
    elif sys.argv[1] == "delete":
        start = time.time()
        delete_lambda()
        print(f"Total time taken for delete: {time.time() - start:.2f} seconds")
    elif sys.argv[1] == "deploy":
        start = time.time()
        deploy_lambda()
        print(f"Total time taken for deploy: {time.time() - start:.2f} seconds")
    else:
        print(f"Unknown command: {sys.argv[1]}")
        sys.exit(1)
