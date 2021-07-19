import insightconnect_plugin_runtime
from .schema import EncodeInput, EncodeOutput, Input, Output, Component
import base64


class Encode(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="encode",
            description=Component.DESCRIPTION,
            input=EncodeInput(),
            output=EncodeOutput(),
        )

    def run(self, params={}):
        string = params[Input.CONTENT].encode("utf-8")
        result = base64.standard_b64encode(string)
        return {Output.DATA: result.decode("utf-8")}
