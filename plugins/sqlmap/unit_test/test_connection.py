import os
import sys
import unittest
from unittest.mock import MagicMock, patch

sys.path.append(os.path.abspath("../"))

import requests.exceptions
from insightconnect_plugin_runtime.exceptions import ConnectionTestException

from util import Util, mocked_requests_success


@patch("icon_sqlmap.util.api.Popen")
@patch("icon_sqlmap.util.api.validators.ipv4", return_value=True)
@patch("icon_sqlmap.util.api.time.sleep")
class TestConnection(unittest.TestCase):
    def setUp(self) -> None:
        self.connection = Util.default_connector_connection()

    @patch("icon_sqlmap.util.api.requests.request", side_effect=mocked_requests_success)
    def test_connection_test_success(
        self, mock_request: MagicMock, mock_sleep: MagicMock, mock_ipv4: MagicMock, mock_popen: MagicMock
    ) -> None:
        result = self.connection.test()
        self.assertEqual(result, {"success": True})

    @patch("icon_sqlmap.util.api.requests.request")
    def test_connection_test_failure(
        self, mock_request: MagicMock, mock_sleep: MagicMock, mock_ipv4: MagicMock, mock_popen: MagicMock
    ) -> None:
        mock_request.side_effect = requests.exceptions.ConnectionError("Connection refused")
        with self.assertRaises(ConnectionTestException) as context:
            self.connection.test()
        self.assertIn("There was a problem with running the SQLMap server.", context.exception.cause)
