import komand
from .schema import FindFileByNameInput, FindFileByNameOutput
# Custom imports below
from googleapiclient.http import MediaIoBaseUpload
from apiclient import errors


class FindFileByName(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='find_file_by_name',
                description='Find a file ID',
                input=FindFileByNameInput(),
                output=FindFileByNameOutput())

    def run(self, params={}):
        filename_operator = params.get('filename_operator')
        filename = params.get('filename')
        parent_id = params.get('parent_id')

        if parent_id:
            if filename_operator == '=':
                response = self.connection.service.files().list(
                    q="name = '{name}' and ('{parent_id}' in parents)".format(name=filename, parent_id=parent_id),
                    spaces='drive', fields='files(id, name)').execute()
            elif filename_operator == '!=':
                response = self.connection.service.files().list(
                    q="name != '{name}' and ('{parent_id}' in parents)".format(name=filename, parent_id=parent_id),
                    spaces='drive', fields='files(id, name)').execute()
            else:
                response = self.connection.service.files().list(
                    q="name contains '{name}' and ('{parent_id}' in parents)".format(name=filename, parent_id=parent_id),
                    spaces='drive', fields='files(id, name)').execute()
        else:
            if filename_operator == '=':
                response = self.connection.service.files().list(q="name = '{name}'".format(name=filename),
                                                                spaces='drive', fields='files(id, name)').execute()
            elif filename_operator == '!=':
                response = self.connection.service.files().list(q="name != '{name}'".format(name=filename),
                                                                spaces='drive', fields='files(id, name)').execute()
            else:
                response = self.connection.service.files().list(q="name contains '{name}'".format(name=filename),
                                                                spaces='drive', fields='files(id, name)').execute()

        file_info = []
        for file in response.get('files', []):
            file_info.append({'file_name': file.get('name'), 'file_id': file.get('id')})
        return {'files_found': file_info}

    def test(self):
        # TODO: Implement test function
        return {}
