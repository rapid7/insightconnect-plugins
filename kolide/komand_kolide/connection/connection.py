import komand
from .schema import ConnectionSchema
# Custom imports below
from komand_kolide.util.api import Kolide


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api = None

    def connect(self, params={}):
        self.logger.info("Connecting...")

        url = params.get('url')
        base_url = url + "/api"
        api_token = params.get("api_token").get("secretKey")
        verify = params.get("ssl_verify")

        self.api = Kolide(base_url, logger=self.logger, api_token=api_token, verify=verify)

    def test(self):
        try:
            _ = self.api.get_me()
        except Exception as e:
            self.logger.error(
                f"An error occurred while testing Kolide Token: {e}")
            raise
