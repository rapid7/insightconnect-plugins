import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_fireeye_hx.actions.check_host_quarantine_status import CheckHostQuarantineStatus
from icon_fireeye_hx.actions.check_host_quarantine_status.schema import Input, Output
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.sessions.Session.request", side_effect=Util.mocked_requests)
class TestCheckHostQuarantineStatus(TestCase):
    @classmethod
    def setUp(cls) -> None:
        cls.action = Util.default_connector(CheckHostQuarantineStatus())

    @parameterized.expand(
        [
            [
                "host_found",
                "1111111111",
                {
                    "results": {
                        "_id": "1111111111",
                        "last_sysinfo": "2022-01-05T04:14:47.419Z",
                        "requested_by_actor": {"_id": 1000, "username": "admin"},
                        "requested_on": "2022-01-05T16:56:52.718Z",
                        "contained_by_actor": {"_id": 1000, "username": "admin"},
                        "contained_on": "2022-01-05T16:56:52.718Z",
                        "queued": True,
                        "excluded": False,
                        "missing_software": False,
                        "reported_clone": False,
                        "state": "uncontaining",
                        "state_update_time": "2022-01-05T17:11:03.276Z",
                        "url": "/hx/api/v3/hosts/1111111111",
                    },
                },
            ]
        ]
    )
    def test_check_host_quarantine_status(self, mock_request, name, host_id, expected):
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
    def test_check_host_quarantine_status_bad(self, mock_request, name, host_id, cause, assistance, data):
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.AGENT_ID: host_id,
                }
            )
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
        self.assertEqual(e.exception.data, data)
