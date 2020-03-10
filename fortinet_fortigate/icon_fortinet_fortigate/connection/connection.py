import komand
from .schema import ConnectionSchema, Input
# Custom imports below
from requests import Session
import requests
from komand.exceptions import ConnectionTestException


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.api_key = params.get(Input.API_KEY).get("secretKey")
        self.host = params.get(Input.HOSTNAME)

        self.session_params = {"access_token": self.api_key}
        self.ssl_verify = params.get(Input.SSL_VERIFY)

        self.session = Session()
        self.session.params = self.session_params

        # This is broken. Leaving this here as its supposed to be fixed in a future version of requests
        # self.session.verify = self.ssl_verify

    def test(self):
        endpoint = f"https://{self.host}/api/v2/cmdb/firewall.consolidated/policy"
        result = self.session.get(endpoint, verify=self.ssl_verify)

        try:
            result.raise_for_status()
        except Exception:
            raise ConnectionTestException(cause=f"Could not connect to {self.host}\n",
                                          assistance="Please check your connection settings\n",
                                          data=result.text)
        return result.json()
