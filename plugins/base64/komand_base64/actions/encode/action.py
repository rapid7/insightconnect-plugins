import base64

import insightconnect_plugin_runtime

from komand_base64.util.constants import DEFAULT_ENCODING

from .schema import Component, EncodeInput, EncodeOutput, Input, Output


class Encode(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="encode",
            description=Component.DESCRIPTION,
            input=EncodeInput(),
            output=EncodeOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        content = params.get(Input.CONTENT, "").encode(DEFAULT_ENCODING)
        # END INPUT BINDING - DO NOT REMOVE

        result = base64.standard_b64encode(content)
        return {Output.DATA: result.decode(DEFAULT_ENCODING)}
