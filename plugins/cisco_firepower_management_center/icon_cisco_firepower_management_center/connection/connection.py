import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

# Custom imports below
from icon_cisco_firepower_management_center.util.api import CiscoFirePowerApi
from icon_cisco_firepower_management_center.util.host_input import CiscoFirePowerHostInput


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.cisco_firepower_api = None
        self.cisco_firepower_host_input = None
        self.username = None
        self.password = None
        self.host = None
        self.certificate = None
        self.passphrase = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        username, password = (
            params["username_and_password"]["username"],
            params["username_and_password"]["password"],
        )
        self.username = username
        self.password = password
        self.host = params.get(Input.SERVER)
        self.certificate = params.get(Input.CERTIFICATE)
        self.passphrase = params.get(Input.CERTIFICATE_PASSPHRASE).get("secretKey")

        self.cisco_firepower_api = CiscoFirePowerApi(
            username=username,
            password=password,
            url=self.host,
            verify_ssl=params.get(Input.SSL_VERIFY, True),
            port=params.get(Input.PORT, 443),
            domain=params.get(Input.DOMAIN, "Global"),
            logger=self.logger,
        )

        self.cisco_firepower_host_input = CiscoFirePowerHostInput(
            certificate=self.certificate,
            passphrase=self.passphrase,
            server=self.host,
            port=params.get(Input.HOST_INPUT_PORT, 8307),
            logger=self.logger,
        )

    def test(self):
        try:
            self.cisco_firepower_api.get_server_version()
            return {"success": True}
        except PluginException:
            raise ConnectionTestException(
                cause="Connection error.",
                assistance="Please check that the provided credentials are correct and try again.",
            )
