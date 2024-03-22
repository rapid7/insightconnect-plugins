import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

# Custom imports below
from komand_cherwell.util.api import Cherwell


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self._base_url = None
        self.api = None

    def connect(self, params={}):

        base_uri = params.get(Input.URL)
        username, password = (
            params.get(Input.USERNAME_AND_PASSWORD, {}).get("username"),
            params.get(Input.USERNAME_AND_PASSWORD, {}).get("password"),
        )
        client_id = params.get(Input.CLIENT_ID, {}).get("secretKey")
        authentication_mode = params.get(Input.AUTHENTICATION_MODE)

        # Form the base URL for the Cherwell server
        scheme = "https://" if params.get(Input.SSL_VERIFY) else "http://"
        self._base_url = f"{scheme}{base_uri}"

        self.api = Cherwell(self._base_url, self.logger, username, password, client_id, authentication_mode)

    def test(self):
        try:
            self.api.get_serviceinfo()
            return {"success": True}
        except PluginException as exception:
            self.logger.error(f"An error occurred while testing Cherwell credentials: {exception}")
            raise ConnectionTestException()
