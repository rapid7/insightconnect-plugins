import logging
import time
from unittest import TestCase
from unittest import mock

from komand.exceptions import PluginException, ConnectionTestException

from icon_azure_ad_admin.connection import Connection

TEST_TENANT = "FOOBARMICROSOFTUIDSTUFF"
TEST_API_TOKEN = "FLYYOUFOOLS"
TEST_APP_ID = "SOME_FAKE_ID"

TEST_CLIENT_SECRET = "client_secret"
TEST_CLIENT_ID = "client_id"


# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == f'https://login.microsoftonline.com/{TEST_TENANT}/oauth2/token':
        return MockResponse({"access_token": TEST_API_TOKEN}, 200)

    return MockResponse(None, 404)


def mocked_requests_get_fails(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code
            self.text = "Fatality"

        def json(self):
            return self.json_data

    return MockResponse(None, 404)


class TestConnection(TestCase):
    def setUp(self) -> None:
        self.params = {
            "application_id": TEST_CLIENT_ID,
            "application_secret": {
                "secretKey": TEST_CLIENT_SECRET
            },
            "tenant_id": TEST_TENANT
        }

    def tearDown(self) -> None:
        pass

    @mock.patch('requests.post', side_effect=mocked_requests_get)
    def test_can_connect(self, mock):
        self.connection = Connection()
        self.connection.logger = logging.getLogger("test_logger")
        self.connection.connect(self.params)

        self.assertEqual(self.connection.auth_token, TEST_API_TOKEN)

    @mock.patch('requests.post', side_effect=mocked_requests_get)
    def test_get_auth_token(self, mock):
        self.connection = Connection()
        self.connection.logger = logging.getLogger("test_logger")

        self.connection.time_ago = 100000
        self.connection.time_now = time.time()

        self.connection.app_secret = TEST_CLIENT_SECRET
        self.connection.app_id = TEST_APP_ID
        self.connection.tenant = TEST_TENANT

        token = self.connection.get_auth_token()

        self.assertEqual(token, TEST_API_TOKEN)

    @mock.patch('requests.post', side_effect=mocked_requests_get)
    def test_get_auth_token_under_one_hour(self, mock):
        self.connection = Connection()
        self.connection.logger = logging.getLogger("test_logger")

        self.connection.time_ago = time.time()
        self.connection.time_now = time.time()
        self.connection.auth_token = None

        self.connection.app_secret = TEST_CLIENT_SECRET
        self.connection.app_id = TEST_APP_ID
        self.connection.tenant = TEST_TENANT

        token = self.connection.get_auth_token()

        self.assertEqual(token, None)

    @mock.patch('requests.post', side_effect=mocked_requests_get_fails)
    def test_get_auth_fails(self, mock):
        self.connection = Connection()
        self.connection.logger = logging.getLogger("test_logger")

        self.connection.time_ago = 0
        self.connection.time_now = time.time()
        self.connection.auth_token = None

        self.connection.app_secret = TEST_CLIENT_SECRET
        self.connection.app_id = TEST_APP_ID
        self.connection.tenant = TEST_TENANT

        with self.assertRaises(PluginException):
            self.connection.get_auth_token()

    def test_connection_test(self):
        self.connection = Connection()
        self.connection.logger = logging.getLogger("test_logger")
        self.connection.auth_token = "this is a token"

        try:
            self.connection.test()
        except Exception:
            self.fail("Connection test failed!!!")

    def test_connection_test_failed(self):
        self.connection = Connection()
        self.connection.logger = logging.getLogger("test_logger")
        self.connection.auth_token = None

        with self.assertRaises(ConnectionTestException):
            self.connection.test()

    def test_get_headers(self):
        self.connection = Connection()
        self.connection.logger = logging.getLogger("test_logger")

        actual_val = self.connection.get_headers(TEST_API_TOKEN)

        expected_val = {'Authorization': 'Bearer FLYYOUFOOLS', 'Content-type': 'application/json'}

        self.assertEqual(actual_val, expected_val)
