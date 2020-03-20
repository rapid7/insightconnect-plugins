import komand
import base64
import hashlib
from .schema import BytesInput, BytesOutput, Input, Output, Component


# Custom imports below


class Bytes(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='bytes',
            description=Component.DESCRIPTION,
            input=BytesInput(),
            output=BytesOutput())

    def run(self, params={}):
        raw = base64.standard_b64decode(params[Input.BYTES])
        md5 = hashlib.md5(raw).hexdigest()  # nosec
        sha1 = hashlib.sha1(raw).hexdigest()  # nosec
        sha256 = hashlib.sha256(raw).hexdigest()
        sha512 = hashlib.sha512(raw).hexdigest()

        hashes = {
            Output.MD5: md5,
            Output.SHA1: sha1,
            Output.SHA256: sha256,
            Output.SHA512: sha512,
        }
        return hashes
