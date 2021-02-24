import komand
from .schema import ConnectionSchema, Input
from komand_rest.util.util import Common
from komand.exceptions import PluginException, ConnectionTestException

# Custom imports below
from requests.auth import HTTPDigestAuth, HTTPBasicAuth


class Connection(komand.Connection):
    CUSTOM_SECRET_INPUT = "CUSTOM_SECRET_INPUT"

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_key = None
        self.ssl_verify = None
        self.base_url = None
        self.default_headers = None
        self.authentication_type = None
        self.auth = None

    def connect(self, params={}):
        self.logger.info("Connect: Configuring REST details")
        base_url = params.get(Input.BASE_URL)
        default_headers = params.get(Input.DEFAULT_HEADERS, {})
        self.authentication_type = params.get(Input.AUTHENTICATION_TYPE)
        username = None
        password = None
        secret_key = None

        if self.authentication_type:
            if self.authentication_type == "Basic Auth" or self.authentication_type == "Digest Auth":
                username = params.get(Input.BASIC_AUTH_CREDENTIALS).get("username")
                password = params.get(Input.BASIC_AUTH_CREDENTIALS).get("password")
                if not username or not password:
                    raise PluginException(
                        cause="Basic Auth authentication selected without providing username and password.",
                        assistance="The authentication type requires a username and password."
                        " Please complete the connection with a username and password or change the authentication type.",
                    )
            else:
                secret_key = params.get(Input.SECRET).get("secretKey")
                if not secret_key:
                    raise PluginException(
                        cause="An authentication type was selected that requires a secret key.",
                        assistance="Please complete the connection with a secret key or change the authentication type.",
                    )

            if self.authentication_type == "Basic Auth":
                self.auth = HTTPBasicAuth(username, password)
            elif self.authentication_type == "Digest Auth":
                self.auth = HTTPDigestAuth(username, password)
            elif self.authentication_type == "Bearer Token":
                default_headers = Common.merge_dicts(default_headers, {"Authorization": f"Bearer {secret_key}"})
            elif self.authentication_type == "Rapid7 Insight":
                default_headers = Common.merge_dicts(default_headers, {"X-Api-Key": secret_key})
            elif self.authentication_type == "OpsGenie":
                default_headers = Common.merge_dicts(default_headers, {"Authorization": f"GenieKey {secret_key}"})
            elif self.authentication_type == "Pendo":
                default_headers = Common.merge_dicts(
                    default_headers, {"content-type": "application/json", "x-pendo-integration-key": secret_key}
                )
            elif self.authentication_type == "Custom":
                new_headers = {}
                for key, value in default_headers.items():
                    if value == self.CUSTOM_SECRET_INPUT:
                        new_headers[key] = secret_key
                    else:
                        new_headers[key] = value
                default_headers = new_headers

        self.base_url = base_url
        self.default_headers = default_headers
        self.ssl_verify = params.get("ssl_verify")
        self.logger.info("Connect: Connecting..")

    def test(self):
        path = ""
        url = self.base_url
        if self.authentication_type == "Rapid7 Insight":
            path = "/validate"
        elif self.authentication_type == "Pendo":
            path = "/api/v1/feature"
            url = self.base_url.replace("/api", "").replace("/v1", "")
        elif self.authentication_type == "OpsGenie":
            path = "/v2/users"
            url = self.base_url.replace("/v2", "")

        try:
            Common.call_api(url.rstrip("/"), path, self.default_headers, self.ssl_verify, auth=self.auth)
        except PluginException as e:
            raise ConnectionTestException(cause=e.cause, assistance=e.assistance, data=e.data)

        return {"success": True}
