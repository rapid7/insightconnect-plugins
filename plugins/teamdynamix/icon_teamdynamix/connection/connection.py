"""TeamDynamix InsightConnect Plugin Connection."""

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from icon_teamdynamix.util.request_helper import TeamDynamixClient
from .schema import ConnectionSchema, Input

AUTH_TYPE_ADMIN = "Admin"
AUTH_TYPE_USER = "User"


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client: TeamDynamixClient = None

    def connect(self, params):
        self.logger.info("Connection: Connecting to TeamDynamix...")

        base_url = params.get(Input.BASE_URL, "").strip().rstrip("/")
        auth_type = params.get(Input.AUTH_TYPE, AUTH_TYPE_ADMIN)
        app_id = params.get(Input.APP_ID)

        if auth_type == AUTH_TYPE_ADMIN:
            beid = params.get(Input.BEID, "").strip()
            web_services_key = params.get(Input.WEB_SERVICES_KEY, {}).get("secretKey", "").strip()

            if not beid or not web_services_key:
                raise PluginException(
                    cause="BEID and Web Services Key are required for Admin authentication",
                    assistance="Provide both BEID and Web Services Key in the connection settings",
                )

            self.client = TeamDynamixClient(
                base_url=base_url,
                auth_type="admin",
                beid=beid,
                web_services_key=web_services_key,
                app_id=app_id,
                logger=self.logger,
            )
        else:
            credentials = params.get(Input.CREDENTIALS, {})
            username = credentials.get("username", "").strip()
            password = credentials.get("password", "").strip()

            if not username or not password:
                raise PluginException(
                    cause="Username and password are required for User authentication",
                    assistance="Provide both username and password in the connection settings",
                )

            self.client = TeamDynamixClient(
                base_url=base_url,
                auth_type="user",
                username=username,
                password=password,
                app_id=app_id,
                logger=self.logger,
            )

        self.logger.info(f"Connection: TeamDynamix client initialized with {auth_type} authentication.")

    def test(self):
        try:
            self.client.test()
            return {"success": True}
        except Exception as error:
            raise ConnectionTestException(
                preset=ConnectionTestException.Preset.UNKNOWN,
                data=str(error),
            )
