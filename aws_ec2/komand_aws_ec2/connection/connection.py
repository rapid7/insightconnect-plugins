import komand
from .schema import ConnectionSchema

# Custom imports below
import botocore.session
from komand_aws_ec2.util.common import ActionHelper


class Connection(komand.Connection):
    client = None
    helper = ActionHelper()

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        session = botocore.session.Session()
        self.client = session.create_client(
            "ec2",
            aws_access_key_id=params.get("aws_access_key_id").get("secretKey"),
            aws_secret_access_key=params.get("aws_secret_access_key").get("secretKey"),
            region_name=params.get("region"),
        )
        self.logger.info("Client connection object created...")
