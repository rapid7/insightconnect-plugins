import insightconnect_plugin_runtime
from .schema import DlFilterAllInput, DlFilterAllOutput, Input, Output, Component
from insightconnect_plugin_runtime.helper import clean


class DlFilterAll(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="dlFilterAll", description=Component.DESCRIPTION, input=DlFilterAllInput(), output=DlFilterAllOutput()
        )

    def run(self, params={}):
        result = self.connection.client.get_destination_lists().get("data", [])
        result = clean(result)

        access = params.get(Input.ACCESS)
        is_global = params.get(Input.ISGLOBAL)
        msp_default = params.get(Input.ISMSPDEFAULT)
        deletion = params.get(Input.MARKEDFORDELETION)

        values = [access, is_global, msp_default, deletion]
        value_names = ["access", "isGlobal", "isMspDefault", "markedForDeletion"]

        output = []

        # Goes through each destination list and checks if all filters match
        for destination_list in result:
            all_right = False
            for (value, value_name) in zip(values, value_names):
                if value == destination_list.get(value_name) or value is None:
                    all_right = True
                else:
                    all_right = False
                    break
            if all_right:
                output.append(destination_list)

        return {Output.DATA: output}
