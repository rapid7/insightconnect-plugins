import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
import urllib3
from requests import Session
from requests.auth import HTTPBasicAuth
from requests.exceptions import RequestException
from komand_rapid7_insightvm.util import async_requests
from collections import namedtuple
from komand_rapid7_insightvm.util import endpoints
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from typing import Dict, Any


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        self.session = None
        self.console_url = None
        self.async_connection = None
        self.ssl_verify = None
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}) -> None:
        username = params.get(Input.CREDENTIALS, {}).get("username")
        password = params.get(Input.CREDENTIALS, {}).get("password")
        self.console_url = params.get(Input.URL)
        self.ssl_verify = params.get(Input.SSL_VERIFY, True)

        self.session = Session()
        self.session.auth = HTTPBasicAuth(username=username, password=password)
        self.async_connection = async_requests.AsyncRequests(username, password, self.ssl_verify)

        # Suppress insecure request messages
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def test(self) -> Dict[str, Any]:
        """
        Tests connectivity to the InsightVM Console via administrative info endpoint
        :return: Namedtuple indicating connectivity (true = success, false = fail) and error message (if one exists)
        """

        endpoint = endpoints.Administration.get_info(self.console_url)
        Result = namedtuple("Result", "status message")
        success_codes = (200, 201)
        response = None

        try:
            response = self.session.get(url=endpoint, verify=self.ssl_verify)
        except RequestException:
            if response:
                test_result = Result(False, response.json()["message"])
            else:
                test_result = Result(False, "No response received")
        else:
            status = response.status_code
            if status in success_codes:
                test_result = Result(status, "Success")
            else:
                test_result = Result(status, response.json()["message"])

        if not test_result.status:
            raise ConnectionTestException(f"Connectivity test to InsightVM Console failed: {test_result.message}")
        else:
            self.logger.info("Connectivity test to InsightVM Console passed")
            return {"success": True}
