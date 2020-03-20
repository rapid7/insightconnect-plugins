import os

import komand
from komand.helper import encode_file
from .schema import GetFileInput, GetFileOutput, Input, Output, Component
# Custom imports below


class GetFile(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_file',
                description=Component.DESCRIPTION,
                input=GetFileInput(),
                output=GetFileOutput())

    def run(self, params={}):
        path = params.get(Input.FILE_PATH).lstrip('/')

        return {
            Output.FILE: {
                "content": encode_file(path).decode('UTF-8'),
                "filename": os.path.basename(path)
            }
        }
