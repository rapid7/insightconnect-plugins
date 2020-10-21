import komand
from .schema import ConnectionSchema
# Custom imports below
import pypd
import requests
from komand.exceptions import ConnectionTestException

class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        """
        Connect to PagerDuty
        """

        key = params.get('api_key').get('secretKey')
        pypd.api_key = key
        self.logger.debug("Connecting: %s", key)
        pypd.Incident.find(maximum=1)

        self.api_connection = requests.Session()
        headers = {
            "Authorization": f"Token token={key}"
        }
        self.api_connection.headers = headers

    def test(self):
        response = self.api_connection.get("https://api.pagerduty.com/users")
        try:
            response.raise_for_status()
        except Exception as e:
            raise ConnectionTestException(cause="Connection Test Failed",
                                          assistance="Please check your API key. "
                                                     "See the following for more information.",
                                          data=str(e))
        return {"success": True}