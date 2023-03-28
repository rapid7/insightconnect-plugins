import insightconnect_plugin_runtime
from .schema import DlGetAllInput, DlGetAllOutput, Input, Output, Component
from typing import Any, Dict
from insightconnect_plugin_runtime.helper import clean

# Custom imports below


class DlGetAll(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="dlGetAll",
            description=Component.DESCRIPTION,
            input=DlGetAllInput(),
            output=DlGetAllOutput(),
        )

    def run(self, _params=None):
        result = self.connection.client.get_destination_lists().get("data", [])
        result = clean(result)
        print("DLDEBUG result: {}".format(result))
        print("DLDEBUG result.createdAt: {}".format(result[0].get("createdAt")))



        return {Output.DATA: result}
