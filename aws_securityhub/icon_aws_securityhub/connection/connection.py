import komand
from .schema import ConnectionSchema, Input
# Custom imports below
import boto3


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.aws = None

    def connect(self, params):
        self.logger.info("Connecting")

        region = params.get('region', None)
        kwargs = {
            'aws_access_key_id': params.get(Input.AWS_ACCESS_KEY_ID).get('secretKey'),
            'aws_secret_access_key': params.get(Input.AWS_SECRET_ACCESS_KEY).get('secretKey'),
        }
        if region:
            kwargs['region_name'] = region
        self.aws = boto3.Session(**kwargs)

    def test(self):
        self.aws.client('securityhub')
        return {}
