import insightconnect_plugin_runtime

from .schema import ConnectionSchema, Input

# Custom imports below
from jira import JIRA
import requests
import os
from requests.auth import HTTPBasicAuth
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from komand_jira.util.api import JiraApi
from komand_jira.util.constants import REQUESTS_TIMEOUT


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None
        self.url = None
        self.username = None
        self.password = None
        self.is_cloud = False
        self.rest_client = None

    def _validate_params(self, params={}):
        self.url = params.get(Input.URL, "").strip()
        self.username = params.get(Input.USER, "").strip()
        self.password = params.get(Input.API_KEY, {}).get("secretKey", "").strip()
        self.pat = params.get(Input.PAT, {}).get("secretKey", "").strip()

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

    def connect(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        self._validate_params(params)
        # END INPUT BINDING - DO NOT REMOVE

        if ".atlassian.net" in self.url or ".jira.com" in self.url:
            self.is_cloud = True

        # add a check that if not are running on orchestrator, we are only trying to connect to Jira cloud instance
        if not self.is_cloud and os.environ.get("PLUGIN_RUNTIME_ENVIRONMENT", "") == "cloud":
            raise ConnectionTestException(
                cause="Connection to Jira on-prem instance detected. please use a Jira Cloud instance.",
                assistance="When running on ICON cloud we only support connections to Jira Cloud instances.",
            )

        if self.pat:
            client = JIRA(options={"server": self.url}, token_auth=self.pat)
            rest_client = JiraApi(self.url, {"Authorization": f"Bearer {self.pat}"}, self.logger)
        elif self.test():
            client = JIRA(options={"server": self.url}, basic_auth=(self.username, self.password))
            rest_client = JiraApi(self.url, HTTPBasicAuth(username=self.username, password=self.password), self.logger)
        else:
            raise PluginException(cause="Please provide basic_auth or PAT.")

        self.client = client
        self.rest_client = rest_client

    def test_pat(self) -> tuple[str, int]:
        with requests.Session() as session, session.get(
            self.url,
            headers={"Authorization": f"Bearer {self.pat}", "Content-Type": "application/json"},
            timeout=REQUESTS_TIMEOUT,
        ) as response:
            return response.content, response.status_code

    def test_basic_auth(self) -> tuple[str, int]:
        with requests.Session() as session, session.get(
            self.url, auth=HTTPBasicAuth(username=self.username, password=self.password), timeout=REQUESTS_TIMEOUT
        ) as response:
            return response.content, response.status_code

    def test(self) -> dict[str, bool]:
        # If a PAT is provided, use it to test the connection. Otherwise, fall back to basic auth testing.
        test_method = self.test_pat if self.pat else self.test_basic_auth
        content, status_code = test_method()

        # https://developer.atlassian.com/cloud/jira/platform/rest/v2/?utm_source=%2Fcloud%2Fjira%2Fplatform%2Frest%2F&utm_medium=302#error-responses
        if status_code == 200:
            return {"success": True}
        elif status_code == 401:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.USERNAME_PASSWORD)
        elif status_code == 404:
            raise ConnectionTestException(
                cause=f"Unable to reach Jira instance at: {self.url}.",
                assistance="Verify the Jira server at the URL configured in your plugin " "connection is correct.",
            )
        else:
            raise ConnectionTestException(cause="Unhandled error occurred.", assistance=content)
