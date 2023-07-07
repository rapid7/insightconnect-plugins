import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import (
    ConnectionTestException,
    PluginException,
)
from .schema import ConnectionSchema, Input

# Custom imports below

from icon_ipqualityscore.util.api import IPQSClient, URL_ENDPOINT


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_key = None
        self.ipqs_client = None

    def connect(self, params):
        """
        Connection config params are supplied as a dict in
        params or also accessible in self.parameters['key']

        The following will setup the var to be accessed
          self.blah = self.parameters['blah']
        in the action and trigger files as:
          blah = self.connection.blah
        """
        # TODO: Implement connection or 'pass' if no connection is necessary
        self.api_key = params.get("apiKey").get("secretKey")
        self.ipqs_client = IPQSClient(self.api_key, self.logger)
        self.logger.info("Connect: Connecting...")

    def test(self):
        try:
            additional_params = {"strictness": 0, "fast": False}
            ud_params = {"url": "www.ipqualityscore.com", "params": additional_params}
            self.ipqs_client.ipqs_lookup(URL_ENDPOINT, ud_params)
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
