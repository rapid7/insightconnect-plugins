import insightconnect_plugin_runtime
from .schema import ConnectionSchema

# Custom imports below
from typing import Dict, Any


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}) -> None:
        pass

    @staticmethod
    def test() -> Dict[str, Any]:
        return {"success": True}
