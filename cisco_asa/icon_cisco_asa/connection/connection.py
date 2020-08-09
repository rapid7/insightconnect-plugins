import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
# Custom imports below
from icon_cisco_asa.util.api import CiscoAsaAPI
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.cisco_asa_api = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        self.cisco_asa_api = CiscoAsaAPI(
            verify_ssl=params.get(Input.SSL_VERIFY, True),
            username=params.get(Input.CREDENTIALS).get("username"),
            password=params.get(Input.CREDENTIALS).get("password"),
            url=params.get(Input.URL),
            port=params.get(Input.PORT, 443),
            user_agent=params.get(Input.USER_AGENT, "REST API Agent"),
            logger=self.logger
        )

    def test(self):
        try:
            clock = self.cisco_asa_api.get_clock()
            if not clock.get("date"):
                raise ConnectionTestException(
                    cause="Connection error.",
                    assistance="Problem with connecting to Cisco Server."
                )
        except PluginException as e:
            raise ConnectionTestException(
                cause=e.cause,
                assistance=e.assistance,
                data=e.data
            )

        return {"success": True}
