import insightconnect_plugin_runtime
from .schema import CreateFileInFolderInput, CreateFileInFolderOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from googleapiclient.http import MediaIoBaseUpload
from mimetypes import guess_type
from io import BytesIO
from base64 import b64decode
from googleapiclient.errors import HttpError


class CreateFileInFolder(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_file_in_folder",
            description=Component.DESCRIPTION,
            input=CreateFileInFolderInput(),
            output=CreateFileInFolderOutput(),
        )

    def run(self, params={}):
        filename = params.get(Input.FILE).get("filename")
        file_bytes = params.get(Input.FILE).get("content")
        file_metadata = {"name": filename, "parents": [params.get(Input.FOLDER_ID)]}

        mime_type = guess_type(filename)
        if mime_type and isinstance(mime_type, tuple):
            mime_type = mime_type[0]
        if not mime_type:
            mime_type = "text/plain"

        file_bytes = BytesIO(b64decode(file_bytes))
        media = MediaIoBaseUpload(file_bytes, mime_type, resumable=True)

        try:
            result = self.connection.service.files().create(body=file_metadata, media_body=media, fields="id").execute()
            return {Output.FILE_ID: result.get("id")}
        except HttpError as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=str(error))
