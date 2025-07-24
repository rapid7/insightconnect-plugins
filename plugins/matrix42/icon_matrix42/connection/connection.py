import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
import requests
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_key = None
        self.server_name = None
        self.api_url = None
        self.access_token = None
        self.request_header = None

    def get_access_token(self):
        """
        Get a temporary access token from Matrix42 using the API key.
        """

        # Prepare the URL for generating an access token
        token_url = self.api_url + "ApiToken/GenerateAccessTokenFromApiToken"

        # Request the access token from Matrix42
        headers = {"Authorization": f"Bearer {self.api_key}", "Accept": "application/json"}

        try:
            self.logger.info(f"Requesting access token with API key from {token_url}")
            response = requests.post(token_url, headers=headers)  # nosec B113
            response.raise_for_status()
        except requests.RequestException as e:
            raise ConnectionTestException(
                cause="Failed to retrieve access token from Matrix42.",
                assistance="Please check your Matrix42 API URL and API key.",
                data=str(e),
            )

        # Extract the access token from the response
        try:
            access_token = response.json().get("RawToken")

        except ValueError as e:
            raise ConnectionTestException(
                cause="Failed to parse the access token from Matrix42.",
                assistance="Ensure that the API key is valid and the Matrix42 API is reachable.",
                data=str(e),
            )

        return access_token

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        self.api_key = params.get(Input.API_KEY).get("secretKey").strip()
        self.server_name = params.get(Input.SERVER_NAME).strip()
        # END INPUT BINDING - DO NOT REMOVE

        # Prepare the API URL
        self.api_url = f"https://{self.server_name}/m42Services/api/"

        # Get the access token
        self.access_token = self.get_access_token()

        # Prepare headers
        self.request_header = {
            "Authorization": f"Bearer {self.access_token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

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
