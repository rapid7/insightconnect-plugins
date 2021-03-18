import insightconnect_plugin_runtime
from .schema import DecodeInput, DecodeOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
from urllib.parse import unquote


class Decode(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="decode",
            description=Component.DESCRIPTION,
            input=DecodeInput(),
            output=DecodeOutput(),
        )

    def run(self, params={}):
        input_url = params.get(Input.URL)
        errors = params.get(Input.ERRORS)

        try:
            result = self.decode_url(input_url, errors)
            return {Output.URL: result}
        except Exception as e:
            self.logger.error("An error has occurred while decoding ", e)
            raise PluginException(
                cause="Failed to decode because a valid encoded URL input was not provided.",
                assistance="If you would like continue to attempt to decode the input try setting the value of the error field to ignore errors or to replace the characters.",
                data=e,
            )

    def decode_url(self, input_url:str, errors:str) -> str:
        self.logger.info(f"Decoding: {input_url}")

        if errors.lower() in ["replace", "ignore"]:
            return unquote(input_url, errors=errors)
        else:
            return unquote(input_url)
