import komand
from .schema import ConnectionSchema, Input
# Custom imports below
from google.oauth2 import service_account
import apiclient
import json


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        secret_key = params.get(Input.CREDENTIALS_FILE_CONTENTS)
        auth_file_contents = json.loads(secret_key.get('secretKey'))

        self.logger.info(f"Contents Loaded: {type(auth_file_contents)}")
        self.logger.info(f"Logging in as: {auth_file_contents.get('client_email')}")

        # Build a Google credentials object
        credentials = service_account.Credentials.from_service_account_info(auth_file_contents)

        # Connect to Google Drive
        self.drive_service = apiclient.discovery.build('drive', 'v3', credentials=credentials)
        self.doc_service = apiclient.discovery.build('docs', 'v1', credentials=credentials)

    def test(self):
        self.drive_service.files().list().execute()
