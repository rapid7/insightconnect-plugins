import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from komand_rest.util.util import RestAPI, TestRestAPI
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api = None
        self.authentication_type = None

    def connect(self, params={}):
        self.logger.info("Connect: Configuring REST details")
        base_url = params.get(Input.BASE_URL)
        default_headers = params.get(Input.DEFAULT_HEADERS, {})
        self.authentication_type = params.get(Input.AUTHENTICATION_TYPE)
        username = None
        password = None
        secret_key = None

        self.api = RestAPI(
            base_url,
            self.logger,
            params.get(Input.SSL_VERIFY, True),
            default_headers,
            params.get(Input.FAIL_ON_HTTP_ERRORS, True),
            params.get(Input.CLIENT_CERTIFICATE),
            params.get(Input.PRIVATE_KEY),
        )

        if self.authentication_type and self.authentication_type != "No Authentication":
            if self.authentication_type in ('Basic Auth', 'Digest Auth'):
                username = params.get(Input.BASIC_AUTH_CREDENTIALS).get("username")
                password = params.get(Input.BASIC_AUTH_CREDENTIALS).get("password")
            else:
                secret = params.get(Input.SECRET, None)
                if secret:
                    secret_key = secret.get("secretKey")

            self.api.with_credentials(self.authentication_type, username, password, secret_key)

        self.logger.info("Connect: Connecting..")

    def test(self):
        path = ""
        api = TestRestAPI(self.api)
        if self.authentication_type == "Rapid7 Insight":
            path = "/validate"
        elif self.authentication_type == "Pendo":
            path = "/api/v1/feature"
        elif self.authentication_type == "OpsGenie":
            path = "/v2/users"

        try:
            api.call_api("GET", path)
        except PluginException as e:
            raise ConnectionTestException(cause=e.cause, assistance=e.assistance, data=e.data)

        return {"success": True}
