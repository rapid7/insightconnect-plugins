import komand
from .schema import ConnectionSchema
# Custom imports below
import zenpy


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params):
        creds = {
            'email': params.get('credentials').get('username'),
            'subdomain': params.get('subdomain')
        }

        if params.get('credentials').get('password'):
            creds['password'] = params.get('credentials').get('password')
        elif params.get('api_key').get('secretKey'):
            creds['token'] = params.get('api_key').get('secretKey')
        else:
            raise Exception('Error: Must define either password or API key!')

        self.client = zenpy.Zenpy(**creds)
        self.logger.info('Connect: Connecting...')
