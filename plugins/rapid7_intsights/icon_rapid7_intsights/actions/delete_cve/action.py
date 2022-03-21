import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean

from .schema import DeleteCveInput, DeleteCveOutput, Input, Output, Component


class DeleteCve(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_cve", description=Component.DESCRIPTION, input=DeleteCveInput(), output=DeleteCveOutput()
        )

    def run(self, params={}):
        response = self.connection.client.delete_cve(params.get(Input.CVE_ID, []))
        return clean(
            {
                Output.SUCCESS_AMOUNT: response.get("success", {}).get("amount"),
                Output.FAILURE: response.get(Output.FAILURE),
            }
        )
