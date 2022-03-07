import json
import logging
import os

import boto3
import botocore.exceptions

from insightconnect_plugin_runtime import Action
from komand_dynamodb.connection import Connection
from komand_dynamodb.connection.schema import Input
from komand_dynamodb.util.constants import SERVICE_NAME, DEFAULT_REGION


class Util:
    @staticmethod
    def default_connection(action: Action) -> Action:
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        default_connection.connect(
            {
                Input.ACCESS_KEY: {"secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"},
                Input.SECRET_KEY: {"secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"},
                Input.REGION: "us-east-1",
            }
        )
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def load_json(filename):
        with open((os.path.join(os.path.dirname(os.path.realpath(__file__)), filename))) as file:
            return json.loads(file.read())

    @staticmethod
    def mocked_request(*args, **kwargs):
        if args[0] == "Scan" and args[1].get("TableName") == "test_table_for_scan":
            return Util.load_json("payloads/action_scan.json.resp")
        elif args[0] == "PutItem" and args[1].get("TableName") == "test_table_for_insert":
            if "wrong_key" in args[1].get("Item"):
                raise botocore.exceptions.ClientError(
                    Util.load_json("payloads/action_bad_insert_resource_not_found.resp"), "PutItem"
                )
            else:
                return Util.load_json("payloads/action_insert.json.resp")
        elif args[0] == "UpdateItem" and args[1].get("TableName") == "test_table_for_update":
            if "wrong_key" in args[1].get("Key"):
                raise botocore.exceptions.ClientError(
                    Util.load_json("payloads/action_bad_update_validation_exception.resp"), "UpdateItem"
                )
            else:
                return Util.load_json("payloads/action_update.json.resp")

    @staticmethod
    def mock_request_exception_handling(*args, **kwargs):
        if args[0] == "Scan" and args[1].get("TableName") == "wrong_table_name":
            raise boto3.client(SERVICE_NAME, region_name=DEFAULT_REGION).exceptions.ResourceNotFoundException(
                Util.load_json("payloads/wrong_table_name.json.resp"), "Scan"
            )
        elif args[0] == "Scan" and args[1].get("TableName") == "wrong_credentials":
            raise botocore.exceptions.ClientError(Util.load_json("payloads/wrong_credentials.json.resp"), "Scan")
        elif args[0] == "Scan" and args[1].get("TableName") == "endpoint_connection_error":
            raise botocore.exceptions.EndpointConnectionError(endpoint_url="test")
        elif args[0] == "Scan" and args[1].get("TableName") == "param_validation_error":
            raise botocore.exceptions.ParamValidationError(report="test")
        elif args[0] == "Scan" and args[1].get("TableName") == "unexpected_error":
            raise Exception()
