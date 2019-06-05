import komand
from .schema import UploadFileInput, UploadFileOutput
# Custom imports below
from io import BytesIO
from base64 import b64decode
from googleapiclient.http import MediaIoBaseUpload


class UploadFile(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='upload_file',
                description='Upload a file to Google Drive',
                input=UploadFileInput(),
                output=UploadFileOutput())

    def run(self, params={}):
        filename = params.get('file').get('filename')
        file_bytes = params.get('file').get('content')
        file_type = params.get('google_file_type')
        folder_id = params.get('folder_id')

        # Apply mime_type. Set mime_type to unknown by default. will allow for additions to this action later
        mime_type = 'application/vnd.google-apps.unknown'
        if file_type == 'Docs':
            mime_type = 'application/vnd.google-apps.document'
        if file_type == 'Sheets':
            mime_type = 'application/vnd.google-apps.spreadsheet'
        if file_type == 'Slides':
            mime_type = 'application/vnd.google-apps.presentation'

        file_bytes = BytesIO(b64decode(file_bytes))

        media = MediaIoBaseUpload(file_bytes, 'file/Komand', resumable=True)
        if folder_id:
            file_metadata = {'name': filename, 'mimeType': mime_type,
                             'parents': [folder_id]}
        else:
            file_metadata = {'name': filename, 'mimeType': mime_type}

        newfile = self.connection.service.files().create(body=file_metadata, media_body=media,
                                                         supportsTeamDrives=True, fields='id',).execute().get('id')

        url = 'https://docs.google.com'
        if file_type == 'Docs':
            url = url + '/document/d/' + newfile
        if file_type == 'Sheets':
            url = url + '/spreadsheets/d/' + newfile
        if file_type == 'Slides':
            url = url + '/presentation/d/' + newfile

        return {'file_id': newfile, 'file_link': url}

    def test(self):
        # TODO: Implement test function
        return {}
