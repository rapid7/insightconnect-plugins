import logging

import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from ..util.api import API


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.phishtank_api = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        self.phishtank_api = API(
            credentials=params.get(Input.CREDENTIALS).get("secretKey"), username=params.get(Input.USERNAME)
        )

    def test(self):
        endpoint = "phishtank/status"
        try:
            self.phishtank_api.check(endpoint)
            return {"success": True}
        except Exception as exception:
            self.logger.error(f"Error: {str(exception)}")
            raise ConnectionTestException(preset=ConnectionTestException.Preset.UNAUTHORIZED, data=exception)
