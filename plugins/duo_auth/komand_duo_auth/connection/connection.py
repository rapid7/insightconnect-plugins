from typing import Dict

# Custom imports below
import duo_client
import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException

from .schema import ConnectionSchema, Input


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.auth_api = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")
        self.auth_api = duo_client.Auth(
            ikey=params.get(Input.INTEGRATION_KEY, {}).get("secretKey", "").strip(),
            skey=params.get(Input.SECRET_KEY, {}).get("secretKey", "").strip(),
            host=params.get(Input.HOSTNAME, "").strip(),
        )

    def test(self) -> Dict[str, bool]:
        try:
            self.auth_api.ping()
            self.auth_api.check()
            return {"success": True}
        except Exception as error:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.UNKNOWN, data=error)
