import json
import logging

from icon_intsights.connection import Connection
from icon_intsights.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {
                Input.ACCOUNT_ID: {'secretKey': 'account_id'},
                Input.API_KEY: {'secretKey': 'api_key'}
            }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename):
        with open(filename) as my_file:
            return my_file.read()

    @staticmethod
    def mock_request(*args, **kwargs):
        class MockResponse:
            def __init__(self, status_code: int, filename: str = None):
                self.status_code = status_code
                self.text = ''
                self.filename = filename

            def json(self):
                return json.loads(Util.read_file_to_string(f'payloads/{self.filename}.json.resp'))

        if kwargs.get('url') == 'https://api.intsights.com/public/v1/test-credentials' \
                and kwargs.get('auth').username == 'wrong':
            return MockResponse(401)
        elif kwargs.get('url') == 'https://api.intsights.com/public/v1/test-credentials':
            return MockResponse(200)
        elif kwargs.get(
                'url') == 'https://api.intsights.com/public/v1/public/v2/iocs/ioc-by-value?iocValue=example.com':
            return MockResponse(200, 'iocs_ioc-by-value')
        elif kwargs.get('url') == 'https://api.intsights.com/public/v1/public/v2/iocs/ioc-by-value?iocValue=empty':
            return MockResponse(204)
        else:
            raise NotImplementedError('Not implemented')
