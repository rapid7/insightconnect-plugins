import komand
from .schema import ConnectionSchema
# Custom imports below
import boto3


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        self.logger.info("Connect: Connecting to AWS...")
        region = params.get("region")
        kwargs = {
            'aws_access_key_id': params.get('access_key').get('secretKey'),
            'aws_secret_access_key': params.get('secret_key').get('secretKey'),
        }
        if region:
            kwargs['region_name'] = region

        aws = boto3.Session(**kwargs)
        self.dynamodb = aws.resource('dynamodb')
        self.logger.info("Connect: Connected!")
