import komand
from .schema import ConnectionSchema, Input
# Custom imports below
import ipahttp
from komand.exceptions import ConnectionTestException


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.ipa = None

    def connect(self, params):
        server = params.get(Input.SERVER)
        username = params.get(Input.CREDENTIALS).get('username')
        password = params.get(Input.CREDENTIALS).get('password')

        self.ipa = ipahttp.ipa(server)
        self.ipa.login(username, password)
        self.logger.info("Connect: Connecting...")

    def test(self):
        test = self.ipa
        if test is None:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.USERNAME_PASSWORD)
        return {}
