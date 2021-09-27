import insightconnect_plugin_runtime
from .schema import UploadFileInput, UploadFileOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from googleapiclient.errors import HttpError
from io import BytesIO
from base64 import b64decode
from googleapiclient.http import MediaIoBaseUpload


class UploadFile(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="upload_file",
            description=Component.DESCRIPTION,
            input=UploadFileInput(),
            output=UploadFileOutput(),
        )

    def run(self, params={}):
        filename = params.get(Input.FILE).get("filename")
        file_bytes = params.get(Input.FILE).get("content")
        file_type = params.get(Input.GOOGLE_FILE_TYPE)
        folder_id = params.get(Input.FOLDER_ID)

        # Apply mime_type. Set mime_type to unknown by default. will allow for additions to this action later
        mime_type = "application/vnd.google-apps.unknown"
        if file_type == "Docs":
            mime_type = "application/vnd.google-apps.document"
        if file_type == "Sheets":
            mime_type = "application/vnd.google-apps.spreadsheet"
        if file_type == "Slides":
            mime_type = "application/vnd.google-apps.presentation"

        file_bytes = BytesIO(b64decode(file_bytes))

        media = MediaIoBaseUpload(file_bytes, "file/Komand", resumable=True)
        if folder_id:
            file_metadata = {"name": filename, "mimeType": mime_type, "parents": [folder_id]}
        else:
            file_metadata = {"name": filename, "mimeType": mime_type}

        try:
            new_file = (
                self.connection.service.files()
                .create(
                    body=file_metadata,
                    media_body=media,
                    supportsTeamDrives=True,
                    fields="id",
                )
                .execute()
                .get("id")
            )
        except HttpError as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=str(error))

        url = "https://docs.google.com"
        if file_type == "Docs":
            url = f"{url}/document/d/{new_file}"
        if file_type == "Sheets":
            url = f"{url}/spreadsheets/d/{new_file}"
        if file_type == "Slides":
            url = f"{url}/presentation/d/{new_file}"

        return {Output.FILE_ID: new_file, Output.FILE_LINK: url}
