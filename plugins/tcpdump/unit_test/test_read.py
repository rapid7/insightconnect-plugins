import base64
import os
import subprocess
import sys
from typing import Any, Dict, List

from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, mock_open, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_tcpdump.actions.read import Read
from komand_tcpdump.actions.read.schema import Input, Output

from utils import Util

VALID_PCAP = base64.b64encode(
    b"\xd4\xc3\xb2\xa1\x02\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\x00\x00\x01\x00\x00\x00"
).decode()


class TestRead(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(Read())
        # Common mock setup can be moved here
        self.mock_path_instance = MagicMock()
        self.mock_path_instance.is_file.return_value = True

    @patch("komand_tcpdump.actions.read.action.subprocess.run")
    @patch("builtins.open", new_callable=mock_open)
    @patch("komand_tcpdump.actions.read.action.Path")
    def test_read_success(self, mock_path: MagicMock, mock_file: MagicMock, mock_subprocess: MagicMock) -> None:
        # Setup mocks
        mock_path.return_value = self.mock_path_instance
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_result.stdout = b"15:30:00.000000 IP 10.0.0.1 > 10.0.0.2: ICMP echo request\n"
        mock_result.stderr = b""
        mock_subprocess.return_value = mock_result

        # Run action
        result = self.action.run({Input.PCAP: VALID_PCAP})

        # Assertions
        self.assertIn(Output.DUMP_CONTENTS, result)
        self.assertIn(Output.DUMP_FILE, result)
        self.assertIn(Output.STDERR, result)
        self.assertIsInstance(result[Output.DUMP_CONTENTS], list)
        self.assertGreater(len(result[Output.DUMP_CONTENTS]), 0)

    @parameterized.expand(
        [
            ("with_options", {Input.PCAP: VALID_PCAP, Input.OPTIONS: "-v -n"}, ["-v", "-n"]),
            ("with_filter", {Input.PCAP: VALID_PCAP, Input.FILTER: "tcp port 80"}, ["tcp port 80"]),
        ]
    )
    @patch("komand_tcpdump.actions.read.action.subprocess.run")
    @patch("builtins.open", new_callable=mock_open)
    @patch("komand_tcpdump.actions.read.action.Path")
    def test_read_with_params(
        self,
        name: str,
        input_params: Dict[str, Any],
        expected_args: List[str],
        mock_path: MagicMock,
        mock_file: MagicMock,
        mock_subprocess: MagicMock,
    ) -> None:
        # Setup mocks
        mock_path.return_value = self.mock_path_instance
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_result.stdout = b"packet data\n"
        mock_result.stderr = b""
        mock_subprocess.return_value = mock_result

        # Run action
        result = self.action.run(input_params)

        self.assertIn(Output.DUMP_CONTENTS, result)
        # Verify subprocess was called with expected args
        call_args = mock_subprocess.call_args[0][0]
        for arg in expected_args:
            self.assertIn(arg, call_args)

    def test_read_invalid_base64(self) -> None:
        # Run action with invalid base64 and verify exception
        with self.assertRaises(PluginException):
            self.action.run({Input.PCAP: "not-valid-base64!!!"})

    @patch("komand_tcpdump.actions.read.action.subprocess.run")
    @patch("builtins.open", new_callable=mock_open)
    @patch("komand_tcpdump.actions.read.action.Path")
    def test_read_tcpdump_failure(self, mock_path: MagicMock, mock_file: MagicMock, mock_subprocess: MagicMock) -> None:
        # Setup mocks
        mock_path.return_value = self.mock_path_instance
        mock_result = MagicMock()
        mock_result.returncode = 1
        mock_result.stdout = b""
        mock_result.stderr = b"tcpdump: invalid pcap file"
        mock_subprocess.return_value = mock_result

        # Run action and verify exception
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.PCAP: VALID_PCAP})
        self.assertEqual(context.exception.cause, "Tcpdump execution failed")
        self.assertIn("tcpdump: invalid pcap file", context.exception.assistance)

    @patch("komand_tcpdump.actions.read.action.subprocess.run")
    @patch("builtins.open", new_callable=mock_open)
    @patch("komand_tcpdump.actions.read.action.Path")
    def test_read_subprocess_timeout(
        self, mock_path: MagicMock, mock_file: MagicMock, mock_subprocess: MagicMock
    ) -> None:
        mock_path.return_value = self.mock_path_instance
        mock_subprocess.side_effect = subprocess.TimeoutExpired(cmd="tcpdump", timeout=300)
        with self.assertRaises(subprocess.TimeoutExpired):
            self.action.run({Input.PCAP: VALID_PCAP})

    @parameterized.expand(
        [
            ("invalid_options", {Input.OPTIONS: "--invalid-option"}, "Invalid tcpdump option. "),
            ("dangerous_options", {Input.OPTIONS: "-v; rm -rf /"}, "Invalid options provided. "),
            ("options_too_long", {Input.OPTIONS: "a" * 501}, "Options string too long. "),
            ("filter_too_long", {Input.FILTER: "tcp and " * 200}, "Filter expression too long. "),
            ("dangerous_filter", {Input.FILTER: "tcp && echo malicious"}, "Invalid filter expression. "),
        ]
    )
    def test_read_validation_errors(self, name: str, extra_params: Dict[str, str], expected_cause: str) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.PCAP: VALID_PCAP, **extra_params})
        self.assertEqual(context.exception.cause, expected_cause)
