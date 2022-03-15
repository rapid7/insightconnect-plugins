import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean

from .schema import AddCveInput, AddCveOutput, Input, Output, Component


class AddCve(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_cve", description=Component.DESCRIPTION, input=AddCveInput(), output=AddCveOutput()
        )

    def run(self, params={}):
        response = self.connection.client.add_cve(params.get(Input.CVE_ID, []))
        return clean(
            {
                Output.SUCCESS_AMOUNT: response.get("success", {}).get("amount"),
                Output.FAILURE: response.get(Output.FAILURE),
            }
        )
