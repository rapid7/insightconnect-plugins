import komand
from .schema import ConnectionSchema
# Custom imports below
from tenable_io.client import TenableIOClient


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")
        self.client = TenableIOClient(access_key=params['access_key']['secretKey'], secret_key=params['secret_key']['secretKey'])
