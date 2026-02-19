import insightconnect_plugin_runtime

from .schema import ConnectionSchema
from typing import Dict

# Custom imports below


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        pass

    @staticmethod
    def test() -> Dict[str, bool]:
        return {"success": True}
