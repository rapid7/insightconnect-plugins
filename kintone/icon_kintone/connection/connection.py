import komand
from komand.exceptions import ConnectionTestException
from .schema import ConnectionSchema, Input
# Custom imports below
from icon_kintone.util.kintone import get_api_list


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.api_key = params.get(Input.API_KEY).get("secretKey")
        self.verify_ssl = params.get(Input.VERIFY_SSL, False)

    def test(self):
        if self.api_key is None:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY)

        response = get_api_list(self.logger, self.api_key, self.verify_ssl)
        if not response:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY)
