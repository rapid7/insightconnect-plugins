import hashlib

import insightconnect_plugin_runtime
from .schema import StringInput, StringOutput, Input, Output, Component


# Custom imports below


class String(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='string',
            description=Component.DESCRIPTION,
            input=StringInput(),
            output=StringOutput())

    def run(self, params={}):
        md5 = hashlib.md5(params[Input.STRING].encode('utf-8')).hexdigest()  # nosec
        sha1 = hashlib.sha1(params[Input.STRING].encode('utf-8')).hexdigest()  # nosec
        sha256 = hashlib.sha256(params[Input.STRING].encode('utf-8')).hexdigest()
        sha512 = hashlib.sha512(params[Input.STRING].encode('utf-8')).hexdigest()

        hashes = {
            Output.MD5: md5,
            Output.SHA1: sha1,
            Output.SHA256: sha256,
            Output.SHA512: sha512,
        }

        return hashes
