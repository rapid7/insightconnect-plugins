import komand
from .schema import ConnectionSchema
# Custom imports below
from komand_cherwell.util.api import Cherwell


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self._base_url = None
        self.api = None

    def connect(self, params={}):

        base_uri = params["url"]
        username, password = params["username_and_password"]["username"], params["username_and_password"]["password"]
        client_id = params["client_id"]["secretKey"]
        authentication_mode = params["authentication_mode"]

        # Form the base URL for the Cherwell server
        scheme = "https://" if params["ssl_verify"] else "http://"
        self._base_url = scheme + base_uri

        self.api = Cherwell(self._base_url, self.logger, username, password, client_id, authentication_mode)

    def test(self):
        try:
            _ = self.api.get_serviceinfo()
        except Exception as e:
            self.logger.error(f"An error occurred while testing Cherwell credentials: {e}")
            raise
