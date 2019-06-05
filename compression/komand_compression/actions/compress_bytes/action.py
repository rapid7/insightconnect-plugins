import komand
from .schema import CompressBytesInput, CompressBytesOutput
# Custom imports below
from ...util import utils, compressor


class CompressBytes(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='compress_bytes',
                description='Compress bytes',
                input=CompressBytesInput(),
                output=CompressBytesOutput())

    def run(self, params={}):
        algorithm = params.get("algorithm")
        file_bytes_b64 = params.get("bytes")  # Base64 encoded file as string
        self.logger.info("Run: Will compress %s with %s", file_bytes_b64, algorithm)

        file_bytes = utils.base64_decode(file_bytes_b64)  # Decode base64 so we can manipulate the file

        compressed = compressor.dispatch_compress(algorithm=algorithm, file_bytes=file_bytes)
        self.logger.info("Run: Compressed file is: %s", compressed)
        # Now re-encode the bytes in base64 so other plugins can use it
        compressed_b64 = utils.base64_encode(compressed)
        compressed_b64_string = compressed_b64.decode("utf-8")
        self.logger.info("Run: Compressed file in base64 string is: %s", compressed_b64_string)

        return {"compressed": compressed_b64_string}

    def test(self):
        """TODO: Test action"""
        return {}