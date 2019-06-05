import komand
from .schema import DecompressBytesInput, DecompressBytesOutput
# Custom imports below
from ...util import utils, decompressor


class DecompressBytes(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='decompress_bytes',
                description='Decompress bytes',
                input=DecompressBytesInput(),
                output=DecompressBytesOutput())

    def run(self, params={}):
        file_bytes_b64 = params.get("bytes")  # Base64 encoded file as string
        self.logger.info("Run: Received base64 string: %s", file_bytes_b64)

        file_bytes = utils.base64_decode(file_bytes_b64)  # Decode base64 so we can manipulate the file

        compression_type = utils.determine_compression_type(file_bytes)  # Determine compression type
        decompressed= decompressor.dispatch_decompress(algorithm=compression_type, file_bytes=file_bytes)
        self.logger.info("Run: Decompressed file is: %s", type(decompressed))

        # Now re-encode the bytes in base64 so other plugins can use it
        decompressed_b64 = utils.base64_encode(decompressed)
        decompressed_b64_string = decompressed_b64.decode("utf-8")

        return {"decompressed": decompressed_b64_string}

    def test(self):
        # TODO: Implement test function
        return {}
