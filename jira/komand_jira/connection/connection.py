import komand
from .schema import ConnectionSchema
from komand.exceptions import ConnectionTestException
# Custom imports below
from jira import JIRA
import requests
from requests.auth import HTTPBasicAuth


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client, self.url, self.username, self.password = None, None, None, None

    def connect(self, params={}):
        self.url, self.username, self.password = params["url"], \
                                                 params["credentials"]["username"], \
                                                 params["credentials"]["password"]

        test_passed = self.test()
        if test_passed:
            client = JIRA(options={"server": self.url},
                          basic_auth=(
                              self.username,
                              self.password
                          ))

            self.client = client

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
            raise ConnectionTestException(cause="Unable to reach Jira instance at: %s." % self.url,
                                          assistance="Verify the Jira server at the URL configured in your plugin "
                                                     "connection is correct.")
        else:
            self.logger.error(ConnectionTestException(cause="Unhandled error occurred: %s" % response.content))
