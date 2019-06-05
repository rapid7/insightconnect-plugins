import komand
from .schema import ConnectionSchema
# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")
        self.headers = {"Content-Type": "application/json"}
        self.url = params.get('url')
        data = {
            'email': params.get('email', None),
            'api_key': params.get('api_key').get('secretKey', None)
        }
        self.data = komand.helper.clean_dict(data)
