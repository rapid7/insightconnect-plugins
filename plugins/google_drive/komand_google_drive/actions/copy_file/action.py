import insightconnect_plugin_runtime
from .schema import CopyFileInput, CopyFileOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from googleapiclient.errors import HttpError


class CopyFile(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="copy_file", description=Component.DESCRIPTION, input=CopyFileInput(), output=CopyFileOutput()
        )

    def run(self, params={}):
        file_id = params.get(Input.FILE_ID)
        folder_id = params.get(Input.FOLDER_ID)
        new_file_name=params.get(Input.NEW_FILE_NAME)
        try:
            metadata_body = clean({"name": new_file_name, "parents": [folder_id]})
            return {
                Output.RESULT: self.connection.service.files().copy(fileId=file_id, body=metadata_body, fields='id, parents', supportsAllDrives=True).execute()
            }
        except HttpError as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=str(error))