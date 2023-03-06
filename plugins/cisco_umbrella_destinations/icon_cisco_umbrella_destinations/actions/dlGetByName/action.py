import insightconnect_plugin_runtime
from .schema import DlGetByNameInput, DlGetByNameOutput, Input, Output, Component

# Custom imports below


class DlGetByName(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="dlGetByName", description=Component.DESCRIPTION, input=DlGetByNameInput(), output=DlGetByNameOutput()
        )

    def run(self, params={}):
        destination_list_name = params.get(Input.NAME)
        result = self.connection.client.get_destination_lists().get("data", [])
        result = clean(result)
        result_list = []
        for destination_list in result:
            if destination_list.get("name") == destination_list_name:
                result_list += destination_list

        return {Output.DATA: result_list}
