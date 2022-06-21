import komand
from .schema import ConnectionSchema
from komand.exceptions import ConnectionTestException

# Custom imports below
import pyldfire


class Connection(komand.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")
        # These are for cases where the library doesn't support what we want
        self.host = params.get("host")
        self.api_key = params.get("api_key").get("secretKey")

        if params.get("proxy"):
            proxy = params.get("proxy")
            self.logger.info("Using proxy: %s", proxy)
        else:
            proxy = {}

        self.client = pyldfire.WildFire(self.api_key, host=self.host, verify=params.get("verify"), proxies=proxy)

    def test(self):
        try:
            self.client.submit_urls("insight.rapid7.com")
        except pyldfire.WildFireException as e:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY, data=e)

        return {"success": True}
