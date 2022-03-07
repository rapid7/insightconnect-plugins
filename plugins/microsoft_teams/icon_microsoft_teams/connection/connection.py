import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
import requests
import time


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.app_id = params.get(Input.APPLICATION_ID)
        self.tenant_id = params.get(Input.DIRECTORY_ID)
        self.app_secret = params.get(Input.APPLICATION_SECRET).get("secretKey")
        self.username = params.get(Input.USERNAME_PASSWORD).get("username")
        self.password = params.get(Input.USERNAME_PASSWORD).get("password")

        self.api_token = ""
        self.refresh_token = ""

        # Auth tokens expire after 1 hour. Only make that call if we need to
        self.time_ago = 0  # Jan 1, 1970
        self.time_now = time.time()  # More than 1 hour since 1978

        self.check_and_refresh_api_token()

    def get_token(self):
        self.logger.info("Updating Auth Token...")
        token_url = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/token"

        body = {
            "resource": "https://graph.microsoft.com",
            "grant_type": "password",
            "client_id": self.app_id,
            "client_secret": self.app_secret,
            "username": self.username,
            "password": self.password,
        }

        if self.refresh_token:
            body["refresh_token"] = self.refresh_token

        self.logger.info(f"Getting token from: {token_url}")
        result = requests.post(token_url, data=body)

        try:
            result.raise_for_status()
        except Exception as e:
            raise PluginException(
                cause="Authentication to Microsoft Graph failed.",
                assistance=f"Some common causes for this error include an invalid username, password, or connection settings."
                f"Verify you are using the correct domain name for your user, and verify that user has access to "
                f"the target tenant. Verify you can log into Office365 with the user account as well.\n"
                f"The result returned was:\n{result.text}",
                data=e,
            ) from e

        result_json = result.json()
        self.api_token = result_json.get("access_token")
        self.refresh_token = result_json.get("refresh_token")

        self.logger.info(f"Authentication was successful, token is: ******************{self.api_token[-5:]}")
        self.logger.info(f"Detected Permissions: {result_json.get('scope')}")

    def check_and_refresh_api_token(self, force_refresh_token=False):
        self.time_now = time.time()
        self.logger.info(f"Time Now: {self.time_now}")
        self.logger.info(f"Time Ago: {self.time_ago}")
        if (self.time_now - self.time_ago) > 3500 or force_refresh_token:  # 1 hour in seconds (minus some buffer time)
            self.logger.info("Refreshing auth token")
            self.get_token()
            self.time_ago = time.time()
        else:
            self.logger.info("Token is valid, not refreshing.")

    def get_headers(self, forceRefreshToken=False):
        self.check_and_refresh_api_token(forceRefreshToken)
        headers = {"Authorization": f"Bearer {self.api_token}", "Content-Type": "application/json"}
        return headers

    def test(self):
        try:
            self.check_and_refresh_api_token()
        except PluginException as e:
            raise ConnectionTestException(
                cause="Unable to get authentication token.",
                assistance="Please check your connection settings.",
            ) from e
        if not self.api_token:
            raise ConnectionTestException(
                cause="No authentication token found.",
                assistance="Please check your connection settings.",
            )
