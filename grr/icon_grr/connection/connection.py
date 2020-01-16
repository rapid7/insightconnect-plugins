import komand
from .schema import ConnectionSchema
# Custom imports below
from grr_api_client import api


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

        self.grrapi = None
        self.api_endpoint = None
        self.username = None
        self.password = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.api_endpoint = params.get('api_endpoint')
        self.username = params.get('credentials').get('username')
        self.password = params.get('credentials').get('password')
        ssl_verify = params.get('ssl_verify')
        try:
            self.grrapi = api.InitHttp(api_endpoint=self.api_endpoint, auth=(self.username, self.password),
                                       verify=ssl_verify)
        except Exception as e:
            self.logger.error("Please provide valid options to connect to the GRR API endpoint")
            raise e
