import komand
from .schema import ConnectionSchema
# Custom imports below
from phabricator import Phabricator


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        hostname = params.get('url',None)
        token = params.get('token').get('secretKey')
        self.phab = None

        self.logger.info("Connect: Connecting..");

        if len(token) != 32:
            self.logger.error("Connection: Connect: Token must be 32 characters length")
            raise Exception("Connection: Connect: Token must be 32 characters length")

        if not hostname.endswith('/'):
            hostname = hostname + '/'

        try:
            self.phab = Phabricator(host=hostname, token=token)
        except ConfigurationError as e:
            self.logger.error("Connection: Connect: Configuration error({0}): {1}".format(e.errno, e.strerror))
            raise e
