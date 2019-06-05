import komand
from .schema import ConnectionSchema
# Custom imports below
from .. import mcafee


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        try:
            self.logger.info("Connect: Connecting..")
            self.client = mcafee.client(params['url'], params['port'], params.get('credentials').get('username'), params.get('credentials').get('password'))
            if self.client is not None:
                self.logger.info("Connected")
        except Exception:
            self.logger.error("Error connecting to Mcafee EPO")
            raise
