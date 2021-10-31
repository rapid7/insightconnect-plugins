import insightconnect_plugin_runtime
from .schema import GetFileContentsInput, GetFileContentsOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from googleapiclient.errors import HttpError
import base64


class GetFileContents(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_file_contents",
            description=Component.DESCRIPTION,
            input=GetFileContentsInput(),
            output=GetFileContentsOutput(),
        )

    def run(self, params={}):
        file_id = params.get(Input.FILE_ID)
        mime_type = params.get(Input.MIME_TYPE)

        try:
            response = self.connection.service.files().export(fileId=file_id, mimeType=mime_type).execute()
        except HttpError as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=str(error))

        _file = base64.b64encode(response).decode("UTF-8")
        return {Output.FILE: _file}
