import insightconnect_plugin_runtime
from .schema import GetMemoryInput, GetMemoryOutput, Input, Output, Component
# Custom imports below
from ...util.util import Util


class GetMemory(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_memory",
            description=Component.DESCRIPTION,
            input=GetMemoryInput(),
            output=GetMemoryOutput(),
        )

    def run(self, params={}):
        task_id = params.get(Input.TASK_ID, "")
        pid = params.get(Input.PID, "")
        endpoint = f"memory/get/{task_id}/{pid}"
        response = self.connection.api.send(endpoint, _json=False)
        content = response.content
        return {Output.CONTENTS: Util.prepare_decoded_value(content)}
