import insightconnect_plugin_runtime
from .schema import DlGetAllInput, DlGetAllOutput, Input, Output, Component
from typing import Any, Dict
from insightconnect_plugin_runtime.helper import clean


# Custom imports below


def filtering(result: list, input_key: str, input_value: any, pre_output: list):
    for destination_list in result:
        if destination_list.get(input_key) == input_value:
            pre_output.append(destination_list)


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
        pre_output = []
        if Input.ACCESS:
            filtering(result, "access", Input.ACCESS, pre_output)
        if Input.ISGLOBAL:
            filtering(result, "is_global", Input.ISGLOBAL, pre_output)
        if Input.ISMSPDEFAULT:
            filtering(result, "is_msp_default", Input.ISMSPDEFAULT, pre_output)
        if Input.MARKEDFORDELETION:
            filtering(result, "marked_for_deletion", Input.MARKEDFORDELETION, pre_output)

        seen_names = set()
        output = []
        if pre_output:
            for dl in pre_output:
                if dl.get("name") not in seen_names:
                    output.append(dl)
                    seen_names.add(dl.get("name"))

            return {Output.DATA: output}
        else:
            return {Output.DATA: result}
