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
from komand_salesforce.connection.schema import Input
from parameterized import parameterized

from util import Util


@patch(
    "komand_salesforce.tasks.monitor_users.task.MonitorUsers.get_current_time",
    return_value=datetime.strptime("2023-07-20 16:21:15.340262+00:00", "%Y-%m-%d %H:%M:%S.%f%z").replace(
        tzinfo=timezone.utc
    ),
)
@patch("requests.request", side_effect=Util.mock_request)
@patch("logging.Logger.info")
@patch("komand_salesforce.util.api.SalesforceAPI.unset_token")
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
        mocked_unset: MagicMock,
        mocked_logger: MagicMock,
        _mock_request: MagicMock,
        _mock_get_time: MagicMock,
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

        if test_name != "bad_request":
            mocked_unset.assert_called()  # corrupt state so a token is never retrieved from Salesforce

        if test_name == "without_state":
            self.assertTrue(mocked_logger.called)
            self.assertIn("lookback time of 24 hours", mocked_logger.call_args_list[0][0][0])

    def test_monitor_events_uses_custom_config_for_backfill(
        self, mock_unset, mocked_logger, _mock_request, _mock_get_time
    ):
        config = {
            "lookback": {"year": 2023, "month": 6, "day": 5, "hour": 3, "minute": 45, "second": 0},
            "cutoff": {"date": {"year": 2023, "month": 6, "day": 5}},
        }

        # for the first run we should be querying using the `lookback` value until `now` (mocked to 2023).
        _logs, actual_state, _more_pages, status_code, error = self.action.run({}, {}, config)
        expected_state = {
            "last_user_login_collection_timestamp": "2023-07-20 16:21:15.340262+00:00",  # current time
            "next_user_collection_timestamp": "2023-07-21 16:21:15.340262+00:00",  # current time + 24 hours
            "last_user_update_collection_timestamp": "2023-07-20 16:21:15.340262+00:00",  # current time
            "next_user_login_collection_timestamp": "2023-07-20 17:21:15.340262+00:00",  # current time + 1 hours
            "users_next_page_id": "/01gRO0000087654321-500",  # mocked response gives us next page
        }
        self.assertEqual(200, status_code)
        self.assertEqual(None, error)
        self.assertDictEqual(actual_state, expected_state)

        self.assertIn("custom lookback", mocked_logger.call_args_list[0][0][0])
        mock_unset.assert_called()

        # on the second iteration we then carry on as normal that we query from last poll end time to now
        mocked_logger.reset_mock()
        mock_unset.reset_mock()
        _logs, updated_state, _more_pages, status_code, error = self.action.run({}, expected_state, config)
        self.assertNotIn("custom lookback", mocked_logger.call_args_list[0][0][0])  # lookback no longer used

        # This means we won't query for user login activity (every hour)
        for mock_log in mocked_logger.call_args_list:
            self.assertNotIn("Get user login history", mock_log[0][0])
        self.assertIn("Get all internal users", mocked_logger.call_args_list[2][0][0])  # we had a next page of users

        # State time for these should not have changed since the last call
        for state_key in ["next_user_login_collection_timestamp", "next_user_collection_timestamp"]:
            self.assertEqual(updated_state[state_key], expected_state[state_key])

        mock_unset.assert_called()

    def test_monitor_events_uses_custom_config_for_cutoff_override(
        self, mock_unset, mocked_logger, _mock_request, _mock_get_time
    ):
        config = {"cutoff": {"hours": 2}}
        customers_paused_state = {
            "last_user_login_collection_timestamp": "2023-06-21 16:21:15.340262+00:00",  # last time customer ran this
            "next_user_collection_timestamp": "2023-06-21 16:21:15.340262+00:00",  # saved next expected
            "last_user_update_collection_timestamp": "2023-06-20 16:21:15.340262+00:00",  # last time customer ran this
            "next_user_login_collection_timestamp": "2023-06-20 17:21:15.340262+00:00",  # saved next expected
        }

        _logs, new_state, _more_pages, _status_code, _error = self.action.run({}, customers_paused_state, config)
        cut_off_log = "Cut off time being applied: 2023-07-20 14:21:15.340262+00:00"  # now - 2 hours
        self.assertIn(cut_off_log, mocked_logger.call_args_list[0][0][0])

        # All timestamps should have been moved forward as cut off was applied
        expected_state = {
            "last_user_login_collection_timestamp": "2023-07-20 16:21:15.340262+00:00",  # just executed 'now'
            "next_user_collection_timestamp": "2023-07-21 16:21:15.340262+00:00",  # next expected now + 24 hours
            "last_user_update_collection_timestamp": "2023-07-20 16:21:15.340262+00:00",  # just executed 'now'
            "next_user_login_collection_timestamp": "2023-07-20 17:21:15.340262+00:00",  # next expected: now + 1 hour
            "users_next_page_id": "/01gRO0000087654321-500",
        }

        self.assertDictEqual(expected_state, new_state)

        mock_unset.assert_called()

    def test_default_cut_off_values_of_7_days(self, mock_unset, mocked_logger, _mock_request, _mock_get_time):
        user_login_time = "2023-06-21 16:21:15.340262+00:00"  # exceeds 7 day lookback value
        user_update_time = "2023-06-20 16:21:15.340262+00:00"  # exceeds 7 day lookback value
        cutoff = "2023-07-13 16:21:15.340262+00:00"  # this is the cut off value now - 7 days

        customers_paused_state = {
            "last_user_login_collection_timestamp": user_login_time,  # last time customer ran this
            "next_user_collection_timestamp": "2023-06-21 16:21:15.340262+00:00",  # saved next expected
            "last_user_update_collection_timestamp": user_update_time,  # last time customer ran this
            "next_user_login_collection_timestamp": "2023-06-20 17:21:15.340262+00:00",  # saved next expected
        }

        _logs, _new_state, _more_pages, _status_code, _error = self.action.run({}, customers_paused_state, {})

        # check logger says the timestamps were moved forward for last_user login and user update endpoint
        cutoff_msg = "State stored timestamp is: {}, returning {} to keep within our fallback period."
        user_login_cutoff = cutoff_msg.format(user_login_time, cutoff)
        user_update_cutoff = cutoff_msg.format(user_update_time, cutoff)
        self.assertEqual(user_update_cutoff, mocked_logger.call_args_list[2][0][0])
        self.assertEqual(user_login_cutoff, mocked_logger.call_args_list[3][0][0])

        mock_unset.assert_called()

    @parameterized.expand(
        [
            [
                "without_state",
                {
                    "last_user_update_collection_timestamp": "2025-07-21 15:21:15.340262+00:00",
                    "next_user_collection_timestamp": "2023-07-21 15:21:15.340262+00:00",
                    "next_user_login_collection_timestamp": "2023-07-20 15:21:15.340262+00:00",
                    "last_user_login_collection_timestamp": "2023-07-20 14:21:15.340262+00:00",
                },
                {},
            ],
        ]
    )
    def test_bad_domain_provided(
        self,
        mocked_unset: MagicMock,
        mocked_logger: MagicMock,
        _mock_request: MagicMock,
        _mock_get_time: MagicMock,
        test_name: str,
        current_state: Dict[str, Any],
        expected: Dict[str, Any],
    ) -> None:

        params = {
            Input.CLIENTID: "example-client-id",
            Input.CLIENTSECRET: {"secretKey": "example-secret-key"},
            Input.SALESFORCEACCOUNTUSERNAMEANDPASSWORD: {
                "username": "example-username",
                "password": "example-password",
            },
            Input.SECURITYTOKEN: {"secretKey": "example-secret-key"},
            Input.LOGINURL: "bad_domain",
        }

        self.action = Util.default_connector(MonitorUsers(), params=params)
        actual, _actual_state, _has_more_pages, status_code, error = self.action.run(state=current_state)

        self.assertEqual(
            error.cause, "Invalid Login URL format. URL should be a pure domain without paths or parameters."
        )
        self.assertEqual(status_code, 400)

        validate(actual, MonitorUsersOutput.schema)
