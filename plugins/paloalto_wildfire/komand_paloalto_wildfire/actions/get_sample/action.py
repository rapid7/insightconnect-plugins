# Custom imports below
import base64

import insightconnect_plugin_runtime

from .schema import GetSampleInput, GetSampleOutput, Input, Output


class GetSample(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_sample",
            description="Query for a sample file",
            input=GetSampleInput(),
            output=GetSampleOutput(),
        )

    def run(self, params={}):
        out = base64.b64encode(self.connection.client.get_sample(params.get(Input.HASH))).decode()
        return {Output.FILE: out}
