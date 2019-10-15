import komand
from .schema import ConnectionSchema
# Custom imports below
import boto.ec2


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")
        access_key_id = params.get("access_key").get("secretKey")
        secret_access_key = params.get("secret_key").get("secretKey")
        self.aws = boto.connect_ec2(aws_access_key_id=access_key_id , aws_secret_access_key=secret_access_key)
