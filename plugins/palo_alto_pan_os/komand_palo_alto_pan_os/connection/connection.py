import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from komand_palo_alto_pan_os.util.pan_os_requests import Request
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.request = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")

        hostname = params.get(Input.SERVER)
        verify_cert = params.get(Input.VERIFY_CERT)

        username = params.get(Input.CREDENTIALS).get("username")
        password = params.get(Input.CREDENTIALS).get("password")
        self.request = Request.new_session(self, username, password, hostname, verify_cert)

    def test(self):
        if len(self.request.key) > 0:
            return {"success": True}
        raise ConnectionTestException(preset=ConnectionTestException.Preset.USERNAME_PASSWORD)
