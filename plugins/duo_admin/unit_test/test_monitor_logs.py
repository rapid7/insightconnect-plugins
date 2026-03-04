import os
import sys
from time import time

sys.path.append(os.path.abspath("../"))

from datetime import datetime, timezone
from unittest import TestCase
from unittest.mock import patch, MagicMock

from komand_duo_admin.tasks.monitor_logs.task import MonitorLogs, ADMIN_LOGS_LIMIT
from parameterized import parameterized

from util import Util


@patch(
    "komand_duo_admin.tasks.monitor_logs.task.MonitorLogs.get_current_time",
    return_value=datetime.strptime("2023-05-01T08:34:46", "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc),
)
@patch("requests.request", side_effect=Util.mock_request)
@patch("komand_duo_admin.util.api.isinstance", return_value=True)
@patch("komand_duo_admin.util.api.DuoAdminAPI.get_headers", return_value={})
class TestMonitorLogs(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.task = Util.default_connector(MonitorLogs())
        cls.custom_config = {"cutoff": {"date": "2023-04-30T08:34:46.000Z"}, "lookback": "2023-04-30T08:34:46.000Z"}

    @parameterized.expand(
        [
            [
                "without_state",
                Util.read_file_to_dict("inputs/monitor_logs_without_state.json.inp"),
                Util.read_file_to_dict("expected/monitor_logs.json.exp"),
                {
                    "filter_cutoff_auth_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "filter_cutoff_admin_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "filter_cutoff_trust_monitor_events_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "lookback": "2023-04-30T08:34:46.000Z",
                },
            ],
            [
                "with_rate_limit",
                Util.read_file_to_dict("inputs/monitor_logs_with_rate_limit.json.inp"),
                Util.read_file_to_dict("expected/monitor_logs_rate_limit.json.exp"),
                {},
            ],
            [
                "with_state",
                Util.read_file_to_dict("inputs/monitor_logs_with_state.json.inp"),
                Util.read_file_to_dict("expected/monitor_logs_2.json.exp"),
                {
                    "filter_cutoff_auth_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "filter_cutoff_admin_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "filter_cutoff_trust_monitor_events_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "lookback": "2023-04-30T08:34:46.000Z",
                },
            ],
            [
                "with_incorrect_timestamp_in_state",
                Util.read_file_to_dict("inputs/monitor_logs_incorrect_timestamp_format.json.inp"),
                Util.read_file_to_dict("expected/monitor_logs_2.json.exp"),
                {
                    "filter_cutoff_auth_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "filter_cutoff_admin_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "filter_cutoff_trust_monitor_events_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "lookback": "2023-04-30T08:34:46.000Z",
                },
            ],
            [
                "next_page",
                Util.read_file_to_dict("inputs/monitor_logs_next_page.json.inp"),
                Util.read_file_to_dict("expected/monitor_logs_3.json.exp"),
                {
                    "filter_cutoff_auth_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "filter_cutoff_admin_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "filter_cutoff_trust_monitor_events_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "lookback": "2023-04-30T08:34:46.000Z",
                },
            ],
            [
                "bad_request",
                Util.read_file_to_dict("inputs/monitor_logs_bad_request.json.inp"),
                Util.read_file_to_dict("expected/monitor_logs_bad_request.json.exp"),
                {
                    "filter_cutoff_auth_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "filter_cutoff_admin_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "filter_cutoff_trust_monitor_events_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "lookback": 72,
                },
            ],
            [
                "server_error",
                Util.read_file_to_dict("inputs/monitor_logs_server_error.json.inp"),
                Util.read_file_to_dict("expected/monitor_logs_server_error.json.exp"),
                {
                    "filter_cutoff_auth_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "filter_cutoff_admin_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "filter_cutoff_trust_monitor_events_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "lookback": 72,
                },
            ],
        ]
    )
    def test_monitor_logs(
        self,
        mock_request,
        mock_request_instance,
        mock_get_headers,
        mock_get_time,
        test_name,
        current_state,
        expected,
        config,
    ) -> None:
        actual, actual_state, has_more_pages, status_code, _ = self.task.run(state=current_state, custom_config=config)
        self.assertEqual(actual, expected.get("logs"))
        self.assertEqual(actual_state, expected.get("state"))
        self.assertEqual(status_code, expected.get("status_code"))

    def test_monitor_logs_with_rate_limit_whole_flow(
        self, mock_request, mock_request_instance, mock_get_headers, mock_get_time
    ) -> None:
        future_time_state = {"rate_limit_datetime": time() + 600}
        passed_time_state = {"rate_limit_datetime": time() - 600}

        actual, new_state, has_more_pages, status_code, _ = self.task.run(state=future_time_state, custom_config={})

        self.assertEqual(actual, [])
        self.assertEqual(future_time_state, new_state)
        self.assertEqual(has_more_pages, False)
        self.assertEqual(status_code, 429)

        actual_2, new_state_2, _, status_code_2, _ = self.task.run(state=passed_time_state, custom_config={})

        self.assertTrue(actual_2)
        self.assertTrue(new_state_2)
        self.assertEqual(status_code_2, 200)

    @patch("komand_duo_admin.util.api.DuoAdminAPI.get_trust_monitor_events")
    @patch("komand_duo_admin.util.api.DuoAdminAPI.get_auth_logs")
    @patch("komand_duo_admin.util.api.DuoAdminAPI.get_admin_logs")
    def test_admin_logs_pagination_triggers(
        self,
        mock_get_admin: MagicMock,
        mock_auth: MagicMock,
        mock_trust: MagicMock,
        mock_request: MagicMock,
        mock_request_instance: MagicMock,
        mock_get_headers: MagicMock,
        mock_get_time: MagicMock,
    ) -> None:
        # Create a list of admin logs with the same timestamp to trigger pagination
        admin_timestamp = 1682836490
        admin_logs = [
            {"action": "user_create", "description": {}, "timestamp": admin_timestamp, "username": "API"}
            for _ in range(ADMIN_LOGS_LIMIT)
        ]

        # Setup mocks to return the admin logs and empty responses for auth logs and trust monitor events
        mock_get_admin.return_value = {"response": admin_logs}
        mock_auth.return_value = {"response": {"authlogs": [], "metadata": {}}}
        mock_trust.return_value = {"response": {"events": [], "metadata": {}}}

        # Set initial state with `admin_timestamp - 1` to ensure the API returns the logs with `admin_timestamp`
        state = {
            "admin_logs_last_log_timestamp": admin_timestamp - 1,
            "auth_logs_last_log_timestamp": 1682843686,
            "trust_monitor_last_log_timestamp": 1682843686000,
        }

        # Execute task run and get the new state and pagination info
        _, new_state, has_more_pages, status_code, _ = self.task.run(state=state, custom_config={})
        pagination_params = new_state["admin_logs_next_page_params"]

        # Verify the pagination parameters and new state
        self.assertIn("admin_logs_next_page_params", new_state)
        self.assertEqual(pagination_params["mintime"], str(admin_timestamp))
        self.assertTrue(has_more_pages)
        self.assertEqual(status_code, 200)

    @patch("komand_duo_admin.tasks.monitor_logs.task.ADMIN_LOGS_LIMIT", 10)
    @patch("komand_duo_admin.util.api.DuoAdminAPI.get_trust_monitor_events")
    @patch("komand_duo_admin.util.api.DuoAdminAPI.get_auth_logs")
    @patch("komand_duo_admin.util.api.DuoAdminAPI.get_admin_logs")
    def test_admin_logs_loop_detection(
        self,
        mock_get_admin: MagicMock,
        mock_auth: MagicMock,
        mock_trust: MagicMock,
        mock_request: MagicMock,
        mock_request_instance: MagicMock,
        mock_get_headers: MagicMock,
        mock_get_time: MagicMock,
    ) -> None:
        # Reimport
        from komand_duo_admin.tasks.monitor_logs.task import ADMIN_LOGS_LIMIT

        # Create a list of admin logs with the same timestamp to trigger pagination
        response = {"response": []}
        for _ in range(ADMIN_LOGS_LIMIT):
            response["response"].append(
                {"action": "user_create", "description": {}, "timestamp": 1682836495, "username": "API"}
            )
        mock_get_admin.return_value = response
        mock_auth.return_value = {"response": {"authlogs": [], "metadata": {}}}
        mock_trust.return_value = {"response": {"events": [], "metadata": {}}}

        # Set initial state with a timestamp that will trigger pagination and infinite loop detection
        state = {
            "admin_logs_last_log_timestamp": 1682836495,
            "auth_logs_last_log_timestamp": 1682843686,
            "trust_monitor_last_log_timestamp": 1682843686000,
            "admin_logs_next_page_params": {"mintime": "1682836495"},
        }

        # Execute task run and get the new state and pagination info
        _, new_state, has_more_pages, status_code, _ = self.task.run(state=state, custom_config={})

        # Verify that the task detected the potential infinite loop and incremented the `mintime` to avoid it
        self.assertIn("admin_logs_next_page_params", new_state)
        self.assertEqual(new_state["admin_logs_next_page_params"]["mintime"], "1682836496")
        self.assertEqual(status_code, 200)

    @patch("komand_duo_admin.util.api.DuoAdminAPI.get_trust_monitor_events")
    @patch("komand_duo_admin.util.api.DuoAdminAPI.get_auth_logs")
    @patch("komand_duo_admin.util.api.DuoAdminAPI.get_admin_logs")
    def test_admin_logs_no_pagination_with_less_elements(
        self,
        mock_get_admin: MagicMock,
        mock_auth: MagicMock,
        mock_trust: MagicMock,
        mock_request: MagicMock,
        mock_request_instance: MagicMock,
        mock_get_headers: MagicMock,
        mock_get_time: MagicMock,
    ) -> None:
        # Create a list of admin logs with the same timestamp
        # But less than the pagination limit to ensure no pagination occurs
        response = {"response": []}
        for _ in range(ADMIN_LOGS_LIMIT - ADMIN_LOGS_LIMIT // 20):
            response["response"].append(
                {"action": "user_create", "description": {}, "timestamp": 1682836400, "username": "API"}
            )
        mock_get_admin.return_value = response
        mock_auth.return_value = {"response": {"authlogs": [], "metadata": {}}}
        mock_trust.return_value = {"response": {"events": [], "metadata": {}}}

        # Set initial state with a timestamp that will return logs but not trigger pagination
        state = {
            "admin_logs_last_log_timestamp": 1682836399,
            "auth_logs_last_log_timestamp": 1682843686,
            "trust_monitor_last_log_timestamp": 1682843686000,
        }

        # Execute task run and get the new state and pagination info
        _, new_state, has_more_pages, status_code, _ = self.task.run(state=state, custom_config={})

        # Verify that no pagination parameters are set and the state is updated correctly
        self.assertNotIn("admin_logs_next_page_params", new_state)
        self.assertFalse(has_more_pages)
        self.assertEqual(status_code, 200)

    @patch("komand_duo_admin.util.api.DuoAdminAPI.get_trust_monitor_events")
    @patch("komand_duo_admin.util.api.DuoAdminAPI.get_auth_logs")
    @patch("komand_duo_admin.util.api.DuoAdminAPI.get_admin_logs")
    def test_admin_logs_stuck_at_same_timestamp_without_pagination(
        self,
        mock_get_admin: MagicMock,
        mock_auth: MagicMock,
        mock_trust: MagicMock,
        mock_request: MagicMock,
        mock_request_instance: MagicMock,
        mock_get_headers: MagicMock,
        mock_get_time: MagicMock,
    ) -> None:
        # Setup mocks to return empty responses for auth logs and trust monitor events
        mock_auth.return_value = {"response": {"authlogs": [], "metadata": {}}}
        mock_trust.return_value = {"response": {"events": [], "metadata": {}}}

        # Simulate customer scenario where querying from timestamp X returns ADMIN_LOGS_LIMIT logs
        # All with the same timestamp X, causing pagination to trigger but getting stuck in loop
        stuck_timestamp = 1772081831
        response = {"response": []}
        for index in range(ADMIN_LOGS_LIMIT):
            response["response"].append(
                {
                    "action": "user_create",
                    "description": {"user_id": f"user_{index}"},
                    "timestamp": stuck_timestamp,
                    "username": "API",
                }
            )
        mock_get_admin.return_value = response

        # First run - `mintime` will be stuck_timestamp (from state), API returns logs at stuck_timestamp
        # This should trigger loop detection: `last_timestamp == mintime` without pagination parameters
        state = {
            "admin_logs_last_log_timestamp": stuck_timestamp,
            "auth_logs_last_log_timestamp": 1682843686,
            "trust_monitor_last_log_timestamp": 1682843686000,
        }

        # Execute task run and get the new state and pagination info
        _, new_state, has_more_pages, status_code, _ = self.task.run(state=state, custom_config={})

        # Should detect loop and bump `mintime` by 1 second
        self.assertIn("admin_logs_next_page_params", new_state)
        self.assertEqual(new_state["admin_logs_next_page_params"]["mintime"], str(stuck_timestamp + 1))

        # The `last_log_timestamp` should remain at the `stuck_timestamp` (or move to `maxtime` if no new logs)
        self.assertTrue(has_more_pages)
        self.assertEqual(status_code, 200)

    @patch("komand_duo_admin.util.api.DuoAdminAPI.get_trust_monitor_events")
    @patch("komand_duo_admin.util.api.DuoAdminAPI.get_auth_logs")
    @patch("komand_duo_admin.util.api.DuoAdminAPI.get_admin_logs")
    def test_admin_logs_normal_pagination_with_different_timestamps(
        self,
        mock_get_admin: MagicMock,
        mock_auth: MagicMock,
        mock_trust: MagicMock,
        mock_request: MagicMock,
        mock_request_instance: MagicMock,
        mock_get_headers: MagicMock,
        mock_get_time: MagicMock,
    ) -> None:
        # Setup mocks to return empty responses for auth logs and trust monitor events
        mock_auth.return_value = {"response": {"authlogs": [], "metadata": {}}}
        mock_trust.return_value = {"response": {"events": [], "metadata": {}}}

        # Create logs with progressing timestamps (normal pagination scenario)
        response = {"response": []}
        base_timestamp = 1682836400
        for index in range(ADMIN_LOGS_LIMIT):
            response["response"].append(
                {"action": "user_create", "description": {}, "timestamp": base_timestamp + index, "username": "API"}
            )
        mock_get_admin.return_value = response

        # Set initial state with `base_timestamp - 1` to ensure the API returns logs starting from `base_timestamp`
        state = {
            "admin_logs_last_log_timestamp": 1682836395,
            "auth_logs_last_log_timestamp": 1682843686,
            "trust_monitor_last_log_timestamp": 1682843686000,
            "admin_logs_next_page_params": {"mintime": "1682836400"},
        }

        # Execute task run and get the new state and pagination info
        _, new_state, has_more_pages, status_code, _ = self.task.run(state=state, custom_config={})

        # Should continue pagination normally without triggering loop detection
        self.assertIn("admin_logs_next_page_params", new_state)

        # Should set `mintime` to last timestamp (not increment by 1)
        self.assertEqual(
            new_state["admin_logs_next_page_params"]["mintime"], str(base_timestamp + ADMIN_LOGS_LIMIT - 1)
        )
        self.assertTrue(has_more_pages)
        self.assertEqual(status_code, 200)
