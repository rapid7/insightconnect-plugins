import logging
import os
import sys
from unittest import TestCase
from unittest.mock import Mock, patch

sys.path.append(os.path.abspath("../"))

from icon_rapid7_surface_command.util.surface_command.api_connection import ApiConnection
from insightconnect_plugin_runtime.exceptions import APIException, PluginException


class TestRunQuery(TestCase):
    def setUp(self):
        self.api_key = "not_an_api_key"
        self.region = "United States"
        self.logger = logging.getLogger("test")
        self.connection = ApiConnection(self.api_key, self.region, self.logger)
        self.query_id = "test_query_id"

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

        # Verify request parameters
        args, kwargs = mock_request.call_args
        self.assertEqual(kwargs["timeout"], 90)
        self.assertEqual(args[0].method, "post")
        self.assertEqual(args[0].json, {"query_id": self.query_id})
        self.assertEqual(args[0].headers, {"X-Api-Key": self.api_key})

    @patch("icon_rapid7_surface_command.util.surface_command.api_connection.make_request")
    def test_run_query_plugin_exception(self, mock_request):
        # Setup mock to raise PluginException
        mock_exception = PluginException(
            cause="Test plugin exception",
            assistance="Please check your input"
        )
        mock_request.side_effect = mock_exception

        # Execute and assert exception is raised
        with self.assertRaises(PluginException) as context:
            self.connection.run_query(self.query_id)

        self.assertEqual(context.exception.cause, "Test plugin exception")

    @patch("icon_rapid7_surface_command.util.surface_command.api_connection.make_request")
    def test_run_query_api_exception(self, mock_request):
        # Setup mock response with error status
        mock_response = Mock()
        mock_response.text = "Error processing request"
        mock_response.status_code = 422

        # Create a plugin exception with response data
        plugin_exc = PluginException(
            cause="Server was unable to process the request",
            assistance="Please validate the request to Rapid7 Surface Command",
            data=mock_response
        )
        mock_request.side_effect = plugin_exc

        # Execute and assert APIException is raised
        with self.assertRaises(APIException) as context:
            self.connection.run_query(self.query_id)

        self.assertEqual(context.exception.status_code, 422)
        self.assertEqual(context.exception.data, "Error processing request")
