import komand
from .schema import CreateFolderInput, CreateFolderOutput, Input, Output, Component

# Custom imports below
from googleapiclient.errors import HttpError


class CreateFolder(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_folder",
            description=Component.DESCRIPTION,
            input=CreateFolderInput(),
            output=CreateFolderOutput(),
        )

    def run(self, params={}):
        folder_metadata = {"name": params.get(Input.FOLDER_NAME), "mimeType": "application/vnd.google-apps.folder"}
        parent_folder_id = params.get(Input.PARENT_FOLDER_ID)
        if parent_folder_id:
            folder_metadata["parents"] = [parent_folder_id]

        try:
            result = self.connection.service.files().create(body=folder_metadata, fields="id").execute()
            return {Output.FOLDER_ID: result.get("id")}
        except HttpError as error:
            raise Exception("An error occurred: %s" % error)
