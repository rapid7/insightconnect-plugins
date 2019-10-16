import komand
from .schema import ConnectionSchema
from komand.exceptions import ConnectionTestException
# Custom imports below
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        url = 'https://{}'.format(params.get("okta_url"))
        key = params.get("okta_key").get("secretKey")

        header = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'SSWS {}'.format(key),
        }

        self.session = requests.Session()
        self.session.headers.update(header)

        self.okta_url = url

    def test(self):
        response = self.session.get('{}/api/v1/groups'.format(self.okta_url))
        if response.status_code == 401:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY)
        if response.status_code == 404:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.NOT_FOUND)
        if response.status_code == range(500, 599):
            raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVER_ERROR)
        if response.status_code == 200:
            return {'Connection test successful': True}
        else:
            self.logger.error('Unknown error. Server response:{}'.format(response.text))
            raise ConnectionTestException(preset='Unknown error')
