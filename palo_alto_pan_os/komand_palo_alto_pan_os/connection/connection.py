import komand
from .schema import ConnectionSchema
# Custom imports below
from komand_palo_alto_pan_os.util.pan_os_requests import Request
from komand.exceptions import ConnectionTestException


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.request = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")

        hostname = params.get("server")
        verify_cert = params.get("verify_cert")

        username = params.get('credentials').get('username')
        password = params.get('credentials').get('password')
        self.request = Request.new_session(self, username, password, hostname, verify_cert)

    def test(self):
        if len(self.request.key) > 0:
            return {
                "success": True
            }
        raise ConnectionTestException(
            preset=ConnectionTestException.Preset.USERNAME_PASSWORD
        )
