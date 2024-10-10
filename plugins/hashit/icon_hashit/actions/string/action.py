import hashlib

import insightconnect_plugin_runtime
from .schema import StringInput, StringOutput, Input, Output, Component


# Custom imports below
DEFAULT_ENCODING = "utf-8"


class String(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="string",
            description=Component.DESCRIPTION,
            input=StringInput(),
            output=StringOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        input_string = params.get(Input.STRING, "")
        # END INPUT BINDING - DO NOT REMOVE

        return {
            Output.MD5: hashlib.md5(input_string.encode(DEFAULT_ENCODING)).hexdigest(),  # nosec
            Output.SHA1: hashlib.sha1(input_string.encode(DEFAULT_ENCODING)).hexdigest(),  # nosec
            Output.SHA256: hashlib.sha256(input_string.encode(DEFAULT_ENCODING)).hexdigest(),
            Output.SHA512: hashlib.sha512(input_string.encode(DEFAULT_ENCODING)).hexdigest(),
        }
