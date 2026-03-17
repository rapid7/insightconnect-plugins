import os
import sys
import unittest
from unittest.mock import MagicMock, Mock, patch

sys.path.append(os.path.abspath("../"))

import requests.exceptions
from icon_sqlmap.actions.scan import Scan
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema.validators import validate

from util import MockResponse, Util, mocked_requests_success


@patch("icon_sqlmap.util.api.Popen")
@patch("icon_sqlmap.util.api.validators.ipv4", return_value=True)
@patch("icon_sqlmap.util.api.time.sleep")
class TestScan(unittest.TestCase):
    def setUp(self) -> None:
        self.action = Scan()
        self.action = Util.default_connector(self.action)
        self.params = Util.load_parameters("scan_params.json.resp")

    @patch("icon_sqlmap.util.api.requests.request", side_effect=mocked_requests_success)
    def test_scan_success(
        self, mock_request: MagicMock, mock_sleep: MagicMock, mock_ipv4: MagicMock, mock_popen: MagicMock
    ) -> None:
        result = self.action.run(self.params)
        validate(result, self.action.output.schema)
        self.assertIn("result", result)
        self.assertIn("log", result["result"])
        self.assertEqual(len(result["result"]["log"]), 1)
        self.assertEqual(result["result"]["log"][0]["message"], "testing connection to the target URL")

    @patch("icon_sqlmap.util.api.requests.request")
    def test_scan_connection_error(
        self, mock_request: MagicMock, mock_sleep: MagicMock, mock_ipv4: MagicMock, mock_popen: MagicMock
    ) -> None:
        mock_request.side_effect = requests.exceptions.ConnectionError("Connection refused")
        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertIn("SQLMap scan failed", context.exception.cause)
        self.assertIn("Unable to connect", str(context.exception.data))

    @patch("icon_sqlmap.util.api.requests.request")
    def test_scan_http_error(
        self, mock_request: MagicMock, mock_sleep: MagicMock, mock_ipv4: MagicMock, mock_popen: MagicMock
    ) -> None:
        mock_request.return_value = MockResponse("task_new.json.resp", status_code=500)
        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertIn("SQLMap scan failed", context.exception.cause)
        self.assertIn("HTTP 500", str(context.exception.data))

    @patch("icon_sqlmap.util.api.requests.request")
    def test_scan_invalid_json(
        self, mock_request: MagicMock, mock_sleep: MagicMock, mock_ipv4: MagicMock, mock_popen: MagicMock
    ) -> None:
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.side_effect = ValueError("No JSON")
        mock_response.__enter__ = Mock(return_value=mock_response)
        mock_response.__exit__ = Mock(return_value=False)
        mock_request.return_value = mock_response
        with self.assertRaises(Exception):
            self.action.run(self.params)
