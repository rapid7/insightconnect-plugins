import sys
from typing import Any, Dict, List

sys.path.append("../")

import datetime
import logging
import unittest
from unittest.mock import MagicMock, patch

from icon_zoom.connection.connection import Connection
from icon_zoom.tasks.monitor_sign_in_out_activity.task import MonitorSignInOutActivity
from icon_zoom.tasks.monitor_sign_in_out_activity.schema import (
    MonitorSignInOutActivityOutput,
    MonitorSignInOutActivityState,
)
from icon_zoom.util.event import Event
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized
from jsonschema import validate
from datetime import timedelta

from mock import STUB_CONNECTION, STUB_OAUTH_TOKEN, Util

REFRESH_OAUTH_TOKEN_PATH = "icon_zoom.util.api.ZoomAPI._refresh_oauth_token"
GET_USER_ACTIVITY_EVENTS_PATH = "icon_zoom.util.api.ZoomAPI.get_user_activity_events_task"
GET_DATETIME_NOW_PATH = "icon_zoom.tasks.monitor_sign_in_out_activity.task.MonitorSignInOutActivity._get_datetime_now"
GET_DATETIME_LAST_X_HOURS_PATH = (
    "icon_zoom.tasks.monitor_sign_in_out_activity.task.MonitorSignInOutActivity._get_datetime_last_x_hours"
)

STUB_SAMPLES = [
    {
        "client_type": "mac",
        "email": "test@test.com",
        "ip_address": "11.11.11.11",
        "time": "2023-02-22T21:50:44Z",
        "type": "Sign in",
        "version": "5.13.7.15481",
    },
    {
        "client_type": "windows",
        "email": "test2@test.com",
        "ip_address": "192.168.1.1",
        "time": "2023-02-22T21:44:44Z",
        "type": "Sign in",
        "version": "5.13.7.15481",
    },
    {
        "client_type": "mac",
        "email": "test@test.com",
        "ip_address": "11.11.11.11",
        "time": "2023-02-22T21:41:41Z",
        "type": "Sign out",
        "version": "5.13.7.15481",
    },
    {
        "client_type": "mac",
        "email": "test@test.com",
        "ip_address": "11.11.11.11",
        "time": "2023-02-22T21:40:41Z",
        "type": "Sign out",
        "version": "5.13.7.15481",
    },
]
STUB_EVENTS = [Event(**sample) for sample in STUB_SAMPLES]

STUB_DATETIME_LAST_24_HOURS = datetime.datetime(2023, 2, 22, 22, 0, 0)
STUB_DATETIME_NOW = datetime.datetime(2023, 2, 23, 22, 0, 0)
STUB_DATETIME_FUTURE = datetime.datetime(2024, 2, 23, 22, 0, 0)
DEFAULT_TIMEDELTA = 5

STUB_EXPECTED_PREVIOUS_OUTPUT = [
    {
        "client_type": "mac",
        "email": "test@test.com",
        "ip_address": "11.11.11.11",
        "time": "2023-02-22T21:40:41Z",
        "type": "Sign out",
        "version": "5.13.7.15481",
    },
    {
        "client_type": "mac",
        "email": "test@test.com",
        "ip_address": "11.11.11.11",
        "time": "2023-02-22T21:41:41Z",
        "type": "Sign out",
        "version": "5.13.7.15481",
    },
    {
        "client_type": "windows",
        "email": "test2@test.com",
        "ip_address": "192.168.1.1",
        "time": "2023-02-22T21:44:44Z",
        "type": "Sign in",
        "version": "5.13.7.15481",
    },
    {
        "client_type": "mac",
        "email": "test@test.com",
        "ip_address": "11.11.11.11",
        "time": "2023-02-22T21:44:44Z",
        "type": "Sign in",
        "version": "5.13.7.15481",
    },
]

STUB_EXPECTED_PREVIOUS_STATE = {
    "last_request_timestamp": "2023-02-23T22:00:00Z",
    "latest_event_timestamp": "2023-02-22T21:44:44Z",
    "previous_run_state": "starting",
}

STUB_EXPECTED_PAGINATION_ERROR_STATE = {
    "last_request_timestamp": "2023-02-23T22:00:00Z",
    "latest_event_timestamp": "2023-02-22T21:44:44Z",
    "previous_run_state": "starting",
    "next_page_token": "VhJdwkpaVJisdLxsXqfZuIZpwXTOW1IKtOK2",
    "param_end_date": "2023-02-23T22:00:00Z",
    "param_start_date": "2023-02-23T22:00:00Z",
}

STUB_EXPECTED_PAGINATION_ERROR_STATE_OUTPUT = {
    "last_request_timestamp": "2023-02-22T21:44:44Z",
    "latest_event_timestamp": "2023-02-22T21:44:44Z",
    "latest_event_timestamp_latch": None,
    "previous_run_state": "paginating",
}

CUSTOM_LOOKBACK = {"year": 2023, "month": 1, "day": 23, "hour": 22, "minute": 0, "second": 0}
CUSTOM_CUTOFF_DATE = {"date": {"year": 2023, "month": 1, "day": 23, "hour": 22, "minute": 0, "second": 0}}
CUSTOM_CUTOFF_HOURS = {"hours": 744}
STUB_DATETIME_LAST_CUTOFF_HOURS = STUB_DATETIME_NOW - timedelta(hours=CUSTOM_CUTOFF_HOURS.get("hours"))


class TestGetUserActivityEvents(unittest.TestCase):
    @patch(REFRESH_OAUTH_TOKEN_PATH, return_value=None)
    def setUp(self, mock_refresh_call: MagicMock) -> None:
        self.task = Util.default_connector(MonitorSignInOutActivity())

    @patch(GET_DATETIME_LAST_X_HOURS_PATH, side_effect=[STUB_DATETIME_LAST_24_HOURS])
    @patch(GET_DATETIME_NOW_PATH, side_effect=[STUB_DATETIME_NOW])
    @patch(GET_USER_ACTIVITY_EVENTS_PATH, return_value=(STUB_EXPECTED_PREVIOUS_OUTPUT, ""))
    def test_first_run(
        self, mock_call: MagicMock, mock_datetime_now: MagicMock, mock_datetime_last_24: MagicMock
    ) -> None:
        expected_output, expected_has_more_pages, expected_status_code, expected_error = (
            STUB_EXPECTED_PREVIOUS_OUTPUT,
            False,
            200,
            None,
        )
        expected_state = STUB_EXPECTED_PREVIOUS_STATE

        output, state, has_more_pages, status_code, error = self.task.run({})

        self.assertListEqual(output, expected_output)
        self.assertDictEqual(state, expected_state)
        self.assertFalse(has_more_pages, expected_has_more_pages)
        self.assertEqual(status_code, expected_status_code)
        self.assertEqual(error, expected_error)

        validate(output, MonitorSignInOutActivityOutput.schema)
        validate(state, MonitorSignInOutActivityState.schema)

    @patch(GET_DATETIME_LAST_X_HOURS_PATH, side_effect=[STUB_DATETIME_LAST_24_HOURS])
    @patch(GET_DATETIME_NOW_PATH, side_effect=[STUB_DATETIME_NOW + datetime.timedelta(minutes=DEFAULT_TIMEDELTA)])
    @patch(GET_USER_ACTIVITY_EVENTS_PATH, return_value=(STUB_EXPECTED_PREVIOUS_OUTPUT, ""))
    def test_subsequent_run(
        self, mock_call: MagicMock, mock_datetime_now: MagicMock, mock_datetime_last_24: MagicMock
    ) -> None:
        output, state, has_more_pages, status_code, error = self.task.run(state=STUB_EXPECTED_PREVIOUS_STATE)
        expected_output, expected_has_more_pages, expected_status_code, expected_error = [], False, 200, None
        expected_state = {
            "last_request_timestamp": f"{(STUB_DATETIME_NOW + datetime.timedelta(minutes=DEFAULT_TIMEDELTA)).isoformat()}Z",
            "latest_event_timestamp": STUB_EXPECTED_PREVIOUS_STATE.get("latest_event_timestamp", ""),
            "previous_run_state": "continuing",
        }
        self.assertListEqual(output, expected_output)
        self.assertDictEqual(state, expected_state)
        self.assertFalse(output, expected_has_more_pages)
        self.assertEqual(status_code, expected_status_code)
        self.assertEqual(error, expected_error)

        validate(output, MonitorSignInOutActivityOutput.schema)
        validate(state, MonitorSignInOutActivityState.schema)

    @patch(GET_DATETIME_LAST_X_HOURS_PATH, side_effect=[STUB_DATETIME_LAST_24_HOURS])
    @patch(GET_DATETIME_NOW_PATH, side_effect=[STUB_DATETIME_NOW + datetime.timedelta(minutes=DEFAULT_TIMEDELTA)])
    @patch(
        GET_USER_ACTIVITY_EVENTS_PATH,
        side_effect=PluginException(
            preset=PluginException.Preset.BAD_REQUEST,
            data={"code": 300, "message": "The next page token is invalid or expired."},
        ),
    )
    def test_broken_pagination_token_run(
        self, mock_call: MagicMock, mock_datetime_now: MagicMock, mock_datetime_last_24: MagicMock
    ) -> None:
        output, state, has_more_pages, status_code, error = self.task.run(state=STUB_EXPECTED_PAGINATION_ERROR_STATE)
        expected_output, expected_has_more_pages, expected_status_code, expected_error = [], False, 200, None
        expected_state = STUB_EXPECTED_PAGINATION_ERROR_STATE_OUTPUT
        self.assertListEqual(output, expected_output)
        self.assertDictEqual(state, expected_state)
        self.assertFalse(output, expected_has_more_pages)
        self.assertEqual(status_code, expected_status_code)
        self.assertEqual(error, expected_error)

        validate(output, MonitorSignInOutActivityOutput.schema)
        validate(state, MonitorSignInOutActivityState.schema)

    @patch(GET_DATETIME_LAST_X_HOURS_PATH, side_effect=[STUB_DATETIME_LAST_24_HOURS])
    @patch(GET_DATETIME_NOW_PATH, side_effect=[STUB_DATETIME_NOW])
    @patch(GET_USER_ACTIVITY_EVENTS_PATH)
    def test_first_and_subsequent_runs(
        self, mock_call: MagicMock, mock_datetime_now: MagicMock, mock_datetime_last_24: MagicMock
    ) -> None:
        # First run
        first_event_set = [
            {
                "client_type": "mac",
                "email": "test@test.com",
                "ip_address": "11.11.11.11",
                "time": "2023-02-22T21:44:44Z",
                "type": "Sign in",
                "version": "5.13.7.15481",
            },
            {
                "client_type": "mac",
                "email": "test@test.com",
                "ip_address": "22.22.22.22",
                "time": "2023-02-22T21:44:44Z",
                "type": "Sign in",
                "version": "5.13.7.15481",
            },
            {
                "client_type": "mac",
                "email": "test@test.com",
                "ip_address": "33.33.33.33",
                "time": "2023-02-22T21:45:00Z",
                "type": "Sign in",
                "version": "5.13.7.15481",
            },
        ]
        (
            first_expected_output,
            first_expected_state,
            first_expected_has_more_pages,
            first_expected_status_code,
            first_expected_error,
        ) = (
            first_event_set,
            {
                "last_request_timestamp": f"{STUB_DATETIME_NOW.isoformat()}Z",
                "latest_event_timestamp": f"{first_event_set[-1].get('time', '')}",
                "previous_run_state": "starting",
            },
            False,
            200,
            None,
        )
        mock_call.return_value = first_event_set, ""
        output, state, has_more_pages, status_code, error = self.task.run(state={})
        self.assertListEqual(output, first_expected_output)
        self.assertDictEqual(state, first_expected_state)
        self.assertFalse(has_more_pages, first_expected_has_more_pages)
        self.assertEqual(status_code, first_expected_status_code)
        self.assertEqual(error, first_expected_error)

        validate(output, MonitorSignInOutActivityOutput.schema)
        validate(state, MonitorSignInOutActivityState.schema)

        # Second run
        mock_datetime_last_24.side_effect = [STUB_DATETIME_LAST_24_HOURS]
        mock_datetime_now.side_effect = [STUB_DATETIME_NOW + datetime.timedelta(minutes=DEFAULT_TIMEDELTA)]
        second_event_set = [
            {
                "client_type": "mac",
                "email": "test@test.com",
                "ip_address": "55.55.55.55",
                "time": "2023-02-23T21:50:00Z",
                "type": "Sign in",
                "version": "5.13.7.15481",
            },
        ]
        (
            second_expected_output,
            second_expected_state,
            second_expected_has_more_pages,
            second_expected_status_code,
            second_expected_error,
        ) = (
            second_event_set,
            {
                "last_request_timestamp": f"{(STUB_DATETIME_NOW + datetime.timedelta(minutes=DEFAULT_TIMEDELTA)).isoformat()}Z",
                "latest_event_timestamp": second_event_set[-1].get("time", ""),
                "previous_run_state": "continuing",
            },
            False,
            200,
            None,
        )
        mock_call.return_value = second_event_set, False
        output, state, has_more_pages, status_code, error = self.task.run(state=state)
        self.assertListEqual(output, second_expected_output)
        self.assertDictEqual(state, second_expected_state)
        self.assertFalse(has_more_pages, second_expected_has_more_pages)
        self.assertEqual(status_code, second_expected_status_code)
        self.assertEqual(error, second_expected_error)

        validate(output, MonitorSignInOutActivityOutput.schema)
        validate(state, MonitorSignInOutActivityState.schema)

    @patch(GET_DATETIME_NOW_PATH, return_value=datetime.datetime(2000, 1, 1))
    @patch(GET_USER_ACTIVITY_EVENTS_PATH, return_value=([{"test": "value"}], ""))
    def test_api_output_changed_error_catch(self, mock_call: MagicMock, mock_datetime: MagicMock) -> None:
        output, state, has_more_pages, status_code, error = self.task.run(state={})

        expected_state = {
            "last_request_timestamp": "2000-01-01T00:00:00Z",
            "latest_event_timestamp": None,
        }
        expected_output, expected_has_more_pages, expected_status_code, expected_error = (
            [],
            False,
            500,
            PluginException(
                cause=PluginException.causes[PluginException.Preset.SERVER_ERROR],
                assistance=MonitorSignInOutActivity.API_CHANGED_ERROR_MESSAGE_ASSISTANCE,
            ),
        )
        self.assertDictEqual(state, expected_state)
        self.assertListEqual(output, expected_output)
        self.assertFalse(has_more_pages, expected_has_more_pages)
        self.assertEqual(status_code, expected_status_code)
        self.assertEqual(error.cause, expected_error.cause)
        self.assertEqual(error.assistance, expected_error.assistance)

        validate(output, MonitorSignInOutActivityOutput.schema)
        validate(state, MonitorSignInOutActivityState.schema)

    @parameterized.expand(
        [
            (STUB_EVENTS, STUB_EVENTS[0].time, []),
            (STUB_EVENTS, STUB_EVENTS[1].time, [STUB_EVENTS[0]]),
        ]
    )
    def test_dedupe_events(self, events: List[Event], latest_event_time: str, expected: List[Event]) -> None:
        output = self.task._dedupe_events(all_events=events, latest_event_timestamp=latest_event_time)
        self.assertEqual(expected, output)

    @parameterized.expand(
        [
            [
                {
                    "lookback": CUSTOM_LOOKBACK,
                    "cutoff": CUSTOM_CUTOFF_DATE,
                },
                {
                    "start_date": "2023-01-23T22:00:00Z",
                    "end_date": "2023-02-23T22:00:00Z",
                    "page_size": 300,
                    "next_page_token": None,
                },
                STUB_DATETIME_LAST_CUTOFF_HOURS,
            ],
            [
                {
                    "lookback": CUSTOM_LOOKBACK,
                    "cutoff": CUSTOM_CUTOFF_HOURS,
                },
                {
                    "start_date": "2023-01-23T22:00:00Z",
                    "end_date": "2023-02-23T22:00:00Z",
                    "page_size": 300,
                    "next_page_token": None,
                },
                STUB_DATETIME_LAST_CUTOFF_HOURS,
            ],
            [
                {"lookback": CUSTOM_LOOKBACK},
                {
                    "start_date": "2023-01-23T22:00:00Z",
                    "end_date": "2023-02-23T22:00:00Z",
                    "page_size": 300,
                    "next_page_token": None,
                },
                STUB_DATETIME_LAST_24_HOURS,
            ],
            [
                {
                    "cutoff": CUSTOM_CUTOFF_HOURS,
                },
                {
                    "start_date": "2023-01-23T22:00:00Z",
                    "end_date": "2023-02-23T22:00:00Z",
                    "page_size": 300,
                    "next_page_token": None,
                },
                STUB_DATETIME_LAST_CUTOFF_HOURS,
            ],
            [
                {},
                {
                    "start_date": "2023-02-22T22:00:00Z",
                    "end_date": "2023-02-23T22:00:00Z",
                    "page_size": 300,
                    "next_page_token": None,
                },
                STUB_DATETIME_LAST_24_HOURS,
            ],
        ]
    )
    @patch(GET_DATETIME_LAST_X_HOURS_PATH)
    @patch(GET_DATETIME_NOW_PATH, side_effect=[STUB_DATETIME_NOW])
    @patch(GET_USER_ACTIVITY_EVENTS_PATH, return_value=(STUB_EXPECTED_PREVIOUS_OUTPUT, ""))
    def test_first_run_with_backfill_logic(
        self,
        custom_config: dict,
        expected_api_call_params: dict,
        mock_last_x_hours: str,
        mock_call: MagicMock,
        mock_datetime_now: MagicMock,
        mock_datetime_last_x: MagicMock,
    ) -> None:
        mock_datetime_last_x.side_effect = [mock_last_x_hours]

        expected_output, expected_has_more_pages, expected_status_code, expected_error = (
            STUB_EXPECTED_PREVIOUS_OUTPUT,
            False,
            200,
            None,
        )
        expected_state = STUB_EXPECTED_PREVIOUS_STATE

        output, state, has_more_pages, status_code, error = self.task.run(state={}, custom_config=custom_config)

        self.assertListEqual(output, expected_output)
        self.assertDictEqual(state, expected_state)
        self.assertFalse(has_more_pages, expected_has_more_pages)
        self.assertEqual(status_code, expected_status_code)
        self.assertEqual(error, expected_error)

        validate(output, MonitorSignInOutActivityOutput.schema)
        validate(state, MonitorSignInOutActivityState.schema)

        mock_call.assert_called_with(
            start_date=expected_api_call_params.get("start_date"),
            end_date=expected_api_call_params.get("end_date"),
            page_size=expected_api_call_params.get("page_size"),
            next_page_token=expected_api_call_params.get("next_page_token"),
        )

    @patch(GET_DATETIME_LAST_X_HOURS_PATH, side_effect=[STUB_DATETIME_LAST_24_HOURS])
    @patch(GET_DATETIME_NOW_PATH, side_effect=[STUB_DATETIME_FUTURE])
    @patch(GET_USER_ACTIVITY_EVENTS_PATH, return_value=(STUB_EXPECTED_PREVIOUS_OUTPUT, ""))
    def test_backfill_continiuous_pagination(
        self, mock_call: MagicMock, mock_datetime_now: MagicMock, mock_datetime_last_24: MagicMock
    ) -> None:
        state = {
            "param_end_date": "2023-02-23T22:00:00Z",
            "param_start_date": "2023-02-22T21:44:44Z",
            "previous_run_state": "paginating",
            "next_page_token": "123456789abcdefgh",
        }

        expected_output, expected_has_more_pages, expected_status_code, expected_error = (
            STUB_EXPECTED_PREVIOUS_OUTPUT,
            True,
            200,
            None,
        )

        expected_state = {"previous_run_state": "paginating", "last_request_timestamp": "2024-02-23T22:00:00Z"}

        output, state, has_more_pages, status_code, error = self.task.run(state=state)

        self.assertListEqual(output, expected_output)
        self.assertDictEqual(state, expected_state)
        self.assertEqual(has_more_pages, expected_has_more_pages)
        self.assertEqual(status_code, expected_status_code)
        self.assertEqual(error, expected_error)

        validate(output, MonitorSignInOutActivityOutput.schema)
        validate(state, MonitorSignInOutActivityState.schema)
