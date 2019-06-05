import komand
from .schema import ConnectionSchema
# Custom imports below
from komand.exceptions import ConnectionTestException
from komand_samanage.util.api import SamanageAPI


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        token = params.get('token')['secretKey']
        is_eu_customer = params.get('eu_customer')

        if not token:
            raise ConnectionTestException(cause="Missing API key from Connection. This is a required field.",
                                          assistance="The API authentication token can be obtained from your Samanage account.")

        self.logger.info("Connect: Connecting...")
        self.api = SamanageAPI(token, is_eu_customer, self.logger)

        self.logger.info("Connect: Connection successful")
