import insightconnect_plugin_runtime

from .schema import DecompressBytesInput, DecompressBytesOutput, Component, Input, Output
from komand_compression.util import utils, decompressor
from komand_compression.util.constants import UTF_8
from base64 import b64encode, b64decode


class DecompressBytes(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="decompress_bytes",
            description=Component.DESCRIPTION,
            input=DecompressBytesInput(),
            output=DecompressBytesOutput(),
        )

    def run(self, params: dict = {}) -> dict:
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        file_bytes_b64 = params.get(Input.BYTES, "")
        # END INPUT BINDING - DO NOT REMOVE

        file_bytes = b64decode(file_bytes_b64)
        compression_type = utils.determine_compression_type(file_bytes)
        decompressed = decompressor.dispatch_decompress(
            algorithm=compression_type, file_bytes=file_bytes, logger=self.logger
        )
        return {Output.DECOMPRESSED: b64encode(decompressed).decode(UTF_8)}
