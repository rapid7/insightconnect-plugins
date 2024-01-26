import github
import requests
import insightconnect_plugin_runtime

from komand_github.util.util import TIMEOUT
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
from komand_github.connection.schema import ConnectionSchema, Input

# Custom imports below


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.github_user = None
        self.user_data = ""
        self.user = None
        self.username = ""
        self.api_prefix = "https://api.github.com"
        self.secret = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")
        try:
            credentials = params.get(Input.CREDENTIALS)
            self.username = credentials.get("username")
            self.secret = credentials.get("personal_token", {}).get("secretKey")
            self.auth_header = {"Authorization": f"Bearer {self.secret}"}
            self.github_user = github.Github(auth=github.Auth.Token(self.secret))
            self.user = self.github_user.get_user(self.username)
            self.github_session = requests.Session()

        except github.GithubException:
            raise PluginException(
                cause="Github: Connect: user could not be authenticated please try again.",
                assistance="Please check that your username and personal token is correct.",
            )

    def test(self):
        try:
            self.github_session_user = requests.get(
                f"{self.api_prefix}/user", headers=self.auth_header, verify=True, timeout=TIMEOUT
            )

            if self.github_session_user.status_code == 200:
                self.logger.info("Connect: Login successful")
                return {"Success": True}
            else:
                self.logger.info("Connect: Login unsuccessful")
                raise ConnectionTestException(
                    cause="Connection Test Failed.",
                    assistance="Please check that your username and personal is correct.",
                )
        except PluginException:
            raise ConnectionTestException(cause="Connection Test Failed.")
