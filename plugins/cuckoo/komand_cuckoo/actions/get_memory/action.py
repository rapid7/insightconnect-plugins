import insightconnect_plugin_runtime
from .schema import GetMemoryInput, GetMemoryOutput, Input, Output

# Custom imports below
import requests
import base64


class GetMemory(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_memory",
            description="Returns one memory dump file associated with the specified task ID",
            input=GetMemoryInput(),
            output=GetMemoryOutput(),
        )

    def run(self, params={}):
        server = self.connection.server
        task_id = params.get(Input.TASK_ID, "")
        pid = params.get(Input.PID, "")
        endpoint = f"{server}/memory/get/{task_id}/{pid}"

        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            if response.headers.get("Content-Type", "").startswith("application/octet-stream"):
                content = response.content
                return {Output.CONTENTS: base64.b64encode(content).decode("UTF-8")}
            else:
                response = response.json()
                return response

        except Exception as exception:
            self.logger.error(f"Error: {str(exception)}")
