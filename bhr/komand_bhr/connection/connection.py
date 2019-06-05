import komand
from bhr_client.rest import login as bhr_client_login
from .schema import ConnectionSchema
# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        self.host   = params.get('token').get('domain')
        self.token  = params.get('token').get('token')
        self.verify = params.get('ssl_no_verify', True)
        self.client = bhr_client_login(self.host, token=self.token, ssl_no_verify=self.verify)
