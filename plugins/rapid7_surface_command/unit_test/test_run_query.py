import logging
import os
import sys
from unittest import TestCase
from unittest.mock import Mock, patch

sys.path.append(os.path.abspath("../"))

from icon_rapid7_surface_command.util.surface_command.api_connection import ApiConnection
from insightconnect_plugin_runtime.exceptions import APIException, PluginException
from requests import Response


class TestRunQuery(TestCase):
    def setUp(self):
        self.api_key = "not_an_api_key"
        self.region = "United States"
        self.logger = logging.getLogger("test")
        self.connection = ApiConnection(self.api_key, self.region, self.logger)
        self.query_id = "rapid7.insightplatform.compute_machines_without_vulnerability_scan"

    @patch("icon_rapid7_surface_command.util.surface_command.api_connection.make_request")
    def test_run_query_success(self, mock_request):
        # Setup mock response
        mock_response = Mock()
        expected_data = {"results": ["test_result_1", "test_result_2"]}
        mock_response.json.return_value = expected_data
        mock_request.return_value = mock_response

        # Execute the method
        result = self.connection.run_query(self.query_id)

        # Assert results
        self.assertEqual(result, expected_data)
        mock_request.assert_called_once()

    @patch("icon_rapid7_surface_command.util.surface_command.api_connection.make_request")
    def test_run_query_api_exception(self, mock_request):
        # Setup mock to raise PluginException
        error_response = Mock(spec=Response)
        error_response.status_code = 401
        error_response._content = b'{"error": "Invalid API key"}'
        # Mock the text property correctly
        type(error_response).text = Mock(return_value='{"error": "Invalid API key"}')

        mock_request.side_effect = PluginException(
            cause="API Authentication Failed",
            assistance="Please verify your API key is correct",
            data=error_response
        )

        # Execute the method and check for exception
        with self.assertRaises(PluginException) as context:
            self.connection.run_query(self.query_id)

        # Verify the PluginException details
        self.assertEqual(context.exception.cause, "API Authentication Failed")
        self.assertEqual(context.exception.assistance, "Please verify your API key is correct")

    @patch("icon_rapid7_surface_command.util.surface_command.api_connection.make_request")
    def test_run_query_malformed_response(self, mock_request):
        # Setup mock response with malformed JSON
        mock_response = Mock()
        mock_response.json.side_effect = ValueError("Invalid JSON")
        mock_request.return_value = mock_response

        # Execute the method and check for exception
        with self.assertRaises(ValueError):
            self.connection.run_query(self.query_id)

    @patch("icon_rapid7_surface_command.util.surface_command.api_connection.make_request")
    def test_run_query_unprocessable_entity(self, mock_request):
        # Setup mock for 422 error
        error_response = Response()
        error_response.status_code = 422
        error_response._content = b'{"error": "Invalid query parameters"}'

        mock_request.side_effect = PluginException(
            cause="Server was unable to process the request",
            assistance="Please validate the request to Rapid7 Surface Command",
            data=error_response
        )

        # Execute the method and check for exception
        with self.assertRaises(PluginException) as context:
            self.connection.run_query(self.query_id)

        # Verify exception details
        self.assertEqual(context.exception.cause, "Server was unable to process the request")
