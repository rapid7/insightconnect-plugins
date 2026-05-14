"""TeamDynamix InsightConnect Plugin Connection."""

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException

from icon_teamdynamix.util.request_helper import TeamDynamixClient
from .schema import ConnectionSchema, Input


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client: TeamDynamixClient = None

    def connect(self, params):
        self.logger.info("Connection: Connecting to TeamDynamix...")

        base_url = params.get(Input.BASE_URL, "").strip().rstrip("/")
        beid = params.get(Input.BEID, "").strip()
        web_services_key = params.get(Input.WEB_SERVICES_KEY, {}).get("secretKey", "").strip()
        app_id = params.get(Input.APP_ID)

        self.client = TeamDynamixClient(
            base_url=base_url,
            beid=beid,
            web_services_key=web_services_key,
            app_id=app_id,
            logger=self.logger,
        )

        self.logger.info("Connection: TeamDynamix client initialized.")

    def test(self):
        try:
            self.client.test()
            return {"success": True}
        except Exception as e:
            raise ConnectionTestException(
                preset=ConnectionTestException.Preset.UNKNOWN,
                data=str(e),
            )
