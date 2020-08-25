import insightconnect_plugin_runtime
from .schema import GetFileInfoInput, GetFileInfoOutput, Input, Output, Component
# Custom imports below
import filetype
import base64


class GetFileInfo(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_file_info',
                description=Component.DESCRIPTION,
                input=GetFileInfoInput(),
                output=GetFileInfoOutput())

    def run(self, params={}):
        file = params.get(Input.FILE)
        kind = filetype.guess(base64.decodebytes(file.encode("utf-8")))
        if kind is None:
            extension = "unknown"
        else:
            extension = kind.extension

        return {
            Output.FILE_SIZE: self.size(file),
            Output.FILE_TYPE: extension
        }

    @staticmethod
    def size(file: str) -> int:
        return int((len(file) * 3) / 4) - file.count('=', -2)
