import komand
from .schema import ConnectionSchema
# Custom imports below
from komand.exceptions import ConnectionTestException
from komand_red_canary.util.api import RedCanary3
import logging


# suppress request logging
logging.getLogger("requests").setLevel(logging.WARNING)


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_token = None
        self.customer_id = None
        self.api = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        api_token = params['api_token'].get("secretKey")
        customer_id = params['customer_id']
        if not customer_id:
            raise ConnectionTestException(cause="Missing customer ID from Connection. This is a required field.",
                                          assistance="The customer ID can be obtained from your Red Canary account URL e.g. https://<customer_id>.my.redcanary.co.")

        if not api_token:
            raise ConnectionTestException(cause="Missing API key from Connection. This is a required field.",
                                          assistance="The API authentication token can be obtained from your Red Canary account at https://<customer_id>.my.redcanary.co/users/edit.")

        self.api = RedCanary3(api_token, customer_id, self.logger)
        self.customer_id = customer_id

        self.logger.info("Connect: Connection successful")

    def test(self):
        self.api.test_call()
        return {'detection': {}}
