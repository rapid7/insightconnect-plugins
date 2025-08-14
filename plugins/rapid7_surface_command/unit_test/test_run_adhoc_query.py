import logging
import os
import sys
from unittest import TestCase
from unittest.mock import Mock, patch

sys.path.append(os.path.abspath("../"))

from icon_rapid7_surface_command.util.api_connection import ApiConnection
from insightconnect_plugin_runtime.exceptions import PluginException
from requests import Response


class MockResponse:
    def __init__(self, status_code, json_data=None, text=None, content=None):
        self.status_code = status_code
        self.json_data = json_data
        self.text = text
        self.content = content


class TestRunAdhocQuery(TestCase):
    def setUp(self):
        self.api_key = "not_an_api_key"
        self.region = "us"
        self.logger = logging.getLogger("test")
        self.connection = ApiConnection(self.api_key, self.region, self.logger)
        self.cypher = "rapid7.insightplatform.compute_machines_without_vulnerability_scan"

    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_run_query_success(self, mock_request):
        # Mock a valid CSV response with two rows
        mock_response = Mock()
        mock_response.text = (
            'Name,Sources,Hostnames,"IP Address(es)"\n'
            'host-a,"Rapid7IVMAsset, Rapid7InsightVMAsset",a.example.com,"10.1.1.1, 10.1.1.2"\n'
            "host-b,Rapid7IVMAsset,b.example.com,10.2.2.2\n"
        )
        mock_request.return_value = mock_response

        result = self.connection.run_adhoc_query(self.cypher)

        self.assertIn("items", result)
        self.assertEqual(len(result["items"]), 2)

        row0 = result["items"][0]
        self.assertEqual(row0["Name"], "host-a")
        # Depending on parser settings, multi-value fields should be lists
        self.assertIn("IP Address(es)", row0)
        self.assertIsInstance(row0["IP Address(es)"], list)
        self.assertIn("10.1.1.1", row0["IP Address(es)"])

        mock_request.assert_called_once()

    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_run_query_api_exception(self, mock_request):
        error_response = Mock(spec=Response)
        error_response.status_code = 401
        error_response.content = b'{"error": "Invalid API key"}'
        type(error_response).text = Mock(return_value='{"error": "Invalid API key"}')

        mock_request.side_effect = PluginException(
            cause="API Authentication Failed",
            assistance="Please verify your API key is correct",
            data=error_response,
        )

        with self.assertRaises(PluginException) as context:
            self.connection.run_adhoc_query(self.cypher)

        self.assertEqual(context.exception.cause, "API Authentication Failed")
        self.assertEqual(
            context.exception.assistance, "Please verify your API key is correct"
        )

    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_run_query_malformed_response(self, mock_request):
        # Not real CSV; parser should yield zero rows, not raise
        mock_response = Mock()
        mock_response.text = "<html>oops</html>"
        mock_request.return_value = mock_response

        result = self.connection.run_adhoc_query(self.cypher)

        self.assertIn("items", result)
        self.assertEqual(result["items"], [])
        mock_request.assert_called_once()

    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_run_query_unprocessable_entity(self, mock_request):
        error_response = MockResponse(
            status_code=422, content=b'{"error": "Invalid query parameters"}'
        )

        mock_request.side_effect = PluginException(
            cause="Server was unable to process the request",
            assistance="Please validate the request to Rapid7 Surface Command",
            data=error_response,
        )

        with self.assertRaises(PluginException) as context:
            self.connection.run_adhoc_query(self.cypher)

        self.assertEqual(
            context.exception.cause, "Server was unable to process the request"
        )
        self.assertEqual(
            context.exception.assistance,
            "Please validate the request to Rapid7 Surface Command",
        )

    @patch("icon_rapid7_surface_command.util.api_connection.make_request")
    def test_run_query_timeout(self, mock_request):
        mock_request.side_effect = PluginException(
            cause="Request timed out",
            assistance="Please check your network connection or try again later",
        )

        with self.assertRaises(PluginException) as context:
            self.connection.run_adhoc_query(self.cypher)

        self.assertEqual(context.exception.cau
