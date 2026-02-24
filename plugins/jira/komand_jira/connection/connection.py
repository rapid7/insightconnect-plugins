import insightconnect_plugin_runtime

from .schema import ConnectionSchema, Input

# Custom imports below
from jira import JIRA
import os
from requests.auth import HTTPBasicAuth
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from komand_jira.util.api import JiraApi
from komand_jira.util.constants import CLOUD_DOMAIN_PATTERNS


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
        # Extract parameters and strip whitespace
        self.url = params.get(Input.URL, "").strip()
        self.username = params.get(Input.USER, "").strip()
        self.password = params.get(Input.API_KEY, {}).get("secretKey", "").strip()
        self.pat = params.get(Input.PAT, {}).get("secretKey", "").strip()
        self.client_id = params.get(Input.CLIENT_ID, "").strip()
        self.client_secret = params.get(Input.CLIENT_SECRET, {}).get("secretKey", "").strip()

        # Check how many authentication methods are provided
        auth_methods_provided = sum(
            [bool(self.pat), bool(self.client_id or self.client_secret), bool(self.username or self.password)]
        )

        # Ensure only one auth method is provided
        if auth_methods_provided > 1:
            raise PluginException(
                cause="Multiple authentication methods provided.",
                assistance="Provide only ONE of: PAT, OAuth2 (client_id + client_secret), or Basic Auth (username + password).",
            )

        # Validate PAT (Personal Access Token)
        if self.pat:
            if self.username or self.password or self.client_id or self.client_secret:
                raise PluginException(
                    cause="PAT provided along with other credentials.",
                    assistance="When using PAT, do not provide any other credentials.",
                )
            return

        # Validate OAuth2 credentials
        if self.client_id or self.client_secret:
            if not (self.client_id and self.client_secret):
                raise PluginException(
                    cause="Incomplete OAuth2 credentials.",
                    assistance="Both 'client_id' and 'client_secret' must be provided for OAuth2 authentication.",
                )
            if self.username or self.password:
                raise PluginException(
                    cause="OAuth2 credentials provided along with Basic Auth credentials.",
                    assistance="When using OAuth2, do not provide username or password.",
                )
            return

        # Validate Basic Auth credentials
        if self.username or self.password:
            if not (self.username and self.password):
                raise PluginException(
                    cause="Incomplete Basic Auth credentials.",
                    assistance="Both 'username' and 'password' must be provided for Basic Auth authentication.",
                )
            return

        # No credentials provided
        raise PluginException(
            cause="No authentication credentials provided.",
            assistance="Provide ONE of: PAT, OAuth2 (client_id + client_secret), or Basic Auth (username + password).",
        )

    def connect(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        self._validate_params(params)
        # END INPUT BINDING - DO NOT REMOVE

        # Determine if the URL is for a Jira Cloud instance based on common patterns
        if any(url in self.url for url in CLOUD_DOMAIN_PATTERNS):
            self.is_cloud = True

        # add a check that if not are running on orchestrator, we are only trying to connect to Jira cloud instance
        if not self.is_cloud and os.environ.get("PLUGIN_RUNTIME_ENVIRONMENT", "") == "cloud":
            raise ConnectionTestException(
                cause="Connection to Jira on-prem instance detected. please use a Jira Cloud instance.",
                assistance="When running on ICON cloud we only support connections to Jira Cloud instances.",
            )

        # Initialize the appropriate client based on the provided authentication method
        if self.pat:
            client = JIRA(options={"server": self.url}, token_auth=self.pat)
            rest_client = JiraApi(self.url, {"Authorization": f"Bearer {self.pat}"}, self.logger)
        elif self.client_id and self.client_secret:
            # Jira library doesn't support OAuth2
            client = None
            rest_client = JiraApi(
                self.url, {"client_id": self.client_id, "client_secret": self.client_secret}, self.logger
            )
        else:
            client = JIRA(options={"server": self.url}, basic_auth=(self.username, self.password))
            rest_client = JiraApi(self.url, HTTPBasicAuth(username=self.username, password=self.password), self.logger)

        self.client = client
        self.rest_client = rest_client

    def test(self) -> dict[str, bool]:
        # https://developer.atlassian.com/cloud/jira/platform/rest/v2/?utm_source=%2Fcloud%2Fjira%2Fplatform%2Frest%2F&utm_medium=302#error-responses
        try:
            self.rest_client.test_connection()
            return {"success": True}
        except PluginException as error:
            if error.preset == ConnectionTestException.Preset.BAD_REQUEST:
                raise ConnectionTestException(
                    cause=f"Unable to reach Jira instance at: {self.url}.",
                    assistance="Verify the Jira server at the URL configured in your plugin " "connection is correct.",
                )
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance)
        except Exception as error:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.UNKNOWN, data=error)
