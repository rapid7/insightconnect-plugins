import sys
from typing import Any, Dict, List

sys.path.append("../")

import datetime
import logging
import unittest
from unittest.mock import MagicMock, patch

from icon_zoom.connection.connection import Connection
from icon_zoom.tasks.monitor_sign_in_out_activity.task import MonitorSignInOutActivity
from icon_zoom.util.event import Event
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

from mock import STUB_CONNECTION, STUB_OAUTH_TOKEN, Util

REFRESH_OAUTH_TOKEN_PATH = "icon_zoom.util.api.ZoomAPI._refresh_oauth_token"
GET_USER_ACTIVITY_EVENTS_PATH = "icon_zoom.util.api.ZoomAPI.get_user_activity_events_task"
GET_DATETIME_NOW_PATH = "icon_zoom.tasks.monitor_sign_in_out_activity.task.MonitorSignInOutActivity._get_datetime_now"
GET_DATETIME_LAST_24_HOURS_PATH = (
    "icon_zoom.tasks.monitor_sign_in_out_activity.task.MonitorSignInOutActivity._get_datetime_last_24_hours"
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


class TestGetUserActivityEvents(unittest.TestCase):
    @patch(REFRESH_OAUTH_TOKEN_PATH, return_value=None)
    def setUp(self, mock_refresh_call: MagicMock) -> None:
        self.task = Util.default_connector(MonitorSignInOutActivity())

    @patch(GET_DATETIME_LAST_24_HOURS_PATH, side_effect=[STUB_DATETIME_LAST_24_HOURS])
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

    @patch(GET_DATETIME_LAST_24_HOURS_PATH, side_effect=[STUB_DATETIME_LAST_24_HOURS])
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

    @patch(GET_DATETIME_LAST_24_HOURS_PATH, side_effect=[STUB_DATETIME_LAST_24_HOURS])
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

    @parameterized.expand(
        [
            (STUB_EVENTS, STUB_EVENTS[0].time, []),
            (STUB_EVENTS, STUB_EVENTS[1].time, [STUB_EVENTS[0]]),
        ]
    )
    def test_dedupe_events(self, events: List[Event], latest_event_time: str, expected: List[Event]) -> None:
        output = self.task._dedupe_events(all_events=events, latest_event_timestamp=latest_event_time)
        self.assertEqual(expected, output)
