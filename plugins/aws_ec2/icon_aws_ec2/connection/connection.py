from logging import Logger

import botocore.session
import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.clients.aws_client import AWSAction, ActionHelper

from .schema import ConnectionSchema, Input


class Connection(insightconnect_plugin_runtime.Connection):
    client = None
    helper = ActionHelper()
    logger: Logger

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        service_name = "ec2"
        self.auth_params = {
            "aws_access_key_id": params.get(Input.AWS_ACCESS_KEY_ID).get("secretKey"),
            "aws_secret_access_key": params.get(Input.AWS_SECRET_ACCESS_KEY).get("secretKey"),
        }
        self.assume_role_params = {
            "region": params.get(Input.REGION, ""),
            "role_arn": params.get(Input.ROLE_ARN, ""),
            "external_id": params.get(Input.EXTERNAL_ID, ""),
        }

        session = botocore.session.Session()
        self.client = session.create_client(
            service_name, region_name=self.assume_role_params.get("region"), **self.auth_params
        )
        self.logger.info("Client connection object created...")

        if self.assume_role_params.get(Input.ROLE_ARN):
            self.client = AWSAction.try_to_assume_role(service_name, self.assume_role_params, self.auth_params)
