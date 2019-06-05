import komand
import github
import requests
from .schema import ConnectionSchema
# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.github_user = None
        self.user_data = ''
        self.user = None
        self.username = ''
        self.api_prefix = 'https://api.github.com'
        self.secret = None
        self.github_session = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")
        try:
            self.username = params.get('credentials').get("username")
            self.secret = params.get("credentials").get('password')
            self.basic_auth = (self.username, self.secret)
            self.github_session = requests.Session()
            self.github_user = github.Github(self.username, self.secret)
            user_info = self.github_user.get_user()
            self.user = self.github_user.get_user(self.username)
            self.github_session_user = requests.get(self.api_prefix, auth=(self.username, self.secret), verify=True)
            if str(self.github_session_user.status_code).startswith('2'):
                self.logger.info('Connect: Login successful')
            else:
                self.logger.info('Connect: Login unsuccessful')

        except github.GithubException as err:
            self.logger.error('Github: Connect: error %s', err.data)
            raise Exception('Github: Connect: user could not be authenticated please try again.')

        except requests.exceptions.RequestException as e:
            raise e

    def test(self):
        # connect handles the authentication
        return {}
