import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
# Custom imports below
from icon_sonicwall.util.api import SonicWallAPI
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.sonicwall_api = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.sonicwall_api = SonicWallAPI(
            verify_ssl=params.get(Input.VERIFY_SSL, True),
            username=params.get(Input.CREDENTIALS).get("username"),
            password=params.get(Input.CREDENTIALS).get("password"),
            url=params.get(Input.URL),
            port=params.get(Input.PORT, 443),
            logger=self.logger
        )

    def test(self):
        try:
            if self.sonicwall_api.login().get("status", {}).get("success", False):
                return {}
        except PluginException as e:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.UNAUTHORIZED, data=e)
        finally:
            self.sonicwall_api.logout()

        raise ConnectionTestException(preset=ConnectionTestException.Preset.UNKNOWN)
