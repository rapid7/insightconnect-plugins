import sys
import os

from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_traceroute.actions.traceroute import Traceroute
from unittest.mock import patch, MagicMock


class TestTraceroute(TestCase):
    def setUp(self) -> None:
        self.action = Traceroute()
        self.action.logger = MagicMock()

    @parameterized.expand(
        [
            [
                # Default case, all params set, resolve_hostname True, set_ack False
                {
                    "host": "example.com",
                    "count": 5,
                    "max_ttl": 20,
                    "time_out": 2,
                    "set_ack": False,
                    "resolve_hostname": True,
                    "port": 443,
                },
                ["tcptraceroute", "-m", "20", "-q", "5", "-w", "2", "example.com", "443"],
            ],
            [
                # set_ack True, resolve_hostname True
                {
                    "host": "example.com",
                    "count": 5,
                    "max_ttl": 20,
                    "time_out": 2,
                    "set_ack": True,
                    "resolve_hostname": True,
                    "port": 443,
                },
                ["tcptraceroute", "-m", "20", "-q", "5", "-w", "2", "-A", "example.com", "443"],
            ],
            [
                # set_ack False, resolve_hostname False
                {
                    "host": "example.com",
                    "count": 5,
                    "max_ttl": 20,
                    "time_out": 2,
                    "set_ack": False,
                    "resolve_hostname": False,
                    "port": 443,
                },
                ["tcptraceroute", "-n", "-m", "20", "-q", "5", "-w", "2", "example.com", "443"],
            ],
            [
                # set_ack True, resolve_hostname False
                {
                    "host": "example.com",
                    "count": 5,
                    "max_ttl": 20,
                    "time_out": 2,
                    "set_ack": True,
                    "resolve_hostname": False,
                    "port": 443,
                },
                ["tcptraceroute", "-n", "-m", "20", "-q", "5", "-w", "2", "-A", "example.com", "443"],
            ],
            [
                # Edge case: count=0, max_ttl=0, time_out=0, port out of range
                {
                    "host": "example.com",
                    "count": 0,
                    "max_ttl": 0,
                    "time_out": 0,
                    "set_ack": False,
                    "resolve_hostname": True,
                    "port": 70000,
                },
                ["tcptraceroute", "-m", "30", "-q", "3", "-w", "3", "example.com", "80"],
            ],
            [
                # Edge case: port below range
                {
                    "host": "example.com",
                    "count": 1,
                    "max_ttl": 1,
                    "time_out": 1,
                    "set_ack": False,
                    "resolve_hostname": True,
                    "port": 0,
                },
                ["tcptraceroute", "-m", "1", "-q", "1", "-w", "1", "example.com", "80"],
            ],
        ]
    )
    @patch("subprocess.Popen")
    def test_command_construction(self, mocked_input, expected_cmd, mock_popen):
        process_mock = MagicMock()
        traceroute_output = b"traceroute to example.com (93.184.216.34), 30 hops max\n 1  192.168.1.1  1.123 ms\n 2  10.0.0.1  2.456 ms\n 3  93.184.216.34 open 3.789 ms\n"
        attrs = {"communicate.return_value": (traceroute_output, b""), "returncode": 0}
        process_mock.configure_mock(**attrs)
        mock_popen.return_value.__enter__.return_value = process_mock

        result = self.action.run(mocked_input)

        called_args = mock_popen.call_args.args[0]
        self.assertEqual(" ".join(expected_cmd), " ".join(called_args))

        # Assert the response is parsed correctly
        self.assertTrue(result["reply"])
        self.assertIn("open", result["response"])
        self.assertEqual(result["ip"], ["93.184.216.34", "192.168.1.1", "10.0.0.1", "93.184.216.34"])
        self.assertTrue(any("open" in line for line in result["path"]))

    def test_invalid_hostname_raises_exception(self):
        from insightconnect_plugin_runtime.exceptions import PluginException

        invalid_params = {
            "host": "!!!invalid!!!",
            "count": 1,
            "max_ttl": 1,
            "time_out": 1,
            "set_ack": False,
            "resolve_hostname": True,
            "port": 80,
        }
        with self.assertRaises(PluginException) as context:
            self.action.run(invalid_params)
        self.assertIn("Invalid hostname format", str(context.exception))
