import insightconnect_plugin_runtime
from .schema import GetPcapInput, GetPcapOutput, Input, Output

# Custom imports below
import requests
import base64


class GetPcap(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_pcap",
            description="Returns the content of the PCAP associated with the given task",
            input=GetPcapInput(),
            output=GetPcapOutput(),
        )

    def run(self, params={}):
        server = self.connection.server
        task_id = params.get(Input.TASK_ID, "")
        endpoint = f"{server}/pcap/get/{task_id}"

        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            ctype = response.headers.get("Content-Type", "")
            if (
                ctype.startswith("application/x-tar")
                or ctype.startswith("application/octet-stream")
                or ctype.startswith("application/json")
                or ctype.startswith("application/vnd.tcpdump.pcap")
            ):
                content = response.content
                return {Output.CONTENTS: base64.b64encode(content).decode("UTF-8")}

        except Exception as exception:
            self.logger.error(f"Error: {str(exception)}")
