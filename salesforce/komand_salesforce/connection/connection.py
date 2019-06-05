import komand
from .schema import ConnectionSchema
# Custom imports below
from komand_salesforce.util.api import SalesforceAPI


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting...")

        client_id = params.get('client_id')
        client_secret = params.get('client_secret').get('secretKey')
        username = params.get('salesforce_account_username_and_password').get(
            'username'
        )
        password = params.get('salesforce_account_username_and_password').get(
            'password'
        )
        security_token = params.get('security_token').get('secretKey')

        self.api = SalesforceAPI(
            client_id, client_secret, username,
            password, security_token, self.logger
        )

        self.logger.info("Connect: Connection successful")

    def test(self):
        # Since `connect` tests the API when creating a Salesforce instance, if we
        # got to this point, the API is working and the API key is correct
        return {}
