import komand
from .schema import ConnectionSchema
# Custom imports below
import ssl
from metasploit.msfrpc import MsfRpcClient


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params):
        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError as e:
            self.logger.debug(e)
        else:
            ssl._create_default_https_context = _create_unverified_https_context
        self.logger.info("Connect: Connecting...")
        params = {unicode(k).encode("utf-8"): unicode(v).encode("utf-8") for k,v in params.iteritems()}
        self.client = MsfRpcClient(**params)
        self.logger.info("Client connection established")

