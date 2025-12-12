
import json
import os
import uuid
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])


def lambda_handler(event, context):
    # Parse body
    try:
        body = json.loads(event.get("body") or "{}")
    except json.JSONDecodeError:
        return _response(400, {"message": "Invalid JSON in request body"})

    # Required field
    name = body.get("name")
    if not name:
        return _response(400, {"message": "Field 'name' is required"})

    # Generate or accept ID
    item_id = body.get("id") or str(uuid.uuid4())

    item = {
        "id": item_id,
        "name": name,
        "description": body.get("description", ""),
    }

    try:
        table.put_item(Item=item)
    except ClientError as e:
        return _response(
            500,
            {"message": "Failed to create item", "error": str(e)},
        )

    return _response(201, item)


def _response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps(body),
    }
