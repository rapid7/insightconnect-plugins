import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
import requests

from icon_ibm_qradar.util.utils import handle_response
from icon_ibm_qradar.util.constants.endpoints import SYSTEM_INFO


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super().__init__(input=ConnectionSchema())
        self.username = ""
        self.password = ""
        self.host_url = ""
        self.verify_ssl = False

    def connect(self, params={}):
        """To read the connection configuration.

        :param params: Config Params required for connection
        :return: None
        """
        credentials = params.get(Input.CREDENTIALS)
        self.username = credentials.get("username")
        self.password = credentials.get("password")
        self.host_url = params.get(Input.HOST_URL)
        self.verify_ssl = params.get(Input.VERIFY_SSL, False)

    def test(self, params):
        """To test the connection.

        :param params: Config Params required for connection
        :return dict: connection was successful
        """
        auth = (self.username, self.password)
        response = requests.get(url=f"{self.host_url}{SYSTEM_INFO}", auth=auth, verify=self.verify_ssl)
        handle_response(response=response)
        return {"connection": "successful"}
