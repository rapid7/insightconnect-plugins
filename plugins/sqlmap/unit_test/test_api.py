import os
import sys
import unittest
from subprocess import SubprocessError
from unittest.mock import MagicMock, patch

sys.path.append(os.path.abspath("../"))

import logging

from icon_sqlmap.util.api import SqlmapApi
from icon_sqlmap.util.constants import MAX_WAIT_FOR_COMPLETION_ITERATIONS
from insightconnect_plugin_runtime.exceptions import PluginException

from util import MockResponse


@patch("icon_sqlmap.util.api.requests.request")
@patch("icon_sqlmap.util.api.Popen")
@patch("icon_sqlmap.util.api.validators.ipv4", return_value=True)
@patch("icon_sqlmap.util.api.time.sleep")
class TestApi(unittest.TestCase):
    def setUp(self) -> None:
        self.logger = logging.getLogger("test")

    def _create_api(self) -> SqlmapApi:
        return SqlmapApi("127.0.0.1", "8775", self.logger)

    def test_create_task_success(
        self, mock_sleep: MagicMock, mock_ipv4: MagicMock, mock_popen: MagicMock, mock_request: MagicMock
    ) -> None:
        mock_request.return_value = MockResponse("task_new.json.resp")
        api = self._create_api()
        task_id = api._create_task()
        self.assertEqual(task_id, "a1b2c3d4e5f6")

    def test_create_task_no_taskid(
        self, mock_sleep: MagicMock, mock_ipv4: MagicMock, mock_popen: MagicMock, mock_request: MagicMock
    ) -> None:
        mock_request.return_value = MockResponse("task_new_empty.json.resp")
        api = self._create_api()
        with self.assertRaises(PluginException) as context:
            api._create_task()
        self.assertIn("Failed to create a new task", context.exception.cause)

    def test_wait_for_completion_success(
        self, mock_sleep: MagicMock, mock_ipv4: MagicMock, mock_popen: MagicMock, mock_request: MagicMock
    ) -> None:
        mock_request.return_value = MockResponse("scan_status_terminated.json.resp")
        api = self._create_api()
        api._wait_for_completion("a1b2c3d4e5f6")

    def test_wait_for_completion_timeout(
        self, mock_sleep: MagicMock, mock_ipv4: MagicMock, mock_popen: MagicMock, mock_request: MagicMock
    ) -> None:
        mock_request.return_value = MockResponse("scan_status_running.json.resp")
        api = self._create_api()
        with self.assertRaises(PluginException) as context:
            api._wait_for_completion("a1b2c3d4e5f6")
        self.assertIn("Scan timed out", context.exception.cause)
        status_calls = [call for call in mock_request.call_args_list if "status" in str(call)]
        self.assertEqual(len(status_calls), MAX_WAIT_FOR_COMPLETION_ITERATIONS)

    def test_validate_host_invalid(
        self, mock_sleep: MagicMock, mock_ipv4: MagicMock, mock_popen: MagicMock, mock_request: MagicMock
    ) -> None:
        mock_ipv4.return_value = False
        with self.assertRaises(PluginException) as context:
            SqlmapApi("not-an-ip", "8775", self.logger)
        self.assertIn("Invalid API host", context.exception.cause)

    def test_validate_port_invalid(
        self, mock_sleep: MagicMock, mock_ipv4: MagicMock, mock_popen: MagicMock, mock_request: MagicMock
    ) -> None:
        with self.assertRaises(PluginException) as context:
            SqlmapApi("127.0.0.1", "not_a_number", self.logger)
        self.assertIn("Invalid API port", context.exception.cause)

    def test_validate_port_out_of_range(
        self, mock_sleep: MagicMock, mock_ipv4: MagicMock, mock_popen: MagicMock, mock_request: MagicMock
    ) -> None:
        with self.assertRaises(PluginException) as context:
            SqlmapApi("127.0.0.1", "99999", self.logger)
        self.assertIn("API port out of range", context.exception.cause)

    def test_prepare_headers_default(
        self, mock_sleep: MagicMock, mock_ipv4: MagicMock, mock_popen: MagicMock, mock_request: MagicMock
    ) -> None:
        result = SqlmapApi._prepare_headers(None)
        self.assertEqual(result, {"Content-Type": "application/json"})

    def test_prepare_headers_empty(
        self, mock_sleep: MagicMock, mock_ipv4: MagicMock, mock_popen: MagicMock, mock_request: MagicMock
    ) -> None:
        result = SqlmapApi._prepare_headers({})
        self.assertEqual(result, {"Content-Type": "application/json"})

    def test_prepare_headers_custom(
        self, mock_sleep: MagicMock, mock_ipv4: MagicMock, mock_popen: MagicMock, mock_request: MagicMock
    ) -> None:
        result = SqlmapApi._prepare_headers({"X-Custom": "value"})
        self.assertEqual(result, {"X-Custom": "value"})

    def test_initialize_server_command_structure(
        self, mock_sleep: MagicMock, mock_ipv4: MagicMock, mock_popen: MagicMock, mock_request: MagicMock
    ) -> None:
        SqlmapApi("127.0.0.1", "8775", self.logger)
        mock_popen.assert_called_once()
        popen_call_arguments = mock_popen.call_args
        command = popen_call_arguments[0][0]
        self.assertIsInstance(command, list)
        self.assertEqual(command[0], "python")
        self.assertIn("sqlmapapi.py", command[1])
        self.assertNotIn("shell", popen_call_arguments[1] or {})

    def test_initialize_server_subprocess_error(
        self, mock_sleep: MagicMock, mock_ipv4: MagicMock, mock_popen: MagicMock, mock_request: MagicMock
    ) -> None:
        mock_popen.side_effect = SubprocessError("spawn failed")
        with self.assertRaises(PluginException):
            SqlmapApi("127.0.0.1", "8775", self.logger)

    def test_get_logs_reads_from_start(
        self, mock_sleep: MagicMock, mock_ipv4: MagicMock, mock_popen: MagicMock, mock_request: MagicMock
    ) -> None:
        api = self._create_api()
        api._logs.write("line 1\nline 2\n")
        api._logs.flush()
        api.get_logs()

    def test_get_logs_cleanup(
        self, mock_sleep: MagicMock, mock_ipv4: MagicMock, mock_popen: MagicMock, mock_request: MagicMock
    ) -> None:
        api = self._create_api()
        api._logs.write("some log data\n")
        api._logs.flush()
        api.get_logs(cleanup=True)
        api._logs.seek(0)
        self.assertEqual(api._logs.read(), "")
