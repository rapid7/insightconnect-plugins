import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException

from icon_rapid7_cyber_grc.connection.connection import Connection
from icon_rapid7_cyber_grc.connection.schema import Input
from util import API_KEY, BASE_URL, MockResponse, Util


@patch("requests.Session.request", side_effect=Util.mock_request)
class TestConnection(TestCase):
    def test_connect_builds_a_client_with_the_api_key_header(self, mock_request):
        connection = Util.default_connector(Connection()).connection

        self.assertEqual(connection.client.url, BASE_URL)
        self.assertEqual(connection.client.session.headers.get("X-API-Key"), API_KEY)

    def test_connect_trims_a_trailing_slash_from_the_url(self, mock_request):
        connection = Connection()
        connection.logger = Util.default_connector(Connection()).logger
        connection.connect({Input.URL: f"{BASE_URL}/", Input.API_KEY: {"secretKey": API_KEY}, Input.SSL_VERIFY: True})

        self.assertEqual(connection.client.url, BASE_URL)

    def test_test_succeeds_when_the_api_answers(self, mock_request):
        connection = Util.default_connector(Connection()).connection

        self.assertEqual(connection.test(), {"success": True})

    def test_test_raises_a_connection_test_exception_when_the_key_is_rejected(self, mock_request):
        connection = Util.default_connector(Connection()).connection
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(401, {"error": "unauthorized"})

        with self.assertRaises(ConnectionTestException) as context:
            connection.test()

        self.assertEqual(context.exception.cause, "Unauthorized.")
