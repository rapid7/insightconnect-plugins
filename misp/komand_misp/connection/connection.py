import komand
from .schema import ConnectionSchema
# Custom imports below
import pymisp


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        url = params.get('url')
        key = params.get('automation_code').get('secretKey')
        ssl = params.get('ssl')
        try:
            self.client = pymisp.PyMISP(url, key, ssl, 'json', debug=False)
            self.logger.info("Connect: Connected!")
        except:
            self.logger.error("Connect: Not Connected")
            raise
