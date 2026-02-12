import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from komand_ping.actions.ping import Ping
from komand_ping.actions.ping.schema import Input, Output

from insightconnect_plugin_runtime.exceptions import PluginException

from util import Util


class _FakeCompletedProcess:
    """Minimal subprocess.CompletedProcess stand-in for unit tests."""

    def __init__(self, args, *, stdout="", stderr="", returncode=0):
        self.args = args
        self.stdout = stdout
        self.stderr = stderr
        self.returncode = returncode


LINUX_PING_SUCCESS = (
    "PING example.com (0.0.0.0) 56(84) bytes of data.\n"
    "64 bytes from 0.0.0.0: icmp_seq=1 ttl=56 time=10.1 ms\n\n"
    "--- example.com ping statistics ---\n"
    "4 packets transmitted, 4 received, 0% packet loss, time 3002ms\n"
    "rtt min/avg/max/mdev = 9.900/10.100/10.300/0.200 ms\n"
)


class TestPing(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(Ping())

    def _run_factory(self, *, stdout="", stderr="", returncode=0, capture_calls=False):
        calls = []

        def _factory(args, **kwargs):
            if capture_calls:
                calls.append({"args": args, "kwargs": kwargs})
            return _FakeCompletedProcess(args, stdout=stdout, stderr=stderr, returncode=returncode)

        return _factory, calls

    def test_run_success_linux_output_parsing(self):
        run_factory, _ = self._run_factory(stdout=LINUX_PING_SUCCESS, returncode=0)
        with patch("komand_ping.actions.ping.action.subprocess.run", side_effect=run_factory):
            result = self.action.run({Input.HOST: "example.com", Input.COUNT: 4, Input.RESOLVE_HOSTNAME: True})

        self.assertTrue(result[Output.REPLY])
        self.assertIn("ping statistics", result[Output.RESPONSE])
        self.assertEqual(result[Output.PACKETS_TRANSMITTED], 4)
        self.assertEqual(result[Output.PACKETS_RECEIVED], 4)
        self.assertEqual(result[Output.PACKETS_PERCENT_LOST], 0.0)
        self.assertEqual(result[Output.MINIMUM_LATENCY], "9.900ms")
        self.assertEqual(result[Output.AVERAGE_LATENCY], "10.100ms")
        self.assertEqual(result[Output.MAXIMUM_LATENCY], "10.300ms")
        self.assertEqual(result[Output.STANDARD_DEVIATION], "0.200ms")

    def test_run_uses_no_resolve_flag_when_resolve_hostname_false(self):
        run_factory, calls = self._run_factory(stdout=LINUX_PING_SUCCESS, returncode=0, capture_calls=True)
        with patch("komand_ping.actions.ping.action.subprocess.run", side_effect=run_factory):
            result = self.action.run({Input.HOST: "example.com", Input.COUNT: 2, Input.RESOLVE_HOSTNAME: False})

        self.assertEqual(len(calls), 1)
        argv = calls[0]["args"]
        self.assertEqual(argv[0], "ping")
        self.assertIn("-n", argv)
        self.assertIn("-c", argv)
        self.assertEqual(argv[-1], "example.com")

        self.assertTrue(result[Output.REPLY])
        self.assertEqual(result[Output.PACKETS_TRANSMITTED], 4)
        self.assertEqual(result[Output.PACKETS_RECEIVED], 4)

    def test_run_defaults_count_to_4_when_count_is_zero(self):
        run_factory, calls = self._run_factory(stdout=LINUX_PING_SUCCESS, returncode=0, capture_calls=True)
        with patch("komand_ping.actions.ping.action.subprocess.run", side_effect=run_factory):
            result = self.action.run({Input.HOST: "example.com", Input.COUNT: 0, Input.RESOLVE_HOSTNAME: True})

        self.assertEqual(len(calls), 1)
        argv = calls[0]["args"]
        self.assertEqual(argv[0], "ping")
        self.assertEqual(argv[1:3], ["-c", "4"])
        self.assertEqual(argv[-1], "example.com")

        self.assertTrue(result[Output.REPLY])
        self.assertEqual(result[Output.PACKETS_TRANSMITTED], 4)
        self.assertEqual(result[Output.PACKETS_RECEIVED], 4)

    def test_run_rc_1_or_2_returns_reply_false(self):
        run_factory, _ = self._run_factory(stdout="no reply\n", returncode=1)
        with patch("komand_ping.actions.ping.action.subprocess.run", side_effect=run_factory):
            result = self.action.run({Input.HOST: "example.com", Input.COUNT: 1, Input.RESOLVE_HOSTNAME: True})

        self.assertFalse(result[Output.REPLY])
        self.assertEqual(result[Output.RESPONSE], "no reply\n")

    def test_run_rc_3_or_more_raises_plugin_exception(self):
        run_factory, _ = self._run_factory(stdout="error\n", stderr="bad\n", returncode=3)
        with patch("komand_ping.actions.ping.action.subprocess.run", side_effect=run_factory):
            with self.assertRaises(PluginException):
                self.action.run({Input.HOST: "example.com", Input.COUNT: 1, Input.RESOLVE_HOSTNAME: True})

    def test_run_parse_error_raises_plugin_exception(self):
        run_factory, _ = self._run_factory(stdout="totally malformed output\n", returncode=0)
        with patch("komand_ping.actions.ping.action.subprocess.run", side_effect=run_factory):
            with self.assertRaises(PluginException):
                self.action.run({Input.HOST: "example.com", Input.COUNT: 1, Input.RESOLVE_HOSTNAME: True})

    def test_run_rejects_host_starting_with_dash(self):
        with self.assertRaises(PluginException):
            self.action.run({Input.HOST: "-c", Input.COUNT: 1, Input.RESOLVE_HOSTNAME: True})

    def test_run_rejects_host_with_whitespace_or_shell_chars(self):
        with self.assertRaises(PluginException):
            self.action.run({Input.HOST: "example.com; rm -rf /", Input.COUNT: 1, Input.RESOLVE_HOSTNAME: True})

    def test_run_success_with_ipv4_address(self):
        run_factory, calls = self._run_factory(stdout=LINUX_PING_SUCCESS, returncode=0, capture_calls=True)
        with patch("komand_ping.actions.ping.action.subprocess.run", side_effect=run_factory):
            result = self.action.run({Input.HOST: "192.168.1.1", Input.COUNT: 4, Input.RESOLVE_HOSTNAME: True})

        self.assertTrue(result[Output.REPLY])
        self.assertEqual(len(calls), 1)
        argv = calls[0]["args"]
        self.assertEqual(argv[-1], "192.168.1.1")
        self.assertEqual(result[Output.PACKETS_TRANSMITTED], 4)
        self.assertEqual(result[Output.PACKETS_RECEIVED], 4)
        self.assertEqual(result[Output.PACKETS_PERCENT_LOST], 0.0)
        self.assertEqual(result[Output.MINIMUM_LATENCY], "9.900ms")
        self.assertEqual(result[Output.AVERAGE_LATENCY], "10.100ms")
        self.assertEqual(result[Output.MAXIMUM_LATENCY], "10.300ms")
        self.assertEqual(result[Output.STANDARD_DEVIATION], "0.200ms")

    def test_run_success_with_ipv6_address(self):
        run_factory, calls = self._run_factory(stdout=LINUX_PING_SUCCESS, returncode=0, capture_calls=True)
        with patch("komand_ping.actions.ping.action.subprocess.run", side_effect=run_factory):
            result = self.action.run({Input.HOST: "2001:0db8::1", Input.COUNT: 4, Input.RESOLVE_HOSTNAME: False})

        self.assertTrue(result[Output.REPLY])
        self.assertEqual(len(calls), 1)
        argv = calls[0]["args"]
        self.assertEqual(argv[-1], "2001:0db8::1")
        self.assertEqual(result[Output.PACKETS_TRANSMITTED], 4)
        self.assertEqual(result[Output.PACKETS_RECEIVED], 4)
        self.assertEqual(result[Output.PACKETS_PERCENT_LOST], 0.0)
        self.assertEqual(result[Output.MINIMUM_LATENCY], "9.900ms")
        self.assertEqual(result[Output.AVERAGE_LATENCY], "10.100ms")
        self.assertEqual(result[Output.MAXIMUM_LATENCY], "10.300ms")
        self.assertEqual(result[Output.STANDARD_DEVIATION], "0.200ms")

    def test_run_with_ipv4_loopback(self):
        run_factory, calls = self._run_factory(stdout=LINUX_PING_SUCCESS, returncode=0, capture_calls=True)
        with patch("komand_ping.actions.ping.action.subprocess.run", side_effect=run_factory):
            result = self.action.run({Input.HOST: "127.0.0.1", Input.COUNT: 2, Input.RESOLVE_HOSTNAME: False})

        self.assertTrue(result[Output.REPLY])
        argv = calls[0]["args"]
        self.assertIn("-n", argv)
        self.assertEqual(argv[-1], "127.0.0.1")
        self.assertEqual(result[Output.PACKETS_TRANSMITTED], 4)
        self.assertEqual(result[Output.PACKETS_RECEIVED], 4)
        self.assertEqual(result[Output.PACKETS_PERCENT_LOST], 0.0)

    def test_run_with_private_ip_address(self):
        run_factory, _ = self._run_factory(stdout=LINUX_PING_SUCCESS, returncode=0)
        with patch("komand_ping.actions.ping.action.subprocess.run", side_effect=run_factory):
            result = self.action.run({Input.HOST: "10.0.0.1", Input.COUNT: 3, Input.RESOLVE_HOSTNAME: True})

        self.assertTrue(result[Output.REPLY])
        self.assertIn("ping statistics", result[Output.RESPONSE])
        self.assertEqual(result[Output.PACKETS_TRANSMITTED], 4)
        self.assertEqual(result[Output.PACKETS_RECEIVED], 4)
        self.assertEqual(result[Output.PACKETS_PERCENT_LOST], 0.0)
        self.assertEqual(result[Output.MINIMUM_LATENCY], "9.900ms")
        self.assertEqual(result[Output.AVERAGE_LATENCY], "10.100ms")
        self.assertEqual(result[Output.MAXIMUM_LATENCY], "10.300ms")
        self.assertEqual(result[Output.STANDARD_DEVIATION], "0.200ms")

    def test_run_with_maximum_count(self):
        run_factory, calls = self._run_factory(stdout=LINUX_PING_SUCCESS, returncode=0, capture_calls=True)
        with patch("komand_ping.actions.ping.action.subprocess.run", side_effect=run_factory):
            result = self.action.run({Input.HOST: "192.168.0.1", Input.COUNT: 100, Input.RESOLVE_HOSTNAME: True})

        argv = calls[0]["args"]
        count_index = argv.index("-c")
        self.assertEqual(argv[count_index + 1], "100")
        self.assertTrue(result[Output.REPLY])
        self.assertEqual(result[Output.PACKETS_TRANSMITTED], 4)
        self.assertEqual(result[Output.PACKETS_RECEIVED], 4)

    def test_run_partial_packet_loss(self):
        partial_loss_output = (
            "PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.\n"
            "64 bytes from 8.8.8.8: icmp_seq=1 ttl=56 time=10.1 ms\n\n"
            "--- 8.8.8.8 ping statistics ---\n"
            "4 packets transmitted, 2 received, 50% packet loss, time 3002ms\n"
            "rtt min/avg/max/mdev = 9.900/10.100/10.300/0.200 ms\n"
        )
        run_factory, _ = self._run_factory(stdout=partial_loss_output, returncode=0)
        with patch("komand_ping.actions.ping.action.subprocess.run", side_effect=run_factory):
            result = self.action.run({Input.HOST: "8.8.8.8", Input.COUNT: 4, Input.RESOLVE_HOSTNAME: False})

        self.assertTrue(result[Output.REPLY])
        self.assertEqual(result[Output.PACKETS_TRANSMITTED], 4)
        self.assertEqual(result[Output.PACKETS_RECEIVED], 2)
        self.assertEqual(result[Output.PACKETS_PERCENT_LOST], 50.0)

    def test_run_with_single_count(self):
        run_factory, calls = self._run_factory(stdout=LINUX_PING_SUCCESS, returncode=0, capture_calls=True)
        with patch("komand_ping.actions.ping.action.subprocess.run", side_effect=run_factory):
            result = self.action.run({Input.HOST: "1.1.1.1", Input.COUNT: 1, Input.RESOLVE_HOSTNAME: False})

        argv = calls[0]["args"]
        count_index = argv.index("-c")
        self.assertEqual(argv[count_index + 1], "1")
        self.assertTrue(result[Output.REPLY])
        self.assertEqual(result[Output.PACKETS_TRANSMITTED], 4)
        self.assertEqual(result[Output.PACKETS_RECEIVED], 4)
