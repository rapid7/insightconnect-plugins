import komand
from komand.exceptions import ConnectionTestException

from .schema import ConnectionSchema

# Custom imports below
import boto3


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connecting")

        region = params.get('region', None)
        kwargs = {
            'aws_access_key_id': params.get('aws_access_key_id').get('secretKey'),
            'aws_secret_access_key': params.get('aws_secret_access_key').get('secretKey'),
        }
        if region:
            kwargs['region_name'] = region

        self.aws = boto3.Session(**kwargs)

    def test(self):
        try:
            self.aws.client('workspaces').describe_workspaces()
        except:
            raise ConnectionTestException(cause="AWS Connection was not successful.",
                                          assistance="Please check your API key.")

        return {'connection': 'successful'}
