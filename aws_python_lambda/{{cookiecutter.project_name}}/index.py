import json


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps("helloworld!"),
        "headers": {"Content-Type": "application/json"},
    }
