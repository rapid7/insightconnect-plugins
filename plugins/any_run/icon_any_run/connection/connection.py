import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from typing import Optional

from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from anyrun import RunTimeException
from anyrun.connectors import LookupConnector
from anyrun.connectors.sandbox.base_connector import BaseSandboxConnector

from icon_any_run.util.config import Config


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.sandbox_api_key: Optional[str] = None
        self.lookup_api_key: Optional[str] = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        self.sandbox_api_key = params.get(Input.SANDBOX_API_KEY, {}).get("secretKey", "")
        self.lookup_api_key = params.get(Input.SANDBOX_API_KEY, {}).get("secretKey", "")

        # In case no authentication method is provided, raise an exception
        if not self.sandbox_api_key and not self.lookup_api_key:
            raise ConnectionTestException(
                cause="No authentication credentials provided in the connection.",
                assistance="Configure the connection with either an API key without a prefix.",
            )

    def test(self):
        platform = None
        try:
            if self.sandbox_api_key:
                with BaseSandboxConnector(self.sandbox_api_key, integration=Config.VERSION) as connector:
                    platform = "ANY.RUN Sandbox"
                    connector.check_authorization()

            if self.lookup_api_key:
                with LookupConnector(self.lookup_api_key, integration=Config.VERSION) as connector:
                    platform = "ANY.RUN TI Lookup"
                    connector.check_authorization()

            return {"success": True}
        except RunTimeException as error:
            raise ConnectionTestException(
                cause="The provided authorization is incorrect.",
                assistance=f"Please check your {platform} API key. If you need help, contact us: techsupport@any.run.",
                data=error.json,
            )
