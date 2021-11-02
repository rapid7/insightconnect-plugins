import sys
import os

from unittest import TestCase
from icon_cisco_asa.actions.block_host import BlockHost
from icon_cisco_asa.actions.block_host.schema import Input, Output
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))


@patch("requests.request", side_effect=Util.mocked_requests)
class TestGetBlockedHosts(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(BlockHost())

    @parameterized.expand(
        [
            ["block_host", True, "1.1.1.1", None, None, None, None, True],
            ["block_host2", True, "2.2.2.2", "3.3.3.3", 333, 444, "tcp", True],
            ["block_host_without_ports", True, "2.2.2.2", "3.3.3.3", None, None, "tcp", True],
            ["block_host_without_dest_ip", True, "2.2.2.2", None, 333, 444, "tcp", True],
            ["block_host_without_protocol", True, "2.2.2.2", "3.3.3.3", 333, 444, None, True],
            ["block_host_empty_strings", True, "1.1.1.1", "", "", "", "", True],
            ["unblock_host", False, "1.1.1.1", None, None, None, None, True],
        ]
    )
    def test_block_host(self, mock_post, name, shun, source_ip, dest_ip, source_port, dest_port, protocol, expected):
        actual = self.action.run(
            {
                Input.SHUN: shun,
                Input.SOURCE_IP: source_ip,
                Input.DESTINATION_IP: dest_ip,
                Input.SOURCE_PORT: source_port,
                Input.DESTINATION_PORT: dest_port,
                Input.PROTOCOL: protocol,
            }
        )
        expected = {Output.SUCCESS: expected}
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "block_host_invalid_source_ip",
                True,
                "999.999.999.999",
                "2.2.2.2",
                333,
                444,
                "tcp",
                "Something unexpected occurred.",
                "Check the logs and if the issue persists please contact support.",
                'Response was: {"response": "Error: Invalid Hostname"}',
            ],
            [
                "block_host_invalid_dest_ip",
                True,
                "1.1.1.1",
                "999.999.999.999",
                333,
                444,
                "tcp",
                "Something unexpected occurred.",
                "Check the logs and if the issue persists please contact support.",
                'Response was: {"response": "Error: Invalid Hostname"}',
            ],
            [
                "unblock_host_invalid_ip",
                False,
                "999.999.999.999",
                None,
                None,
                None,
                None,
                "Something unexpected occurred.",
                "Check the logs and if the issue persists please contact support.",
                'Response was: {"response": "Error: Invalid Hostname"}',
            ],
        ]
    )
    def test_block_host_bad(
        self, mock_post, name, shun, source_ip, dest_ip, source_port, dest_port, protocol, cause, assistance, data
    ):
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.SHUN: shun,
                    Input.SOURCE_IP: source_ip,
                    Input.DESTINATION_IP: dest_ip,
                    Input.SOURCE_PORT: source_port,
                    Input.DESTINATION_PORT: dest_port,
                    Input.PROTOCOL: protocol,
                }
            )
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
        self.assertEqual(e.exception.data, data)
