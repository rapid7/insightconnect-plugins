import insightconnect_plugin_runtime
from .schema import DlGetAllInput, DlGetAllOutput, Input, Output, Component
from typing import Any, Dict
from insightconnect_plugin_runtime.helper import clean
import logging


class DlGetAll(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="dlGetAll",
            description=Component.DESCRIPTION,
            input=DlGetAllInput(),
            output=DlGetAllOutput(),
        )

    def run(self, params={}):
        result = self.connection.client.get_destination_lists().get("data", [])
        result = clean(result)
        pre_output = []
        # The issue here is that I'm checking if each dl meets any of these requirements, not all of them
        for destination_list in result:
            if params.get(Input.ACCESS) is not None and destination_list.get("access") == params.get(Input.ACCESS):
                pre_output.append(destination_list)
            if params.get(Input.ISGLOBAL) is not None and destination_list.get("isGlobal") == params.get(
                    Input.ISGLOBAL):
                pre_output.append(destination_list)
            if params.get(Input.ISMSPDEFAULT) is not None and destination_list.get("isMspDefault") == params.get(Input.ISMSPDEFAULT):
                pre_output.append(destination_list)
            if params.get(Input.MARKEDFORDELETION) is not None and destination_list.get("markedForDeletion") == params.get(Input.MARKEDFORDELETION):
                pre_output.append(destination_list)
        logging.info("\n\n\nTHIS IS PRE_OUTPUT" + str(pre_output) + "\n\n\n")
        seen_id = set()
        output = []
        if pre_output:
            for destination_list in pre_output:
                if destination_list.get("id") not in seen_id:
                    output.append(destination_list)
                    seen_id.add(destination_list.get("id"))
        else:
            output = result
        return {Output.DATA: output}
