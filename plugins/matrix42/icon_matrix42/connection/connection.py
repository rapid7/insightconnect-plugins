import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
import requests
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def get_access_token(self):
        """
        Get a temporary access token from Matrix42 using the API key.
        """
        # Ensure api_url ends with a single slash
        base_url = self.api_url.rstrip("/") + "/"
        token_url = base_url + "ApiToken/GenerateAccessTokenFromApiToken"

        headers = {"Authorization": f"Bearer {self.api_key}", "Accept": "application/json"}

        try:
            self.logger.info(f"Requesting access token with API key from {token_url}")
            response = requests.post(token_url, headers=headers)
            response.raise_for_status()
        except requests.RequestException as e:
            raise ConnectionTestException(
                cause="Failed to retrieve access token from Matrix42.",
                assistance="Please check your Matrix42 API URL and API key.",
                data=str(e),
            )

        return response.json().get("RawToken")

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        self.api_key = params.get(Input.API_KEY).get("secretKey")
        self.api_url = params.get(Input.API_URL)
        # END INPUT BINDING - DO NOT REMOVE

        self.access_token = self.get_access_token()

    def test(self):
        """
        Test the connection by attempting to retrieve an access token.
        """
        try:
            token = self.get_access_token()
            if not token:
                raise ConnectionTestException(
                    cause="No access token received from Matrix42.",
                    assistance="Please check your API key and URL.",
                )
            return {"success": True}
        except ConnectionTestException:
            raise
        except Exception as e:
            raise ConnectionTestException(
                cause="Connection test failed.",
                assistance="An unexpected error occurred during the connection test.",
                data=str(e),
            )
