import insightconnect_plugin_runtime
from .schema import FindFileByNameInput, FindFileByNameOutput, Input, Output, Component

# Custom imports below


class FindFileByName(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="find_file_by_name",
            description=Component.DESCRIPTION,
            input=FindFileByNameInput(),
            output=FindFileByNameOutput(),
        )

    def run(self, params={}):
        filename_operator = params.get(Input.FILENAME_OPERATOR)
        filename = params.get(Input.FILENAME)
        parent_id = params.get(Input.PARENT_ID)

        if parent_id:
            query = f"name {filename_operator} '{filename}' and ('{parent_id}' in parents)"
        else:
            query = f"name {filename_operator} '{filename}'"

        response = self.connection.service.files().list(q=query, spaces="drive", fields="files(id, name)").execute()
        file_info = []
        for file in response.get("files", []):
            file_info.append({"file_name": file.get("name"), "file_id": file.get("id")})
        return {Output.FILES_FOUND: file_info}
