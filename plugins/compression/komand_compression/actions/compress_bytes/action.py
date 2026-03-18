import insightconnect_plugin_runtime

from .schema import CompressBytesInput, CompressBytesOutput, Component, Input, Output
from komand_compression.util import compressor
from komand_compression.util.constants import UTF_8
from base64 import b64encode, b64decode


class CompressBytes(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="compress_bytes",
            description=Component.DESCRIPTION,
            input=CompressBytesInput(),
            output=CompressBytesOutput(),
        )

    def run(self, params: dict = {}) -> dict:
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        algorithm = params.get(Input.ALGORITHM, "")
        file_bytes_b64 = params.get(Input.BYTES, "")
        # END INPUT BINDING - DO NOT REMOVE

        file_bytes = b64decode(file_bytes_b64)
        compressed = compressor.dispatch_compress(algorithm=algorithm, file_bytes=file_bytes)
        return {Output.COMPRESSED: b64encode(compressed).decode(UTF_8)}
