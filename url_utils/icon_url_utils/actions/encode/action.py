import insightconnect_plugin_runtime
from .schema import EncodeInput, EncodeOutput, Input, Output, Component
from urllib.parse import quote


class Encode(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="encode",
            description=Component.DESCRIPTION,
            input=EncodeInput(),
            output=EncodeOutput(),
        )

    def run(self, params={}):
        input_url = params.get(Input.URL)
        result = quote(input_url)

        return {Output.URL: result}
