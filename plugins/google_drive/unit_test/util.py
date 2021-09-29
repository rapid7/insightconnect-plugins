import logging
from komand_google_drive.connection.connection import Connection
from googleapiclient.errors import HttpError
import httplib2


def error_response(status, reason):
    headers = {"status": status, "content-type": "application/json"}
    response = httplib2.Response(headers)
    response.reason = reason
    return response


class MockClient:
    def __init__(self):
        self.service = "test"
        self.body = {}
        self.get_file_id = None
        self.update_file_id = None
        self.export_file_id = None
        self.query = None

    def files(self):
        return self

    def create(self, body, fields, media_body=None, supportsTeamDrives=None):
        self.body = body
        return self

    def export(self, fileId, mimeType):
        self.export_file_id = fileId
        return self

    def get(self, fileId, fields):
        self.get_file_id = fileId
        return self

    def list(self, q, spaces, fields):
        self.query = q
        return self

    def update(
        self, fileId, body=None, media_mime_type=None, media_body=None, fields=None, addParents=None, removeParents=None
    ):
        self.update_file_id = fileId
        return self

    def execute(self):
        if self.query == "name = 'File to find' and ('12345' in parents)":
            return {"files": [{"name": "File to find", "id": "98765"}]}
        elif self.query == "name != 'File to find' and ('12345' in parents)":
            return {"files": [{"name": "Another file", "id": "87654"}]}
        elif self.query == "name contains 'File' and ('12345' in parents)":
            return {"files": [{"name": "File to find", "id": "98765"}]}
        elif self.query == "name = 'File to find'":
            return {"files": [{"name": "File to find", "id": "98765"}]}
        elif self.query == "name = 'Not Found'":
            return {"files": []}
        elif self.export_file_id == "get_content":
            return b"\xef\xbb\xbfTest"
        elif self.export_file_id == "not_found":
            self.export_file_id = None
            raise HttpError(
                resp=error_response(404, "File not found"), content=b"File not found", uri="http://example.com"
            )
        elif self.body.get("name") == "New Folder":
            return {"id": "0BwwA4oUTeiV1TGRPeTVjaWRDY1E"}
        elif self.body.get("name") == "New Folder 2":
            return {"id": "0aWwC6yCVab22oS9iaa2WajYdR9o"}
        elif self.body.get("name") == "Folder Not Found":
            raise HttpError(
                resp=error_response(404, "Folder not found"), content=b"Folder not found", uri="http://example.com"
            )
        elif self.body.get("name") == "test.csv":
            return {"id": "1jizwcfNK7JqHtn9kszitKSCWVOborMV8"}
        elif self.body.get("name") == "test.txt":
            return {"id": "1pAT5CqVKi6XtyaD4betZvDQqOt8ZcuUR"}
        elif self.body.get("name") == "test":
            return {"id": "1SVa7eeArDtMWUsjdjm43yicgupzAEIoQ"}
        elif self.body.get("name") == "":
            return {"id": "1SVa7eeArDtMWUsjdjm43yicgupzAEIoQ"}
        elif self.body.get("name") == "upload.txt":
            return {"id": "upload_file"}
        elif self.body.get("name") == "upload.ppt":
            return {"id": "upload_file2"}
        elif self.body.get("name") == "upload.csv":
            return {"id": "upload_file3"}
        elif self.get_file_id == "1pAT5CqVKi6XtyaD4betZvDQqOt8ZcuUR":
            self.get_file_id = None
            return {"parents": ["1HJz7NbjASN8szc_MS1-BoDn_q4opJFmn"]}
        elif self.get_file_id == "File Not Found":
            self.get_file_id = None
            raise HttpError(
                resp=error_response(404, "File not found"), content=b"File not found", uri="http://example.com"
            )
        elif self.update_file_id == "1pAT5CqVKi6XtyaD4betZvDQqOt8ZcuUR":
            self.update_file_id = None
            return {"id": "1pAT5CqVKi6XtyaD4betZvDQqOt8ZcuUR", "parents": ["0BwwA4oUTeiV1TGRPeTVjaWRDY1E"]}
        elif self.update_file_id == "overwrite_1":
            return {"id": "overwrite_1"}
        elif self.update_file_id == "overwrite_2":
            return {"id": "overwrite_2"}
        elif self.update_file_id == "overwrite_3":
            return {"id": "overwrite_3"}
        elif self.update_file_id == "without_new_filename":
            return {"id": "without_new_filename"}
        elif self.update_file_id == "not_found":
            self.update_file_id = None
            raise HttpError(
                resp=error_response(404, "File not found"), content=b"File not found", uri="http://example.com"
            )

        self.body = {}
        self.get_file_id = None
        self.update_file_id = None
        self.export_file_id = None
        self.query = None


class MockConnection:
    def __init__(self):
        self.service = MockClient()


class Util:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        action.connection = MockConnection()
        action.logger = logging.getLogger("action logger")
        return action
