import insightconnect_plugin_runtime
from .schema import DecodeInput, DecodeOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
import base64


class Decode(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="decode",
            description=Component.DESCRIPTION,
            input=DecodeInput(),
            output=DecodeOutput(),
        )

    def run(self, params={}):
        try:
            data = params.get(Input.BASE64)
            errors = params.get(Input.ERRORS)
            result = base64.standard_b64decode(data)
            if errors in ["replace", "ignore"]:
                return {Output.DATA: result.decode("utf-8", errors=errors)}
            else:
                return {Output.DATA: result.decode("utf-8")}
        except Exception as e:
            self.logger.error("An error has occurred while decoding ", e)
            raise PluginException(
                cause="Failed to decode because valid base64 input was not provided.",
                assistance="If you would like continue to attempt to decode the input try setting the value of the error field to ignore errors or to replace the characters.",
                data=e,
            )
