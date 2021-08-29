import logging
from komand_google_drive.connection.connection import Connection
from googleapiclient.errors import HttpError


class MockClient:
    def __init__(self):
        self.service = "test"
        self.body = {}
        self.get_file_id = None
        self.update_file_id = None

    def files(self):
        return self

    def create(self, body, fields, media_body=None):
        self.body = body
        return self

    def get(self, fileId, fields):
        self.get_file_id = fileId
        return self

    def update(self, fileId, fields, addParents, removeParents):
        self.update_file_id = fileId
        return self

    def execute(self):
        if self.body.get("name") == "New Folder":
            return {"id": "0BwwA4oUTeiV1TGRPeTVjaWRDY1E"}
        elif self.body.get("name") == "New Folder 2":
            return {"id": "0aWwC6yCVab22oS9iaa2WajYdR9o"}
        elif self.body.get("name") == "Folder Not Found":
            raise HttpError("Not Found")
        elif self.body.get("name") == "test.csv":
            return {"id": "1jizwcfNK7JqHtn9kszitKSCWVOborMV8"}
        elif self.body.get("name") == "test.txt":
            return {"id": "1pAT5CqVKi6XtyaD4betZvDQqOt8ZcuUR"}
        elif self.body.get("name") == "test":
            return {"id": "1SVa7eeArDtMWUsjdjm43yicgupzAEIoQ"}
        elif self.body.get("name") == "":
            return {"id": "1SVa7eeArDtMWUsjdjm43yicgupzAEIoQ"}
        elif self.get_file_id == "1pAT5CqVKi6XtyaD4betZvDQqOt8ZcuUR":
            self.get_file_id = None
            return {"parents": ["1HJz7NbjASN8szc_MS1-BoDn_q4opJFmn"]}
        elif self.get_file_id == "File Not Found":
            self.get_file_id = None
            raise HttpError("Not Found")
        elif self.update_file_id == "1pAT5CqVKi6XtyaD4betZvDQqOt8ZcuUR":
            self.update_file_id = None
            return {"id": "1pAT5CqVKi6XtyaD4betZvDQqOt8ZcuUR", "parents": ["0BwwA4oUTeiV1TGRPeTVjaWRDY1E"]}

        self.body = {}
        self.get_file_id = None
        self.update_file_id = None


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
