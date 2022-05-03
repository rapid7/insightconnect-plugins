# Custom imports below
import base64

import insightconnect_plugin_runtime

from .schema import GetSampleInput, GetSampleOutput, Input, Output, Component


class GetSample(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_sample",
            description=Component.DESCRIPTION,
            input=GetSampleInput(),
            output=GetSampleOutput(),
        )

    def run(self, params={}):
        return {Output.FILE: base64.b64encode(self.connection.client.get_sample(params.get(Input.HASH))).decode()}
