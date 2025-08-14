import logging
import os
import sys
from unittest import TestCase
from unittest.mock import Mock, patch

sys.path.append(os.path.abspath("../"))

from icon_rapid7_surface_command.util.api_connection import ApiConnection
from icon_rapid7_surface_command.connection.connection import Connection
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
from requests import Response


class MockResponse:
    def __init__(self, status_code, json_data=None, text=None, content=None):
        self.status_code = status_code
        self.json_data = json_data
        self.text = text
        self.content = content


class TestConnection(TestCase):
    @patch("icon_rapid7_surface_command.connection.connection.ApiConnection")
    def test_test_converts_pluginexception_to_connectiontestexception(self, MockApiConnection):
        # Arrange: connect with minimal params; ApiConnection is patched
        conn = Connection()
        params = {"api_key": {"secretKey": "fake"}, "region": "us"}
        conn.connect(params)

        # Make the underlying API call raise PluginException
        MockApiConnection.return_value.run_query.side_effect = PluginException(
            cause="API Authentication Failed",
            assistance="Please verify your API key is correct",
        )

        # Act / Assert: Connection.test should convert to ConnectionTestException
        with self.assertRaises(ConnectionTestException) as ctx:
            conn.test()

        self.assertIn("Connection test failed:", str(ctx.exception))


class TestRunAdhocQuery(TestCase):
    def setUp(self):
        self.api_key = "not_an_api_key"
        self.region = "us"
        self.logger = logging.getLogger("test")
        self.connection = ApiConnection(self.api_key, self.region, self.logger)
        self.cypher = "rapid7.insightplatform.compute_machines_without_vulnerability_scan"

    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_run_query_success(self, mock_request):
        # Valid CSV with two data rows
        mock_response = Mock()
        mock_response.text = (
            'Name,Sources,Hostnames,"IP Address(es)"\n'
            'host-a,"Rapid7IVMAsset, Rapid7InsightVMAsset",a.example.com,"10.1.1.1, 10.1.1.2"\n'
            "host-b,Rapid7IVMAsset,b.example.com,10.2.2.2\n"
        )
        mock_request.return_value = mock_response

        result = self.connection.run_adhoc_query(self.cypher)

        # ApiConnection returns a bare list of dicts
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["Name"], "host-a")
        # No auto-splitting: value remains a string
        self.assertEqual(result[0]["IP Address(es)"], "10.1.1.1, 10.1.1.2")

        mock_request.assert_called_once()

    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_run_query_api_exception(self, mock_request):
        error_response = Response()
        error_response.status_code = 401
        error_response._content = b'{"error": "Invalid API key"}'
        error_response.encoding = "utf-8"

        mock_request.side_effect = PluginException(
            cause="API Authentication Failed",
            assistance="Please verify your API key is correct",
            data=error_response,
        )

        with self.assertRaises(PluginException) as ctx:
            self.connection.run_adhoc_query(self.cypher)

        self.assertEqual(ctx.exception.cause, "API Authentication Failed")
        self.assertEqual(ctx.exception.assistance, "Please verify your API key is correct")

    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_run_query_malformed_response(self, mock_request):
        # Not real CSV; DictReader will produce zero rows
        mock_response = Mock()
        mock_response.text = "<html>oops</html>"
        mock_request.return_value = mock_response

        result = self.connection.run_adhoc_query(self.cypher)

        self.assertIsInstance(result, list)
        self.assertEqual(result, [])
        mock_request.assert_called_once()

    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_run_query_unprocessable_entity(self, mock_request):
        # When data is NOT a requests.Response, PluginException is re-raised
        error_response = MockResponse(
            status_code=422,
            content=b'{"error": "Invalid query parameters"}',
        )

        mock_request.side_effect = PluginException(
            cause="Server was unable to process the request",
            assistance="Please validate the request to Rapid7 Surface Command",
            data=error_response,
        )

        with self.assertRaises(PluginException) as ctx:
            self.connection.run_adhoc_query(self.cypher)

        self.assertEqual(ctx.exception.cause, "Server was unable to process the request")
        self.assertEqual(ctx.exception.assistance, "Please validate the request to Rapid7 Surface Command")

    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_run_query_timeout(self, mock_request):
        mock_request.side_effect = PluginException(
            cause="Request timed out",
            assistance="Please check your network connection or try again later",
        )

        with self.assertRaises(PluginException) as ctx:
            self.connection.run_adhoc_query(self.cypher)

        self.assertEqual(ctx.exception.cause, "Request timed out")
        self.assertEqual(ctx.exception.assistance, "Please check your network connection or try again later")

    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_run_query_server_error(self, mock_request):
        error_response = Response()
        error_response.status_code = 500
        error_response._content = b'{"error": "Internal Server Error"}'
        error_response.encoding = "utf-8"

        mock_request.side_effect = PluginException(
            cause="Server Error",
            assistance="An unexpected error occurred on the server. Please try again later or contact support.",
            data=error_response,
        )

        with self.assertRaises(PluginException) as ctx:
            self.connection.run_adhoc_query(self.cypher)

        self.assertEqual(ctx.exception.cause, "Server Error")
        self.assertEqual(
            ctx.exception.assistance,
            "An unexpected error occurred on the server. Please try again later or contact support.",
        )

    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_run_query_empty_response(self, mock_request):
        # Header-only CSV -> no data rows => []
        mock_response = Mock()
        mock_response.text = 'Name,Sources,Hostnames,"IP Address(es)"\n'
        mock_request.return_value = mock_response

        result = self.connection.run_adhoc_query(self.cypher)

        self.assertIsInstance(result, list)
        self.assertEqual(result, [])
        mock_request.assert_called_once()
