import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
import requests

from icon_ibm_qradar.util.utils import handle_response
from icon_ibm_qradar.util.constants.endpoints import SYSTEM_INFO
from icon_ibm_qradar.util.constants.constant import REQUEST_TIMEOUT


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super().__init__(input=ConnectionSchema())
        self.username = None
        self.password = None
        self.host_url = ""
        self.verify_ssl = None

    def connect(self, params={}):
        """To read the connection configuration.

        :param params: Config Params required for connection
        :return: None
        """
        credentials = params.get(Input.CREDENTIALS)
        self.username = credentials.get("username")
        self.password = credentials.get("password")
        self.verify_ssl = params.get(Input.VERIFY_SSL, False)
        self.host_url = params.get(Input.HOST_URL)
        if self.host_url.endswith("/"):
            self.host_url = self.host_url[:-1]

    def test(self):
        """To test the connection.

        :param params: Config Params required for connection
        :return dict: connection was successful
        """
        auth = (self.username, self.password)
        response = requests.get(
            url=f"{self.host_url}/{SYSTEM_INFO}", auth=auth, verify=self.verify_ssl, timeout=REQUEST_TIMEOUT
        )
        handle_response(response=response)
        return {"connection": "successful"}
