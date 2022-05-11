# Custom imports below
import botocore
import botocore.exceptions

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from komand_dynamodb.connection.schema import Input
from komand_dynamodb.util.constants import SERVICE_NAME
from .schema import ConnectionSchema
from ..util.api import AWSCommunicationAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting to AWS...")
        self.client = AWSCommunicationAPI(
            service_name=SERVICE_NAME,
            aws_access_key_id=params.get(Input.ACCESS_KEY).get("secretKey"),
            aws_secret_access_key=params.get(Input.SECRET_KEY).get("secretKey"),
            region_name=params.get(Input.REGION),
            logger=self.logger,
        )
        self.logger.info("Connect: Connected!")

    def test(self):
        try:
            response = self.client.test_connection()
            if response.get("ResponseMetadata").get("HTTPStatusCode") == 200:
                return {"Connection": "Connection successfully established with the AWS"}
        except botocore.exceptions.ClientError as error:
            raise ConnectionTestException(
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
