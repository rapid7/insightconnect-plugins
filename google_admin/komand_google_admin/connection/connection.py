import komand
from .schema import ConnectionSchema
# Custom imports below
import oauth2client.service_account
import apiclient
import httplib2


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        admin_user = params.get('admin_user')
        project_id = params.get('project_id')
        private_key_id = params.get('private_key_id')
        private_key = params.get('private_key').get('privateKey')
        client_email = params.get('client_email')
        client_id = params.get('client_id')
        client_x509_cert_url = params.get('client_x509_cert_url')
        auth_uri = params.get('auth_uri')
        token_uri = params.get('token_uri')
        auth_provider_x509_cert_url = params.get('auth_provider_x509_cert_url')

        # JSON that will be used to connect to Google
        auth = {'type': 'service_account', 'admin_user': admin_user, 'project_id': project_id,
                'private_key_id': private_key_id, 'private_key': private_key, 'client_email': client_email,
                'client_id': client_id, 'auth_uri': auth_uri, 'token_uri': token_uri,
                'auth_provider_x509_cert_url': auth_provider_x509_cert_url,
                'client_x509_cert_url': client_x509_cert_url}

        self.logger.info("Connecting %s as %s", client_email, admin_user)

        scopes = ['https://www.googleapis.com/auth/admin.directory.user',
                  'https://www.googleapis.com/auth/admin.directory.group']

        # Fix escaping issues in private_key
        if '\\n' in auth['private_key']:
            auth['private_key'] = auth['private_key'].replace('\\n', "\n", -1)

        # Build a Google credentials object
        credentials = oauth2client.service_account.ServiceAccountCredentials.from_json_keyfile_dict(
            auth, scopes=scopes)

        delegated_credentials = credentials.create_delegated(params['admin_user'])

        http = delegated_credentials.authorize(httplib2.Http())
        self.service = apiclient.discovery.build('admin', 'directory_v1', http=http)

        # run a quick test to ensure it works
        self.service.users().get(userKey=params['admin_user']).execute()
