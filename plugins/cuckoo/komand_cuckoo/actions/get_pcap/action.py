import insightconnect_plugin_runtime
from .schema import GetPcapInput, GetPcapOutput, Input, Output, Component
# Custom imports below
from ...util.util import Util


class GetPcap(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_pcap",
            description=Component.DESCRIPTION,
            input=GetPcapInput(),
            output=GetPcapOutput(),
        )

    def run(self, params={}):
        task_id = params.get(Input.TASK_ID, "")
        endpoint = f"pcap/get/{task_id}"
        response = self.connection.api.send(endpoint, _json=False)
        content = response.content
        return {Output.CONTENTS: Util.prepare_decoded_value(content)}
