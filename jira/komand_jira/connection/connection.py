import komand
from .schema import ConnectionSchema, Input

# Custom imports below
from jira import JIRA
import requests
from requests.auth import HTTPBasicAuth
from komand.exceptions import ConnectionTestException
from komand_jira.util.api import JiraApi


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client, self.url, self.username, self.password, self.is_cloud = None, None, None, None, False
        self.rest_client = None

    def connect(self, params={}):
        self.url = params.get(Input.URL)
        self.username = params.get(Input.USER)
        self.password = params.get(Input.API_KEY).get("secretKey")

        if ".atlassian.net" in self.url or ".jira.com" in self.url:
            self.is_cloud = True

        test_passed = self.test()
        if test_passed:
            client = JIRA(
                options={"server": self.url},
                basic_auth=(
                    self.username,
                    self.password
                )
            )

            self.client = client
            self.rest_client = JiraApi(self.client, self.is_cloud, self.logger)

    def test(self):
        auth = HTTPBasicAuth(username=self.username,
                             password=self.password)

        response = requests.get(self.url, auth=auth)

        # https://developer.atlassian.com/cloud/jira/platform/rest/v2/?utm_source=%2Fcloud%2Fjira%2Fplatform%2Frest%2F&utm_medium=302#error-responses
        if response.status_code == 200:
            return True
        elif response.status_code == 401:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.USERNAME_PASSWORD)
        elif response.status_code == 404:
            raise ConnectionTestException(cause=f"Unable to reach Jira instance at: {self.url}.",
                                          assistance="Verify the Jira server at the URL configured in your plugin "
                                                     "connection is correct.")
        else:
            raise ConnectionTestException(cause=f"Unhandled error occurred.",
                                          assistance=response.content)
