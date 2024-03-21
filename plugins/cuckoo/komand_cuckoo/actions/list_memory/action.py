from typing import List

import insightconnect_plugin_runtime
from .schema import ListMemoryInput, ListMemoryOutput, Input, Component, Output


class ListMemory(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_memory",
            description=Component.DESCRIPTION,
            input=ListMemoryInput(),
            output=ListMemoryOutput(),
        )

    def run(self, params={}):
        task_id = params.get(Input.TASK_ID, "")
        endpoint = f"memory/list/{task_id}"
        response = self.connection.api.send(endpoint)
        if not isinstance(response, List):
            response = response.get("dump_files", [])
        return {Output.DUMP_FILES: response}
