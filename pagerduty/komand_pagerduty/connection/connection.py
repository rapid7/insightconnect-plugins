import insightconnect_plugin_runtime
from .schema import ConnectionSchema

# Custom imports below
import pypd
import requests
from komand_pagerduty.util.async_requests import AsyncRequests
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        """
        Connect to PagerDuty
        """

        key = params.get("api_key").get("secretKey")
        pypd.api_key = key
        pypd.Incident.find(maximum=1)

        self.api_connection = requests.Session()
        headers = {"Authorization": f"Token token={key}"}
        self.api_connection.headers = headers

        self.async_connection = AsyncRequests(api_key=key)

    def test(self):
        response = self.api_connection.get("https://api.pagerduty.com/users")
        try:
            response.raise_for_status()
        except Exception as e:
            raise ConnectionTestException(
                cause="Connection Test Failed",
                assistance="Please check your API key. " "See the following for more information.",
                data=str(e),
            )
        return {"success": True}
