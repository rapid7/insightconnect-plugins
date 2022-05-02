import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_fireeye_hx.actions.unquarantine_host import UnquarantineHost
from icon_fireeye_hx.actions.unquarantine_host.schema import Input, Output
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.sessions.Session.request", side_effect=Util.mocked_requests)
class TestUnquarantineHost(TestCase):
    @classmethod
    def setUp(cls) -> None:
        cls.action = Util.default_connector(UnquarantineHost())

    @parameterized.expand(
        [
            [
                "success",
                "1111111111",
                {"success": True},
            ]
        ]
    )
    def test_unquarantine_host(self, mock_request, name, host_id, expected):
        actual = self.action.run(
            {
                Input.AGENT_ID: host_id,
            }
        )
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "host_not_found",
                "invalid_host_id",
                "Invalid or unreachable endpoint provided.",
                "Verify the endpoint/URL/hostname configured in your plugin connection is correct.",
                '{"message": "Not Found"}',
            ]
        ]
    )
    def test_unquarantine_host_bad(self, mock_request, name, host_id, cause, assistance, data):
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.AGENT_ID: host_id,
                }
            )
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
        self.assertEqual(e.exception.data, data)
