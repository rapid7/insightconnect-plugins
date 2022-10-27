import insightconnect_plugin_runtime

from .schema import ConnectionSchema, Input

# Custom imports below
import botocore.session
import boto3
import uuid
from icon_aws_ec2.util.common import ActionHelper
from logging import Logger
from botocore.exceptions import ClientError

from insightconnect_plugin_runtime.exceptions import PluginException


class Connection(insightconnect_plugin_runtime.Connection):
    client = None
    helper = ActionHelper()
    logger: Logger

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def try_to_assume_role(self, params):
        if not params.get(Input.ROLE_ARN, ""):
            return

        session_name = str(uuid.uuid1())
        try:
            assumed_role_object = self.sts_client.assume_role(
                RoleArn=params.pop(Input.ROLE_ARN),
                RoleSessionName=session_name,
                ExternalId=params.pop(Input.EXTERNAL_ID),
            )
        except ClientError as error:
            raise PluginException(
                cause=f"Boto3 raised following error during assume role: {error.response['Error']['Code']}",
                assistance="Please verify your role ARN and external ID if it is necessary",
            )

        credentials = assumed_role_object["Credentials"]

        session = botocore.session.Session()
        self.client = session.create_client(
            "ec2",
            aws_access_key_id=credentials["AccessKeyId"],
            aws_secret_access_key=credentials["SecretAccessKey"],
            aws_session_token=credentials["SessionToken"],
            region_name=self.region,
        )

        self.logger.info(f"Session name: {session_name}")
        self.logger.info("Client connection object created...")

    def connect(self, params={}):
        self.region = params.get(Input.REGION)
        self.sts_client = boto3.client(
            "sts",
            aws_access_key_id=params.get(Input.AWS_ACCESS_KEY_ID).get("secretKey"),
            aws_secret_access_key=params.get(Input.AWS_SECRET_ACCESS_KEY).get("secretKey"),
        )

        session = botocore.session.Session()
        self.client = session.create_client(
            "ec2",
            aws_access_key_id=params.get(Input.AWS_ACCESS_KEY_ID).get("secretKey"),
            aws_secret_access_key=params.get(Input.AWS_SECRET_ACCESS_KEY).get("secretKey"),
            region_name=params.get(Input.REGION),
        )
        self.logger.info("Client connection object created...")
        self.try_to_assume_role(params)
