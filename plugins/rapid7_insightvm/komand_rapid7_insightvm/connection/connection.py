import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
import urllib3
from requests import Session
from requests.auth import HTTPBasicAuth
from requests.exceptions import RequestException
from komand_rapid7_insightvm.util import async_requests
from komand_rapid7_insightvm.util import endpoints
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        self.session = None
        self.console_url = None
        self.async_connection = None
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        username = params.get(Input.CREDENTIALS).get("username")
        password = params.get(Input.CREDENTIALS).get("password")
        self.console_url = params.get(Input.URL)

        self.session = Session()
        self.session.auth = HTTPBasicAuth(username=username, password=password)
        self.async_connection = async_requests.AsyncRequests(username, password)

        # Suppress insecure request messages
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def test(self):
        """
        Tests connectivity to the InsightVM Console via administrative info endpoint
        """

        endpoint = endpoints.Administration.get_info(self.console_url)

        try:
            response = self.session.get(url=endpoint, verify=False)

            if response.status_code in (200, 201):
                return {"success": True}

            else:
                return {"success": False}

        except RequestException as error:
            raise ConnectionTestException(
                cause="Connection Test Failed.", assistance="Check logs for details.", data=error
            )
