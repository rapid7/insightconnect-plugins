import komand
from .schema import ConnectionSchema
from komand.exceptions import ConnectionTestException
# Custom imports below
from google.auth import exceptions
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
import gspread


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        admin_user = params.get('admin_user')
        private_key = params.get('private_key').get('privateKey')
        auth = params
        auth['private_key'] = private_key
        auth['type'] = 'service_account'
        del auth['admin_user']
        self.project = auth['project_id']

        scopes = ['https://www.googleapis.com/auth/drive']

        if admin_user:
            self.logger.info("Connecting to {email} as {admin}".format(email=auth['client_email'],
                                                                       admin=admin_user))
        else:
            self.logger.info("Connection to {} as service account".format(auth['client_email']))

        # Fix escaping issues in private_key
        if '\\n' in auth['private_key']:
            auth['private_key'] = auth['private_key'].replace('\\n', "\n", -1)

        # Build a Google credentials object
        if admin_user:
            try:
                credentials = service_account.Credentials.from_service_account_info(auth,
                                                                                    scopes=scopes,
                                                                                    subject=admin_user)
            except ValueError as e:
                raise e

        else:
            try:
                credentials = service_account.Credentials.from_service_account_info(auth, scopes=scopes)
            except ValueError:
                raise ConnectionTestException.Preset.API_KEY

        self.google_client = gspread.Client(auth=credentials)
        self.google_client.session = AuthorizedSession(credentials)

    def test(self):
        try:
            test = self.google_client.list_spreadsheet_files()
        except exceptions.RefreshError:
            raise ConnectionTestException.Preset.USERNAME_PASSWORD
        return test
