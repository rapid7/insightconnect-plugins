import functools
from logging import Logger

import boto3
import botocore.exceptions

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_dynamodb.util import constants
from komand_dynamodb.util.utils import Utils


def prepare_input_and_output(function):
    @functools.wraps(function)
    def wrapper(*args, input_schema: dict, params: dict) -> dict:
        params = Utils.prepare_input_for_aws_call(params, input_schema)
        return Utils.fix_output_types(function(*args, input_schema, params))

    return wrapper


class AWSCommunicationAPI:
    def __init__(
        self, service_name: str, aws_access_key_id: str, aws_secret_access_key: str, region_name: str, logger: Logger
    ):
        self.client = boto3.client(
            service_name=service_name,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name,
        )
        self.logger = logger
        self.aws_service = service_name

    @prepare_input_and_output
    def insert_data(self, input_schema: dict, params: dict) -> dict:  # pylint: disable=unused-argument
        self.logger.info("Insert data")
        return self._handle_rest_call(self._get_function_from_client(name=constants.INSERT_COMMAND), params)

    @prepare_input_and_output
    def update_data(self, input_schema: dict, params: dict) -> dict:  # pylint: disable=unused-argument
        self.logger.info("Update data")
        return self._handle_rest_call(self._get_function_from_client(name=constants.UPDATE_COMMAND), params)

    @prepare_input_and_output
    def scan_table(self, input_schema: dict, params: dict) -> dict:  # pylint: disable=unused-argument
        self.logger.info("Start scan")
        return self._handle_rest_call(self._get_function_from_client(name=constants.SCAN_COMMAND), params)

    def test_connection(self):
        return self.client.list_tables()

    def _get_function_from_client(self, name: str):
        try:
            client_function = getattr(self.client, name)
        except AttributeError:
            self.logger.error(f'Unable to find the command "{self.aws_service}" "{name}"')
            raise PluginException(
                cause=f"Unable to find the command {self.aws_service} {name}",
                assistance="Please see the plugin logs for more information.",
            )
        return client_function

    def _handle_rest_call(self, client_function, params: dict) -> dict:
        try:
            response = client_function(**params)
        except botocore.exceptions.EndpointConnectionError:
            raise PluginException(
                cause="Error occurred when invoking the aws-cli: Unable to reach the url endpoint.",
                assistance="Check the connection region is correct.",
            )
        except botocore.exceptions.ParamValidationError:
            raise PluginException(
                cause="Error occurred when invoking the aws-cli.",
                assistance="Check the input parameters they could be missing or incorrect and try again.",
            )
        except self.client.exceptions.ResourceNotFoundException as error:
            raise PluginException(
                cause="Requested resource not found.",
                assistance="Check the input parameters they could be missing or incorrect and try again. Especially table name and region.",
                data=error.response,
            )
        except botocore.exceptions.ClientError as error:
            raise PluginException(
                cause="Error occurred when invoking the aws-cli.",
                assistance="Check client connection keys and input arguments and try again.",
                data=error.response,
            )
        except Exception as error:
            raise PluginException(
                cause="Error occurred when invoking the aws-cli.",
                assistance="Please contact with developers because some unexpected appear.",
                data=error,
            )
        return response
