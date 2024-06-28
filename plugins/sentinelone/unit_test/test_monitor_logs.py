import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from komand_sentinelone.tasks.monitor_logs import MonitorLogs
from komand_sentinelone.tasks.monitor_logs.schema import MonitorLogsOutput, Input
from util import Util
from parameterized import parameterized
from jsonschema import validate
from freezegun import freeze_time


STUB_INPUT_PARAMS = {
    Input.COLLECTACTIVITIES: True,
    Input.COLLECTEVENTS: True,
    Input.COLLECTTHREATS: True,
}

STUB_STATE = {
    "activities_last_log_timestamp": "1999-12-31T00:00:00.000000Z",
    "activities_page_cursor": "YWdlbnRfaWQ6NTgwMjkzODE=",
    "events_last_log_timestamp": "1999-12-31T00:00:00.000000Z",
    "events_page_cursor": "YWdlbnRfaWQ6NTgwMjkzODE=",
    "last_run_timestamp": "1999-12-31T00:00:00.000000Z",
    "threats_last_log_timestamp": "1999-12-31T00:00:00.000000Z",
    "threats_page_cursor": "YWdlbnRfaWQ6NTgwMjkzODE=",
}

STUB_STATE_NO_CURSOR = {
    "activities_last_log_timestamp": "1999-12-31T00:00:00.000000Z",
    "events_last_log_timestamp": "1999-12-31T00:00:00.000000Z",
    "last_run_timestamp": "1999-12-31T00:00:00.000000Z",
    "threats_last_log_timestamp": "1999-12-31T00:00:00.000000Z",
}

STUB_STATE_EXPECTED = {
    "activities_last_log_timestamp": "1999-12-31T00:00:00.000000Z",
    "activities_page_cursor": "YWdlbnRfaWQ6NTgwMjkzODE=",
    "events_last_log_timestamp": "1999-12-31T00:00:00.000000Z",
    "events_page_cursor": "YWdlbnRfaWQ6NTgwMjkzODE=",
    "threats_last_log_timestamp": "1999-12-31T00:00:00.000000Z",
    "threats_page_cursor": "YWdlbnRfaWQ6NTgwMjkzODE=",
}

STUB_STATE_ACTIVITIES = {
    "activities_last_log_timestamp": "1999-12-31T00:00:00.000000Z",
    "activities_page_cursor": "YWdlbnRfaWQ6NTgwMjkzODE=",
}

STUB_STATE_EVENTS = {
    "events_last_log_timestamp": "1999-12-31T00:00:00.000000Z",
    "events_page_cursor": "YWdlbnRfaWQ6NTgwMjkzODE=",
}

STUB_STATE_THREATS = {
    "threats_last_log_timestamp": "1999-12-31T00:00:00.000000Z",
    "threats_page_cursor": "YWdlbnRfaWQ6NTgwMjkzODE=",
}

STUB_STATE_LOOKBACK = {
    "activities_last_log_timestamp": "1999-12-31T00:00:00.000000Z",
    "activities_page_cursor": "YWdlbnRfaWQ6NTgwMjkzODE=",
    "events_last_log_timestamp": "1999-12-31T00:00:00.000000Z",
    "events_page_cursor": "YWdlbnRfaWQ6NTgwMjkzODE=",
    "last_run_timestamp": "1999-12-30T00:00:00.000000Z",
    "threats_last_log_timestamp": "1999-12-31T00:00:00.000000Z",
    "threats_page_cursor": "YWdlbnRfaWQ6NTgwMjkzODE=",
}

STUB_STATE_CONTINUATION = {
    "activities_last_log_timestamp": "1999-12-31T00:00:00.000000Z",
    "activities_page_cursor": None,
    "events_last_log_timestamp": "1999-12-31T00:00:00.000000Z",
    "events_page_cursor": None,
    "last_run_timestamp": "1999-12-30T00:00:00.000000Z",
    "threats_last_log_timestamp": "1999-12-31T00:00:00.000000Z",
    "threats_page_cursor": None,
}

STUB_STATE_ACTIVITIES_401 = {
    "activities_last_log_timestamp": "1999-12-31T00:00:00.000000Z",
    "activities_page_cursor": "ZWdlbnRfaWQ6NTgwMjkzODE=",
    "events_last_log_timestamp": "1999-12-31T00:00:00.000000Z",
    "events_page_cursor": "YWdlbnRfaWQ6NTgwMjkzODE=",
    "last_run_timestamp": "1999-12-31T00:00:00.000000Z",
    "threats_last_log_timestamp": "1999-12-31T00:00:00.000000Z",
    "threats_page_cursor": "YWdlbnRfaWQ6NTgwMjkzODE=",
}


@freeze_time("2000-01-01T00:00:00.000000Z")
@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestMonitorLogs(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.task = Util.default_connector(MonitorLogs())

    @parameterized.expand(
        [
            [
                "starting",
                STUB_INPUT_PARAMS,
                {},
                {},
                Util.read_file_to_dict("expected/monitor_logs.json.exp"),
                STUB_STATE_EXPECTED,
                True,
                200,
                None,
            ],
            [
                "continuation",
                STUB_INPUT_PARAMS,
                STUB_STATE_NO_CURSOR,
                {},
                Util.read_file_to_dict("expected/monitor_logs.json.exp"),
                STUB_STATE.copy(),
                True,
                200,
                None,
            ],
            [
                "pagination",
                STUB_INPUT_PARAMS,
                STUB_STATE.copy(),
                {},
                Util.read_file_to_dict("expected/monitor_logs.json.exp"),
                STUB_STATE.copy(),
                True,
                200,
                None,
            ],
            [
                "activities",
                {Input.COLLECTACTIVITIES: True},
                {},
                {},
                [Util.read_file_to_dict("expected/monitor_logs.json.exp")[0]],
                STUB_STATE_ACTIVITIES,
                True,
                200,
                None,
            ],
            [
                "events",
                {Input.COLLECTEVENTS: True},
                {},
                {},
                [Util.read_file_to_dict("expected/monitor_logs.json.exp")[1]],
                STUB_STATE_EVENTS,
                True,
                200,
                None,
            ],
            [
                "threats",
                {Input.COLLECTTHREATS: True},
                {},
                {},
                [Util.read_file_to_dict("expected/monitor_logs.json.exp")[2]],
                STUB_STATE_THREATS,
                True,
                200,
                None,
            ],
        ]
    )
    def test_monitor_logss(
        self,
        mock_request,
        test_name,
        input,
        state,
        custom_config,
        expected_output,
        expected_state,
        expected_has_more_pages,
        expected_status_code,
        expected_error,
    ):
        output, state, has_more_pages, status_code, error = self.task.run(
            params=input, state=state, custom_config=custom_config
        )
        self.assertEqual(expected_output, output)
        self.assertEqual(expected_state, state)
        self.assertEqual(expected_has_more_pages, has_more_pages)
        self.assertEqual(expected_status_code, status_code)
        self.assertEqual(expected_error, error)
        validate(output, MonitorLogsOutput.schema)

    @parameterized.expand(
        [
            [
                "cutoff",
                STUB_INPUT_PARAMS,
                {},
                {"cutoff": 48},
                Util.read_file_to_dict("expected/monitor_logs.json.exp"),
                STUB_STATE_EXPECTED,
                True,
                200,
                None,
            ],
            [
                "cutoff_lookback",
                STUB_INPUT_PARAMS,
                {},
                {"cutoff": 48, "lookback": {"year": 1999, "month": 12, "day": 30, "hour": 0, "minute": 0, "second": 0}},
                Util.read_file_to_dict("expected/monitor_logs.json.exp"),
                STUB_STATE_EXPECTED,
                True,
                200,
                None,
            ],
            [
                "lookback_continuation",
                STUB_INPUT_PARAMS,
                STUB_STATE_CONTINUATION,
                {"cutoff": 48, "lookback": {"year": 1999, "month": 12, "day": 30, "hour": 0, "minute": 0, "second": 0}},
                Util.read_file_to_dict("expected/monitor_logs.json.exp"),
                STUB_STATE_CONTINUATION,
                True,
                200,
                None,
            ],
            [
                "lookback_pagination",
                {Input.COLLECTACTIVITIES: True},
                STUB_STATE,
                {"cutoff": 48, "lookback": {"year": 1999, "month": 12, "day": 30, "hour": 0, "minute": 0, "second": 0}},
                [Util.read_file_to_dict("expected/monitor_logs.json.exp")[0]],
                STUB_STATE,
                True,
                200,
                None,
            ],
        ]
    )
    def test_monitor_logs_custom_config(
        self,
        mock_request,
        test_name,
        input,
        state,
        custom_config,
        expected_output,
        expected_state,
        expected_has_more_pages,
        expected_status_code,
        expected_error,
    ):
        output, state, has_more_pages, status_code, error = self.task.run(
            params=input, state=state, custom_config=custom_config
        )
        self.assertEqual(expected_output, output)
        self.assertEqual(expected_state, state)
        self.assertEqual(expected_has_more_pages, has_more_pages)
        self.assertEqual(expected_status_code, status_code)
        self.assertEqual(expected_error, error)
        validate(output, MonitorLogsOutput.schema)

    @parameterized.expand(
        [
            [
                "400",
                {"activities_page_cursor": "400"},
                400,
                "The server is unable to process the request.",
                "Verify your plugin input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
            [
                "401",
                {"activities_page_cursor": "401"},
                401,
                "The account configured in your connection is unauthorized to access this service.",
                "Verify the permissions for your account and try again.",
            ],
            [
                "403",
                {"activities_page_cursor": "403"},
                401,
                "The account configured in your connection is unauthorized to access this service.",
                "Verify the permissions for your account and try again.",
            ],
            [
                "404",
                {"activities_page_cursor": "404"},
                404,
                "Invalid or unreachable endpoint provided.",
                "Verify the URLs or endpoints in your configuration are correct.",
            ],
            [
                "500",
                {"activities_page_cursor": "500"},
                500,
                "Server error occurred",
                "Verify your plugin connection inputs are correct and not malformed and try again. If the issue persists, please contact support.",
            ],
        ]
    )
    def test_monitor_logs_api_errors(
        self, mock_request, test_name, state, expected_status_code, expected_cause, expected_assistance
    ):
        output, state, has_more_pages, status_code, error = self.task.run(
            params={Input.COLLECTACTIVITIES: True}, state=state
        )
        self.assertEqual(False, has_more_pages)
        self.assertEqual(expected_status_code, status_code)
        self.assertEqual(expected_cause, error.cause)
        self.assertEqual(expected_assistance, error.assistance)

    def test_monitor_logs_forbidden_error(self, mock_request):
        params = STUB_INPUT_PARAMS
        state = STUB_STATE_ACTIVITIES_401
        output, state, has_more_pages, status_code, error = self.task.run(params=params, state=state)
        expected_output = Util.read_file_to_dict("expected/monitor_logs.json.exp")[1:]
        expected_state = STUB_STATE
        expected_state["activities_page_cursor"] = None
        self.assertEqual(expected_output, output)
        self.assertEqual(expected_state, state)
        self.assertEqual(True, has_more_pages)
        self.assertEqual(200, status_code)
        self.assertEqual(None, error)
        validate(output, MonitorLogsOutput.schema)
