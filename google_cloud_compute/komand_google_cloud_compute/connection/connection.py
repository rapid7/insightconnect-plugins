import komand
from .schema import ConnectionSchema
# Custom imports below
from oauth2client.service_account import ServiceAccountCredentials


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")
        version = params.get("version", "v1")
        project_id = params.get("project_id", "")
        server  = params.get("host", "https://www.googleapis.com/compute/")
        server += version

        scopes = ['https://www.googleapis.com/auth/compute']

        creds = {
            "type": "service_account",
        }

        if '\\n' in params.get('private_key').get('privateKey'):
            params.get['private_key'] = params.get('private_key').get('privateKey').replace('\\n', "\n", -1)

        creds.update(params)

        self.logger.debug("Using credentials=%s", params)

        credentials = ServiceAccountCredentials.from_json_keyfile_dict(
            creds, scopes=scopes)

        token = credentials.get_access_token().access_token

        if token is "":
            self.logger.info('Connect: Unauthenticated API will be used')

        self.server  = server
        self.token   = token
        self.project_id = project_id
