import insightconnect_plugin_runtime

from .schema import ConnectionSchema, Input

# Custom imports below
import botocore.session
from icon_aws_ec2.util.common import ActionHelper


class Connection(insightconnect_plugin_runtime.Connection):
    client = None
    helper = ActionHelper()

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        session = botocore.session.Session()
        self.client = session.create_client(
            "ec2",
            aws_access_key_id=params.get(Input.AWS_ACCESS_KEY_ID).get("secretKey"),
            aws_secret_access_key=params.get(Input.AWS_SECRET_ACCESS_KEY).get("secretKey"),
            region_name=params.get(Input.REGION),
        )
        self.logger.info("Client connection object created...")
