import logging
import unittest
import datetime
from unittest.mock import patch

from icon_zoom.util.event import Event
from icon_zoom.tasks.monitor_sign_in_out_activity.task import MonitorSignInOutActivity
from icon_zoom.connection.connection import Connection
from mock import STUB_CONNECTION, STUB_OAUTH_TOKEN

REFRESH_OAUTH_TOKEN_PATH = "icon_zoom.util.api.ZoomAPI._refresh_oauth_token"
GET_USER_ACTIVITY_EVENTS_PATH = "icon_zoom.util.api.ZoomAPI.get_user_activity_events"
GET_DATETIME_NOW_PATH = "icon_zoom.tasks.monitor_sign_in_out_activity.task.MonitorSignInOutActivity._get_datetime_now"
GET_DATETIME_LAST_24_HOURS_PATH = (
    "icon_zoom.tasks.monitor_sign_in_out_activity.task.MonitorSignInOutActivity._get_datetime_last_24_hours"
)


class TestGetUserActivityEvents(unittest.TestCase):
    @patch(REFRESH_OAUTH_TOKEN_PATH)
    def setUp(self, mock_refresh_call) -> None:
        mock_refresh_call.return_value = None
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)
        self.connection.zoom_api.oauth_token = STUB_OAUTH_TOKEN

        self.action = MonitorSignInOutActivity()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")
        self.params = {}

    @patch(GET_DATETIME_LAST_24_HOURS_PATH)
    @patch(GET_DATETIME_NOW_PATH)
    @patch(GET_USER_ACTIVITY_EVENTS_PATH)
    def test_first_run(self, mock_call, mock_datetime_now, mock_datetime_last_24):
        mock_datetime_now.side_effect = [
            datetime.datetime.fromtimestamp(1677211200),  # 2023-02-23 22:00:00, first run, "now"
        ]

        mock_datetime_last_24.side_effect = [
            datetime.datetime.fromtimestamp(1677124800),  # 2023-02-22 22:00:00, first run, "last 24"
        ]

        expected_output = [
            {
                "client_type": "mac",
                "email": "test@test.com",
                "ip_address": "11.11.11.11",
                "time": "2023-02-22T21:44:44Z",
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
        expected_state = {
            "boundary_events": ["197f96ef45ad08592bfea604f60b6abcfc7d4bf2", "8c68922ce0e81f42e4db701317aa7f219049b144"],
            "last_request_timestamp": "2023-02-23T22:00:00Z",
            "latest_event_timestamp": "2023-02-22T21:44:44Z",
            "status_code": 200,
        }

        mock_call.return_value = expected_output

        output, state = self.action.run({})

        self.assertDictEqual(state, expected_state)
        self.assertListEqual(output, expected_output)

    @patch(GET_USER_ACTIVITY_EVENTS_PATH)
    def test_subsequent_run(self, mock_call):
        previous_output = [
            {
                "client_type": "mac",
                "email": "test@test.com",
                "ip_address": "11.11.11.11",
                "time": "2023-02-22T21:44:44Z",
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
        expected_output = []
        expected_state = {
            "boundary_events": ["197f96ef45ad08592bfea604f60b6abcfc7d4bf2", "8c68922ce0e81f42e4db701317aa7f219049b144"],
            "last_request_timestamp": "2023-02-22T21:44:44Z",
            "latest_event_timestamp": "2023-02-22T21:44:44Z",
        }

        mock_call.return_value = previous_output

        output, state = self.action.run(state=expected_state)

        self.assertDictEqual(state, expected_state)
        self.assertListEqual(output, expected_output)

    @patch(GET_DATETIME_LAST_24_HOURS_PATH)
    @patch(GET_DATETIME_NOW_PATH)
    @patch(GET_USER_ACTIVITY_EVENTS_PATH)
    def test_first_and_subsequent_runs(self, mock_call, mock_datetime_now, mock_datetime_last_24):
        mock_datetime_now.side_effect = [
            datetime.datetime.fromtimestamp(1677211200),  # 2023-02-23 22:00:00, first run, "now"
            datetime.datetime.fromtimestamp(1677214800),  # 2023-02-23 23:00:00, subs. run, "1 hour after first run"
        ]

        mock_datetime_last_24.side_effect = [
            datetime.datetime.fromtimestamp(1677124800),  # 2023-02-22 22:00:00, first run, "last 24"
        ]

        # First API call patch
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
        # Second API call patch
        second_event_set = [
            {
                "client_type": "mac",
                "email": "test@test.com",
                "ip_address": "55.55.55.55",
                "time": "2023-02-23T21:44:44Z",
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
        first_expected_output = [
            {
                "client_type": "mac",
                "email": "test@test.com",
                "ip_address": "33.33.33.33",
                "time": "2023-02-22T21:45:00Z",
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
            {
                "client_type": "mac",
                "email": "test@test.com",
                "ip_address": "22.22.22.22",
                "time": "2023-02-22T21:44:44Z",
                "type": "Sign in",
                "version": "5.13.7.15481",
            },
        ]
        second_expected_output = [
            {
                "client_type": "mac",
                "email": "test@test.com",
                "ip_address": "55.55.55.55",
                "time": "2023-02-23T21:44:44Z",
                "type": "Sign in",
                "version": "5.13.7.15481",
            }
        ]
        first_expected_state = {
            "boundary_events": ["854d8b971985244502ba5714f372344a9374c538"],
            "last_request_timestamp": "2023-02-23T22:00:00Z",
            "latest_event_timestamp": "2023-02-22T21:45:00Z",
            "status_code": 200,
        }
        second_expected_state = {
            "boundary_events": ["b308ba69b3beb7207f8271ef7a78f84da98bed67"],
            "last_request_timestamp": "2023-02-23T23:00:00Z",
            "latest_event_timestamp": "2023-02-23T21:44:44Z",
            "status_code": 200,
        }

        # First run
        mock_call.return_value = first_event_set
        output, state = self.action.run(state={})
        self.assertDictEqual(state, first_expected_state)
        self.assertListEqual(output, first_expected_output)

        # Subsequent run
        mock_call.return_value = second_event_set
        output, state = self.action.run(state=state)  # Using state from first run to trigger subsequent run
        self.assertDictEqual(state, second_expected_state)
        self.assertListEqual(output, second_expected_output)

    @patch(GET_DATETIME_NOW_PATH)
    @patch(GET_USER_ACTIVITY_EVENTS_PATH)
    def test_api_output_changed_error_catch(self, mock_call, mock_datetime):
        mock_call.return_value = [{"test": "value"}]
        mock_datetime.return_value = datetime.datetime(2000, 1, 1)
        output, state = self.action.run(state={})

        expected_state = {
            "boundary_events": [],
            "last_request_timestamp": "2000-01-01T00:00:00Z",
            "latest_event_timestamp": None,
            "status_code": 500,
        }
        expected_output = []
        self.assertDictEqual(state, expected_state)
        self.assertListEqual(output, expected_output)

    def test_get_boundary_hashes_two_same_time(self):
        samples = [
            {
                "client_type": "mac",
                "email": "test@test.com",
                "ip_address": "11.11.11.11",
                "time": "2023-02-22T21:44:44Z",
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

        events = [Event(**s) for s in samples]
        task = MonitorSignInOutActivity()
        got = task._get_boundary_event_hashes(latest_event_time="2023-02-22T21:44:44Z", events=events)

        expected = ["197f96ef45ad08592bfea604f60b6abcfc7d4bf2", "8c68922ce0e81f42e4db701317aa7f219049b144"]

        self.assertEqual(got, expected)

    def test_dedupe_events(self):
        samples = [
            {
                "client_type": "mac",
                "email": "test@test.com",
                "ip_address": "11.11.11.11",
                "time": "2023-02-22T21:44:44Z",
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

        all_events = [Event(**s) for s in samples]
        boundary_hashes = ["197f96ef45ad08592bfea604f60b6abcfc7d4bf2", "8c68922ce0e81f42e4db701317aa7f219049b144"]

        task = MonitorSignInOutActivity()
        expected = []
        got = task._dedupe_events(
            boundary_event_hashes=boundary_hashes, all_events=all_events, latest_event_timestamp=all_events[0].time
        )

        self.assertEqual(expected, got)

    def test_dedupe_events_partial_dupes(self):
        samples = [
            {
                "client_type": "mac",
                "email": "test@test.com",
                "ip_address": "11.11.11.11",
                "time": "2023-02-22T21:44:44Z",
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

        all_events = [Event(**s) for s in samples]
        boundary_hashes = ["197f96ef45ad08592bfea604f60b6abcfc7d4bfc", "8c68922ce0e81f42e4db701317aa7f219049b146"]

        task = MonitorSignInOutActivity()
        got = task._dedupe_events(
            boundary_event_hashes=boundary_hashes, all_events=all_events, latest_event_timestamp=all_events[0].time
        )

        self.assertEqual(all_events[:2], got)


if __name__ == "__main__":
    unittest.main()
