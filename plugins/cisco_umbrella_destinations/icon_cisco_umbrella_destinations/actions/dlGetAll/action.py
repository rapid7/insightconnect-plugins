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

        access = params.get(Input.ACCESS)
        is_global = params.get(Input.ISGLOBAL)
        msp_default = params.get(Input.ISMSPDEFAULT)
        deletion = params.get(Input.MARKEDFORDELETION)

        output = []
        for destination_list in result:
            access_right = False
            is_global_right = False
            msp_default_right = False
            deletion_right = False
            if destination_list.get("access") == access or access is None:
                access_right = True
            if destination_list.get("isGlobal") == is_global or is_global is None:
                is_global_right = True
            if destination_list.get("isMspDefault") == msp_default or msp_default is None:
                msp_default_right = True
            if destination_list.get("markedForDeletion") == deletion or deletion is None:
                deletion_right = True
            if access_right and is_global_right and msp_default_right and deletion_right:
                output.append(destination_list)

        return {Output.DATA: output}
