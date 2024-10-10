import insightconnect_plugin_runtime
import base64
import hashlib
from .schema import BytesInput, BytesOutput, Input, Output, Component


# Custom imports below


class Bytes(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="bytes",
            description=Component.DESCRIPTION,
            input=BytesInput(),
            output=BytesOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        input_bytes = base64.standard_b64decode(params.get(Input.BYTES, ""))
        # END INPUT BINDING - DO NOT REMOVE

        return {
            Output.MD5: hashlib.md5(input_bytes).hexdigest(),  # nosec
            Output.SHA1: hashlib.sha1(input_bytes).hexdigest(),  # nosec
            Output.SHA256: hashlib.sha256(input_bytes).hexdigest(),
            Output.SHA512: hashlib.sha512(input_bytes).hexdigest(),
        }
