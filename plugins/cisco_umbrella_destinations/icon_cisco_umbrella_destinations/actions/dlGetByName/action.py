import insightconnect_plugin_runtime
from .schema import DlgetbynameInput, DlgetbynameOutput, Input, Output, Component


# Custom imports below


class Dlgetbyname(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="dlGetByName",
            description="Get destination list by name",
            input=DlgetbynameInput(),
            output=DlgetbynameOutput())

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        destination_list_name = params.get(Input.NAME)
        # END INPUT BINDING - DO NOT REMOVE
        result = self.connection.client.get_destination_lists().get("data", [])
        result = clean(result)
        result_list = []
        for destination_list in result:
            if destination_list.get("name") == destination_list_name:
                result_list += destination_list

        return {Output.DATA: result_list}
