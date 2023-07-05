import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from komand_salesforce.util.api import SalesforceAPI
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")

        client_id = params.get(Input.CLIENTID)
        client_secret = params.get(Input.CLIENTSECRET).get("secretKey")
        username = params.get(Input.SALESFORCEACCOUNTUSERNAMEANDPASSWORD).get("username")
        password = params.get(Input.SALESFORCEACCOUNTUSERNAMEANDPASSWORD).get("password")
        security_token = params.get(Input.SECURITYTOKEN).get("secretKey")

        self.api = SalesforceAPI(client_id, client_secret, username, password, security_token, self.logger)
        self.logger.info("Connect: Connection successful")

    def test(self):
        try:
            self.api.simple_search("test")
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
