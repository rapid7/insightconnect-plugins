import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from ..util.api import GitLabAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.token = None
        self.username = None
        self.url = None
        self.ssl_verify = True
        self.client = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")

        self.token = params.get(Input.CREDENTIALS, {}).get("password")
        self.username = params.get(Input.CREDENTIALS, {}).get("username")
        self.url = params.get(Input.URL) + "/api/v4"
        self.ssl_verify = params.get(Input.SSL_VERIFY, True)

        self.client = GitLabAPI(base_url=self.url, token=self.token, verify=self.ssl_verify)
