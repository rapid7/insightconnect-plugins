import komand
from .schema import ExtractArchiveInput, ExtractArchiveOutput
# Custom imports below
import copy
from ...util import utils, decompressor


class ExtractArchive(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='extract_archive',
                description='Exctract file archivee',
                input=ExtractArchiveInput(),
                output=ExtractArchiveOutput())

    def run(self, params={}):
        archive = params.get("archive")
        file_bytes_b64 = archive["content"]  # Base64 encoded file as string
        fname = archive["filename"]
        file_bytes = utils.base64_decode(file_bytes_b64)  # Decode base64 so we can manipulate the file

        compression_type = utils.determine_compression_type(file_bytes)  # Determine compression type
        decompressed_file = decompressor.dispatch_decompress(algorithm=compression_type, file_bytes=file_bytes)
        self.logger.info("Run: Decompressed file is: %s", type(decompressed_file))
        decompressed_file_b64_string={}
        return_array = []
        if isinstance(decompressed_file,dict):
            for fil in decompressed_file:
                decompressed_file_b64 = utils.base64_encode(decompressed_file[fil])
                decompressed_file_b64_string[fil.split("/")[-1]] = decompressed_file_b64.decode("utf-8")
            for key in decompressed_file_b64_string.keys():
                if key !=  fname:
                    return_array.append({"filename":key,"content":decompressed_file_b64_string[key]})
        else:
            decompressed_file_b64 = utils.base64_encode(decompressed_file)
            decompressed_file_b64_string = decompressed_file_b64.decode("utf-8")
            return_array.append({"filename":fname,"content":decompressed_file_b64_string})
        return {"files": return_array}

    def test(self):
        # TODO: Implement test function
        return {}

