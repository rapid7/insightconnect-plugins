import insightconnect_plugin_runtime
import requests.exceptions

from .schema import ConnectionSchema, Input
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import re
from ..util.api import CiscoUmbrellaEnforcementAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")

        key = params.get(Input.API_KEY).get("secretKey")
        ssl_verify = params.get(Input.SSL_VERIFY)

        self.client = CiscoUmbrellaEnforcementAPI(key, ssl_verify)

    def test_connection(self):
        try:
            self.client.get_domains()
            return {"success": True}
        except requests.exceptions.SSLError as error:
            raise PluginException(cause=error, assistance="Set SSL verify to False or provide a valid certificate.")
