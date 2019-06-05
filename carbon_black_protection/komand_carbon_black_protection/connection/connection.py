import komand
from .schema import ConnectionSchema
# Custom imports below
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.session = None
        self.host = ""

    def connect(self, params):
        token = params.get('api_key').get('secretKey')
        self.logger.info("Connect: Connecting...")
        self.host = params.get("url")

        self.session = requests.Session()
        self.verify = params.get("ssl_verify")
        self.session.headers.update({
            'x-auth-token': token,
            'content-type': "application/json",
        })