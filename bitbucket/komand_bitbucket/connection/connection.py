import komand
import requests
from komand.exceptions import ConnectionTestException
from .schema import ConnectionSchema, Input
# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.bucket_session = None
        self.username = None
        self.base_api = 'https://api.bitbucket.org/2.0'

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")
        try:
            self.username = params.get(Input.CREDENTIALS).get("username")
            # Create Session
            self.bucket_session = requests.Session()
            # self.bucket_session.headers.update({'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'})
            self.bucket_session.auth = (self.username, params.get(Input.CREDENTIALS).get("password"))
            user = self.bucket_session.get(self.base_api + '/user')
            user_obj = user.json()
            if user.status_code == 200:
                self.logger.info('Connect: ' + user_obj['username'] + ' Connected.')
            else:
                self.logger.info('Connect: Connection Failed')
        except requests.exceptions.RequestException as e:
            raise ConnectionTestException(cause='Connect: Connection Failed', data=e)

    def test(self):
        try:
            api_call = self.base_api + '/user'
            response = self.bucket_session.get(api_call)
            if response.status_code == 200:
                return {'status': 'API 2.0 connection test successful'}
        except requests.exceptions.RequestException:
            return {'status': 'Error'}
