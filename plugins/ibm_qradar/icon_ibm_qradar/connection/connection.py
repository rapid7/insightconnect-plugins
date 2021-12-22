"""Connection with Qradar."""
import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ClientException

from .schema import ConnectionSchema


class Connection(insightconnect_plugin_runtime.Connection):
    """Class to handle the connection."""

    def __init__(self):
        """Initialize the connection."""
        super().__init__(input=ConnectionSchema())
        self.username = ""
        self.password = ""
        self.hostname = ""

    def connect(self, params={}):
        """TO read the connection configuration.

        :param params: Config Params required for connection
        :return: None
        """
        self.username = params.get("username", "")
        if self.username == "":
            raise ClientException(Exception("Empty Username provided"))
        self.password = params.get("password", "")
        if self.password == "":
            raise ClientException(Exception("Empty Password provided"))
        self.hostname = params.get("hostname", "")
