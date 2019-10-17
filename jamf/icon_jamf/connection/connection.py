import komand
from .schema import ConnectionSchema, Input

# Custom imports below
from komand.exceptions import ConnectionTestException
import requests
from requests.auth import HTTPBasicAuth


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.base_url = params.get(Input.URL, "")

        if not self.base_url.endswith('/'):
            self.base_url = f'{self.base_url}/'

        username = params[Input.CLIENT_LOGIN].get("username", "")
        password = params[Input.CLIENT_LOGIN].get("password", "")

        self.session = requests.Session()
        self.session.auth = HTTPBasicAuth(username, password)
        self.session.headers = {
                "Accept": "application/json"
            }

    def test(self):
        endpoint = 'JSSResource/users'
        url = f'{self.base_url}{endpoint}'

        result = self.session.get(url)

        if result.status_code != 200:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.INVALID_JSON, data=result.text)

        return {'connection': 'successful'}
