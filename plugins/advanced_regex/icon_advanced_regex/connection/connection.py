import insightconnect_plugin_runtime
from .schema import ConnectionSchema

# Custom imports below
from typing import Dict


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        pass

    def test(self) -> Dict[str, bool]:
        return {"success": True}
