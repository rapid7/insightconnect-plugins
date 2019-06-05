import komand
import requests
from .schema import ConnectionSchema
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
            self.username = params.get("credentials").get("username")
            # Create Session
            self.bucket_session = requests.Session()
            # self.bucket_session.headers.update({'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'})
            self.bucket_session.auth = (self.username, params.get("credentials").get("password"))
            user = self.bucket_session.get(self.base_api + '/user')
            user_obj = user.json()
            if user.status_code == 200:
                self.logger.info('Connect: ' + user_obj['username'] + ' Connected.')
            else:
                self.logger.info('Connect: Connection Failed')
        except requests.exceptions.RequestException as e:
            raise e
