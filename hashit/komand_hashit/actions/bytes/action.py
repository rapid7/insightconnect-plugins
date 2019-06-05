import komand
import base64
import hashlib
from .schema import BytesInput, BytesOutput
# Custom imports below


class Bytes(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='bytes',
            description='Generate Hashes from File Bytes',
            input=BytesInput(),
            output=BytesOutput())

    def run(self, params={}):
        raw = base64.standard_b64decode(params['bytes'])
        md5    = hashlib.md5(raw).hexdigest()
        sha1   = hashlib.sha1(raw).hexdigest()
        sha256 = hashlib.sha256(raw).hexdigest()
        sha512 = hashlib.sha512(raw).hexdigest()

        hashes = {
            'md5': md5,
            'sha1': sha1,
            'sha256': sha256,
            'sha512': sha512,
        }
        return hashes


    def test(self, params={}):
        # base64 encoded file of 'test\n'
        f = 'dGVzdAo='
        raw = base64.standard_b64decode(f)
        # Hashes of file
        real_hashes = {
            'md5': 'd8e8fca2dc0f896fd7cb4cb0031ba249',
            'sha1': '4e1243bd22c66e76c2ba9eddc1f91394e57f9f83',
            'sha256': 'f2ca1bb6c7e907d06dafe4687e579fce76b37e4e93b7605022da52e6ccc26fd2',
            'sha512': '0e3e75234abc68f4378a86b3f4b32a198ba301845b0cd6e50106e874345700cc6663a86c1ea125dc5e92be17c98f9a0f85ca9d5f595db2012f7cc3571945c123'
        }

        test_hashes={}
        test_hashes['md5']    = hashlib.md5(raw).hexdigest()
        test_hashes['sha1']   = hashlib.sha1(raw).hexdigest()
        test_hashes['sha256'] = hashlib.sha256(raw).hexdigest()
        test_hashes['sha512'] = hashlib.sha512(raw).hexdigest()

        # Test against correct hashes of string 'test'
        for alg in real_hashes:
            if test_hashes[alg] != real_hashes[alg]:
                raise Exception('Hash failed')

        return test_hashes
