from icon_bmc_remedy_itsm.connection import Connection
from unittest import TestCase, mock
import maya
import logging

class MockResponse():
    def __init__(self):
        self.text = "Success"

class MockSession():
    def post(*args, **kwargs):
        return MockResponse()

class MockRequests():
    def session(self):
        return MockSession()


class TestConnection(TestCase):

    @mock.patch('requests.session', side_effect=MockSession)
    def test_connection_token_expired(self, mockPost):
        conn = Connection()
        log = logging.getLogger("Test")

        conn.logger = log
        conn.last_jwt_time = maya.now().add(seconds=-3550)
        conn.url = "http://www.google.com"
        conn.auth_payload = {
            'username': 'username',
            'password': 'password'
        }

        actual = conn.make_headers_and_refresh_token()

        expected = {'Authorization': 'AR-JWT Success'}
        self.assertEqual(actual, expected)

    def test_connection_no_token_expired(self):
        conn = Connection()
        log = logging.getLogger("Test")

        conn.logger = log
        conn.last_jwt_time = maya.now()
        conn.url = "http://www.google.com"
        conn.jwt = "fake_token"
        conn.auth_payload = {
            'username': 'username',
            'password': 'password'
        }

        actual = conn.make_headers_and_refresh_token()

        expected = {'Authorization': "AR-JWT fake_token"}
        self.assertEqual(actual, expected)
