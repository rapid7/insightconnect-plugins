import komand
from .schema import ConnectionSchema
# Custom imports below
from google.oauth2 import service_account


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

        scopes = ['https://www.googleapis.com/auth/cloud-platform']

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
            self.credentials = service_account.Credentials.from_service_account_info(auth,
                                                                                     scopes=scopes,
                                                                                     subject=admin_user)
        else:
            self.credentials = service_account.Credentials.from_service_account_info(auth)
