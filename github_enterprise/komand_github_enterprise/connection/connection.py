import komand
from .schema import ConnectionSchema
# Custom imports below
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_prefix = None
        self.username = None
        self.secret = None
        self.enterprise = None
        self.host = None

    def connect(self, params={}):
        self.logger.info('Connect: Connecting')
        # init variables
        self.username = params.get('credentials').get('username')
        self.secret   = params.get('credentials').get('password')
        self.api_prefix = 'https://' + params.get('host') + '/api/v3'
        self.host = params.get('host')
        # login to github
        try:
            self.enterprise = requests.get(self.api_prefix, auth = (self.username, self.secret), verify=False)
            if str(self.enterprise.status_code).startswith('2'):
                self.logger.info('Connect: Login-in successful')
            else:
                self.logger.info('Connect: Login-in unsuccessful')
        except requests.exceptions.RequestException as e:
            raise e
