import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from freezegun import freeze_time
from icon_mimecast_v2.connection.connection import Connection
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from parameterized import parameterized

from util import STUB_CONNECTION, Util


@freeze_time("2000-01-07T00:00:00.000000Z")
class TestConnectionMonitorLogs(TestCase):
    @patch("requests.Session.send", side_effect=Util.mocked_request)
    def setUp(self, mock_request: MagicMock) -> None:
        self.task_connection = Connection()
        self.task_connection.logger = MagicMock()
        self.task_connection.connect(STUB_CONNECTION)

    @parameterized.expand(
        [
            (
                {"success": True},
                None,
                "The connection test to Mimecast was successful.",
            ),
            (
                {"success": True},
                "WARNING_TTP_URL",
                "WARNING: No required permission set to access log type: ttp_url. That log type will be skipped during ingestion.",
            ),
            (
                {"success": True},
                "WARNING_TTP_ATTACHMENT",
                "WARNING: No required permission set to access log type: ttp_attachment. That log type will be skipped during ingestion.",
            ),
            (
                {"success": True},
                "WARNING_TTP_IMPERSONATION",
                "WARNING: No required permission set to access log type: ttp_impersonation. That log type will be skipped during ingestion.",
            ),
        ]
    )
    @patch("requests.Session.send")
    def test_monitor_logs_connection_test_task(
        self,
        expected_data: Dict[str, Any],
        warning_type: str,
        expected_message: str,
        mock_request: MagicMock,
    ) -> None:
        mock_request.side_effect = lambda request, **kwargs: Util.mocked_request(request, type=warning_type, **kwargs)
        data, message = self.task_connection.test_task()
        self.assertDictEqual(expected_data, data)
        self.assertIn(expected_message, message)

    @patch("requests.Session.send")
    def test_monitor_logs_connection_test_task_error(
        self,
        mock_request: MagicMock,
    ) -> None:
        mock_request.side_effect = lambda request, **kwargs: Util.mocked_request(request, type="WARNING_ALL", **kwargs)

        with self.assertRaises(ConnectionTestException) as context:
            self.task_connection.test_task()
        self.assertIn(
            "Configured credentials do not have permission for this API endpoint.",
            context.exception.cause,
        )
        self.assertIn(
            "Please ensure credentials have required permissions.",
            context.exception.assistance,
        )

    @patch("requests.Session.send", side_effect=Util.mocked_request)
    def test_monitor_logs_connection_test(self, mock_request: MagicMock) -> None:
        data = self.task_connection.test()
        self.assertDictEqual(data, {"success": True})
