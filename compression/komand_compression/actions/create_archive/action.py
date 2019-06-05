import komand
from .schema import CreateArchiveInput, CreateArchiveOutput
# Custom imports below
import os
import shutil
import tempfile
from ...util import utils, compressor


class CreateArchive(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_archive',
                description='Compress a files into archive',
                input=CreateArchiveInput(),
                output=CreateArchiveOutput())

    def run(self, params={}):
        algorithm = params.get("algorithm")
        fname = params.get("filename") if params.get("filename") != None else "compressed.%s"%("zip" if params.get("algorithm")== "zip" else "tar.gz")
        files = params.get("files")  # Base64 encoded file as string
        path = tempfile.mkdtemp()+"/"
        for f in files:
            with open(path+f["filename"],'w') as fi:
                fi.write(f["content"])
        compressed_file = compressor.dispatch_compress(algorithm=algorithm, file_bytes=None, tmpdir=path)
        self.logger.info("Run: Compressed file is: %s", compressed_file)

        # Now re-encode the bytes in base64 so other plugins can use it
        compressed_file_b64 = utils.base64_encode(compressed_file)
        compressed_file_b64_string = compressed_file_b64.decode("utf-8")
        self.logger.info("Run: Compressed file in base64 string is: %s", compressed_file_b64_string)
        
        shutil.rmtree(path)
        return {"archive": {"filename": fname,"content":compressed_file_b64_string}}

    def test(self):
        # TODO: Implement test function
        return {}
