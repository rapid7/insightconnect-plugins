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
