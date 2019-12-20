import komand
from .schema import ConnectionSchema
# Custom imports below
import requests
from requests.auth import HTTPBasicAuth


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.session_id = None
        self.url = None
        self.s = requests.session()

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        username = params.get('credentials').get('username')
        password = params.get('credentials').get('password')
        try:
            self.url = params['url']
            auth_api = '/SecureSphere/api/v1/auth/session'
            auth_url = self.url + auth_api
            self.logger.info(auth_url)
            response = self.s.post(auth_url, auth=HTTPBasicAuth(username, password), verify=False)
            self.logger.info(response)
            sessionid = response.json()
            self.session_id = sessionid['session-id']
        except Exception:
            raise Exception("An error has occurred while connection")
