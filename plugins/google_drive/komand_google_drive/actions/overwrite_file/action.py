import insightconnect_plugin_runtime
from .schema import OverwriteFileInput, OverwriteFileOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from io import BytesIO
from base64 import b64decode
from googleapiclient.http import MediaIoBaseUpload
from googleapiclient.errors import HttpError


class OverwriteFile(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="overwrite_file",
            description=Component.DESCRIPTION,
            input=OverwriteFileInput(),
            output=OverwriteFileOutput(),
        )

    def run(self, params={}):
        content = params.get(Input.CONTENT)
        file_id = params.get(Input.FILE_ID)
        new_file_name = params.get(Input.NEW_FILE_NAME)
        new_mime_type = params.get(Input.NEW_MIME_TYPE)

        file_bytes = BytesIO(b64decode(content))

        # Apply mime_type.
        mime_type = None
        if new_mime_type == "Docs":
            mime_type = "application/vnd.google-apps.document"
        if new_mime_type == "Sheets":
            mime_type = "application/vnd.google-apps.spreadsheet"
        if new_mime_type == "Slides":
            mime_type = "application/vnd.google-apps.presentation"

        if new_file_name:
            request_body = {"name": new_file_name, "mimeType": mime_type}
        else:
            request_body = {"mimeType": mime_type}

        try:
            # File's new content.
            media = MediaIoBaseUpload(file_bytes, mime_type, resumable=True)

            # Send the request to the API.
            updated_file = (
                self.connection.service.files()
                .update(
                    body=request_body,
                    fileId=file_id,
                    media_mime_type=mime_type,
                    media_body=media,
                )
                .execute()
            )

            return {Output.FILE_ID: updated_file.get("id")}
        except HttpError as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=str(error))
