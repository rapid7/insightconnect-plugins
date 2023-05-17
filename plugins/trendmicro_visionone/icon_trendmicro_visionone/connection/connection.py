import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import (
    ConnectionTestException,
    PluginException,
)
from .schema import ConnectionSchema, Input

# Custom imports below
import pytmv1


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params: dict = None):
        """
        Connection config params are supplied as a dict in
        params or also accessible in self.parameters['key']

        The following will setup the var to be accessed
          self.blah = self.parameters['blah']
        in the action and trigger files as:
          blah = self.connection.blah
        """
        self.logger.info("Connect: Connecting...")

        url = params.get(Input.API_URL, "")
        if not url:
            raise PluginException(
                cause="No API URL provided.",
                assistance="API URL is a required parameter, please provide a valid API URL.",
                data=url,
            )
        key = params.get(Input.API_KEY).get("secretKey", "")
        if not key or "default" in key:
            raise PluginException(
                cause="No API Key provided.",
                assistance="API Key is a required parameter, please provide a valid API Key.",
                data=key,
            )
        app = params.get(Input.APP_NAME, "Rapid7-InsightConnect")

        self.server = url
        self.token_ = key
        self.app = app

    def test(self):
        # Get Action Parameters
        url = self.server
        key = self.token_
        app = self.app
        # Initialize PYTMV1 Client
        self.logger.info("Initializing PYTMV1 Client...")
        client = pytmv1.client(app, key, url)
        self.logger.info("Making API Call...")
        response = client.check_connectivity()
        if "error" in response.result_code.lower():
            raise ConnectionTestException(
                "Failed to Establish Connection...",
                assistance="Please check your API Key and URL",
                data=response.result_code,
            )
        else:
            self.logger.info("Connection Successfully Established...")
            return response.result_code
