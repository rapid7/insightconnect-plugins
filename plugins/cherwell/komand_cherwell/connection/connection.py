import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

# Custom imports below
from komand_cherwell.util.api import Cherwell


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api = None

    def connect(self, params={}):

        base_uri = params.get(Input.URL)
        username, password = (
            params.get(Input.USERNAME_AND_PASSWORD, {}).get("username"),
            params.get(Input.USERNAME_AND_PASSWORD, {}).get("password"),
        )
        client_id = params.get(Input.CLIENT_ID, {}).get("secretKey")
        authentication_mode = params.get(Input.AUTHENTICATION_MODE)
        ssl_verify = params.get(Input.SSL_VERIFY)

        # Form the base URL for the Cherwell server
        if not (base_uri.startswith("http://") or base_uri.startswith("https://")):
            self.logger.info("No scheme found, defaulting to use HTTPS.")
            base_uri = f"https://{base_uri}"

        if base_uri.startswith("http://"):
            self.logger.info(
                "Using HTTP may result in server-side errors originating from mishandled parameters. If "
                "you encounter such errors, it is recommended to use HTTPS."
            )
        self.api = Cherwell(base_uri, self.logger, username, password, client_id, authentication_mode, ssl_verify)

    def test(self):
        try:
            self.api.get_serviceinfo()
            return {"success": True}
        except PluginException as exception:
            self.logger.error(f"An error occurred while testing Cherwell credentials: {exception}")
            raise ConnectionTestException()
