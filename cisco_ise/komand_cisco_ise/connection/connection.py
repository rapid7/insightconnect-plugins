import komand
from .schema import ConnectionSchema
# Custom imports below
from komand_cisco_ise.util import util


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        username = params['credentials']['username']
        password = params['credentials']['password']
        address = params['address']
        ssl_verify = params['ssl_verify']

        self.ers = util.ERS(address, username, password, ssl_verify)
