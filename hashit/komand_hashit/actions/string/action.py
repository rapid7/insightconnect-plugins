import komand
import hashlib
from .schema import StringInput, StringOutput
# Custom imports below


class String(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='string',
            description='Generate Hashes from Text',
            input=StringInput(),
            output=StringOutput())

    def run(self, params={}):
        md5    = hashlib.md5(params['string'].encode('utf-8')).hexdigest()
        sha1   = hashlib.sha1(params['string'].encode('utf-8')).hexdigest()
        sha256 = hashlib.sha256(params['string'].encode('utf-8')).hexdigest()
        sha512 = hashlib.sha512(params['string'].encode('utf-8')).hexdigest()

        hashes = {
            'md5': md5,
            'sha1': sha1,
            'sha256': sha256,
            'sha512': sha512,
        }

        return hashes

    def test(self, params={}):
        a = 'test'.encode("utf-8")
        # Hashes of 'test'
        real_hashes = {
            'md5': '098f6bcd4621d373cade4e832627b4f6',
            'sha1': 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3',
            'sha256': '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08',
            'sha512': 'ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff'
        }

        test_hashes={}
        test_hashes['md5']    = hashlib.md5(a).hexdigest()
        test_hashes['sha1']   = hashlib.sha1(a).hexdigest()
        test_hashes['sha256'] = hashlib.sha256(a).hexdigest()
        test_hashes['sha512'] = hashlib.sha512(a).hexdigest()

        # Test against correct hashes of string 'test'
        for alg in real_hashes:
            if test_hashes[alg] != real_hashes[alg]:
                raise Exception('Hash failed')

        return test_hashes
