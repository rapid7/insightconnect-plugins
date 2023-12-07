import os
import sys

sys.path.append(os.path.abspath("../"))

from datetime import datetime, timezone
from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from jsonschema import validate
from komand_salesforce.tasks.monitor_users.schema import MonitorUsersOutput
from komand_salesforce.tasks.monitor_users.task import MonitorUsers
from parameterized import parameterized

from util import Util


@patch(
    "komand_salesforce.tasks.monitor_users.task.MonitorUsers.get_current_time",
    return_value=datetime.strptime("2023-07-20 16:21:15.340262+00:00", "%Y-%m-%d %H:%M:%S.%f%z").replace(
        tzinfo=timezone.utc
    ),
)
@patch("requests.request", side_effect=Util.mock_request)
class TestMonitorUsers(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(MonitorUsers())

    @parameterized.expand(
        [
            [
                "without_state",
                Util.read_file_to_dict("inputs/monitor_users_without_state.json.inp"),
                Util.read_file_to_dict("expected/monitor_users_without_state.json.exp"),
            ],
            [
                "with_state",
                Util.read_file_to_dict("inputs/monitor_users_with_state.json.inp"),
                Util.read_file_to_dict("expected/monitor_users_with_state.json.exp"),
            ],
            [
                "with_date_old_format_state",
                Util.read_file_to_dict("inputs/monitor_users_with_state.json.inp"),
                Util.read_file_to_dict("expected/monitor_users_with_state.json.exp"),
            ],
            [
                "empty",
                Util.read_file_to_dict("inputs/monitor_users_empty.json.inp"),
                Util.read_file_to_dict("expected/monitor_users_empty.json.exp"),
            ],
            [
                "next_page",
                Util.read_file_to_dict("inputs/monitor_users_next_page.json.inp"),
                Util.read_file_to_dict("expected/monitor_users_next_page.json.exp"),
            ],
            [
                "bad_request",
                Util.read_file_to_dict("inputs/monitor_users_bad_request.json.inp"),
                Util.read_file_to_dict("expected/monitor_users_bad_request.json.exp"),
            ],
        ]
    )
    def test_monitor_users(
        self,
        mock_request: MagicMock,
        mock_get_time: MagicMock,
        test_name: str,
        current_state: Dict[str, Any],
        expected: Dict[str, Any],
    ) -> None:
        actual, actual_state, has_more_pages, status_code, error = self.action.run(state=current_state)
        validate(actual, MonitorUsersOutput.schema)
        self.assertEqual(actual, expected.get("users"))
        self.assertEqual(actual_state, expected.get("state"))
        self.assertEqual(has_more_pages, expected.get("has_more_pages"))
        self.assertEqual(status_code, expected.get("status_code"))
