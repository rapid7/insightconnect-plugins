import komand
from .schema import ConnectionSchema
# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting..")
        self.conndict = {
            'headers': { "X-ApiKeys": "accessKey={}; secretKey={};".format(params['access_key']['secretKey'], params['secret_key']['secretKey']) },
            'url': params['hostname'],
            'verify': params['ssl_verify']
        }
