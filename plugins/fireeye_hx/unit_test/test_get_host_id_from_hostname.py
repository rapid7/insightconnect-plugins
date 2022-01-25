import sys
import os

from unittest import TestCase
from icon_fireeye_hx.actions.get_host_id_from_hostname import GetHostIdFromHostname
from icon_fireeye_hx.actions.get_host_id_from_hostname.schema import Input, Output
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))


@patch("requests.sessions.Session.request", side_effect=Util.mocked_requests)
class TestGetHostIdFromHostname(TestCase):
    @classmethod
    def setUp(cls) -> None:
        cls.action = Util.default_connector(GetHostIdFromHostname())

    @parameterized.expand(
        [
            [
                "found",
                "example_hostname",
                {"success": True, "host_id": "1111111111"},
            ],
            [
                "not_found",
                "invalid_hostname",
                {"success": False},
            ],
        ]
    )
    def test_get_host_id_from_hostname(self, mock_request, name, hostname, expected):
        actual = self.action.run(
            {
                Input.HOSTNAME: hostname,
            }
        )
        self.assertEqual(actual, expected)
