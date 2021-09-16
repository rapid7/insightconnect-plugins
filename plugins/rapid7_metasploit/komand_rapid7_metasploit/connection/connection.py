import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
import ssl
from metasploit.msfrpc import MsfRpcClient


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None
        self.password = None
        self.params = None

    def connect(self, params):
        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError as e:
            self.logger.debug(e)
        else:
            ssl._create_default_https_context = _create_unverified_https_context
        self.logger.info("Connect: Connecting...")
        self.logger.info(params)
        password = params.get(Input.CREDENTIALS)["password"]
        self.client = MsfRpcClient(password, username=params.get(Input.CREDENTIALS).get("username", "msf"), **params)
        self.password = password
        self.params = params
        self.logger.info("Client connection established")

    def reconnect(self):
        self.client = MsfRpcClient(
            self.password, username=self.params.get(Input.CREDENTIALS).get("username", "msf"), **self.params
        )
