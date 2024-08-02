import base64

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from komand_base64.util.constants import DEFAULT_ENCODING

from .schema import Component, DecodeInput, DecodeOutput, Input, Output


class Decode(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="decode",
            description=Component.DESCRIPTION,
            input=DecodeInput(),
            output=DecodeOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        data = params.get(Input.BASE64, "")
        errors = params.get(Input.ERRORS, "")
        # END INPUT BINDING - DO NOT REMOVE

        try:
            result = base64.standard_b64decode(data)
            if errors in ["replace", "ignore"]:
                return {Output.DATA: result.decode(DEFAULT_ENCODING, errors=errors)}
            else:
                return {Output.DATA: result.decode(DEFAULT_ENCODING)}
        except Exception as error:
            self.logger.error("An error has occurred while decoding ", error)
            raise PluginException(
                cause="Failed to decode because valid base64 input was not provided.",
                assistance="If you would like continue to attempt to decode the input try setting the value of the error field to ignore errors or to replace the characters.",
                data=error,
            )
