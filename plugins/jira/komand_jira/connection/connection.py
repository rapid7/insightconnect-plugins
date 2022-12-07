import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from jira import JIRA
import requests
from requests.auth import HTTPBasicAuth
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from komand_jira.util.api import JiraApi


class Connection(insightconnect_plugin_runtime.Connection):
    def _validate_params(self, params={}):
        self.url = params.get(Input.URL, "")
        self.username = params.get(Input.USER)
        self.password = params.get(Input.API_KEY, {}).get("secretKey", "")
        self.pat = params.get(Input.PAT, {}).get("secretKey", "")

        if (self.username and self.pat) or (self.password and self.pat):
            raise PluginException(
                cause="Both Basic Auth and PAT credentials provided",
                assistance="Provide either PAT or Basic Auth credentials",
            )
        elif self.username and not self.password:
            raise PluginException(cause="Username provided but no password.", assistance="Please also provide password")
        elif not self.username and self.password:
            raise PluginException(cause="Password provided but no username.", assistance="Please also provide username")
        elif not self.username and not self.password and not self.pat:
            raise PluginException(cause="No credentials provided at all.", assistance="Please provide some credentials")

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client, self.url, self.username, self.password, self.is_cloud = (
            None,
            None,
            None,
            None,
            False,
        )
        self.rest_client = None

    def connect(self, params={}):
        self._validate_params(params)

        if ".atlassian.net" in self.url or ".jira.com" in self.url:
            self.is_cloud = True
        if self.pat:
            client = JIRA(options={"server": self.url}, token_auth=self.pat)
        elif self.test():
            client = JIRA(options={"server": self.url}, basic_auth=(self.username, self.password))
        else:
            raise PluginException(cause="Please provide basic_auth or PAT.")

        self.client = client
        self.rest_client = JiraApi(self.client, self.is_cloud, self.logger)

    def test(self):
        auth = HTTPBasicAuth(username=self.username, password=self.password)

        response = requests.get(self.url, auth=auth)

        # https://developer.atlassian.com/cloud/jira/platform/rest/v2/?utm_source=%2Fcloud%2Fjira%2Fplatform%2Frest%2F&utm_medium=302#error-responses
        if response.status_code == 200:
            return True
        elif response.status_code == 401:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.USERNAME_PASSWORD)
        elif response.status_code == 404:
            raise ConnectionTestException(
                cause=f"Unable to reach Jira instance at: {self.url}.",
                assistance="Verify the Jira server at the URL configured in your plugin " "connection is correct.",
            )
        else:
            raise ConnectionTestException(cause="Unhandled error occurred.", assistance=response.content)
