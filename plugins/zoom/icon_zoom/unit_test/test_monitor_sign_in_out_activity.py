import logging
import unittest
from unittest.mock import Mock
from unittest.mock import patch

from icon_zoom.util.event import Event
from icon_zoom.util.api import ZoomAPI
from icon_zoom.tasks.monitor_sign_in_out_activity.task import MonitorSignInOutActivity
from icon_zoom.tasks.monitor_sign_in_out_activity.schema import Input
from icon_zoom.connection.connection import Connection
from icon_zoom.unit_test.mock import (
    STUB_CONNECTION
)

GET_USER_ACTIVITY_EVENTS_PATH = "icon_zoom.util.api.ZoomAPI.get_user_activity_events"


class TestGetUserActivityEvents(unittest.TestCase):

    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = MonitorSignInOutActivity()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")
        self.params = {}

    @patch(GET_USER_ACTIVITY_EVENTS_PATH)
    def test_first_run(self, mock_call):
        expected_output = [{
            "client_type": "mac",
            "email": "test@test.com",
            "ip_address": "11.11.11.11",
            "time": "2023-02-22T21:44:44Z",
            "type": "Sign in",
            "version": "5.13.7.15481"
        }, {
            "client_type": "windows",
            "email": "test2@test.com",
            "ip_address": "192.168.1.1",
            "time": "2023-02-22T21:44:44Z",
            "type": "Sign in",
            "version": "5.13.7.15481"
        }, {
            "client_type": "mac",
            "email": "test@test.com",
            "ip_address": "11.11.11.11",
            "time": "2023-02-22T21:41:41Z",
            "type": "Sign out",
            "version": "5.13.7.15481"
        }, {
            "client_type": "mac",
            "email": "test@test.com",
            "ip_address": "11.11.11.11",
            "time": "2023-02-22T21:40:41Z",
            "type": "Sign out",
            "version": "5.13.7.15481"
        }]
        expected_state = {
            'boundary_events': ['197f96ef45ad08592bfea604f60b6abcfc7d4bf2', '8c68922ce0e81f42e4db701317aa7f219049b144'],
            'last_event_time': '2023-02-22T21:44:44Z'}

        mock_call.return_value = expected_output

        output, state = self.action.run({})

        self.assertDictEqual(state, expected_state)
        self.assertListEqual(output, expected_output)

    @patch(GET_USER_ACTIVITY_EVENTS_PATH)
    def test_subsequent_run(self, mock_call):
        previous_output = [{
            "client_type": "mac",
            "email": "test@test.com",
            "ip_address": "11.11.11.11",
            "time": "2023-02-22T21:44:44Z",
            "type": "Sign in",
            "version": "5.13.7.15481"
        }, {
            "client_type": "windows",
            "email": "test2@test.com",
            "ip_address": "192.168.1.1",
            "time": "2023-02-22T21:44:44Z",
            "type": "Sign in",
            "version": "5.13.7.15481"
        }, {
            "client_type": "mac",
            "email": "test@test.com",
            "ip_address": "11.11.11.11",
            "time": "2023-02-22T21:41:41Z",
            "type": "Sign out",
            "version": "5.13.7.15481"
        }, {
            "client_type": "mac",
            "email": "test@test.com",
            "ip_address": "11.11.11.11",
            "time": "2023-02-22T21:40:41Z",
            "type": "Sign out",
            "version": "5.13.7.15481"
        }]
        expected_output = [{
            "client_type": "mac",
            "email": "test@test.com",
            "ip_address": "11.11.11.11",
            "time": "2023-02-22T21:41:41Z",
            "type": "Sign out",
            "version": "5.13.7.15481"
        }, {
            "client_type": "mac",
            "email": "test@test.com",
            "ip_address": "11.11.11.11",
            "time": "2023-02-22T21:40:41Z",
            "type": "Sign out",
            "version": "5.13.7.15481"
        }]
        expected_state = {
            'boundary_events': ['197f96ef45ad08592bfea604f60b6abcfc7d4bf2', '8c68922ce0e81f42e4db701317aa7f219049b144'],
            'last_event_time': '2023-02-22T21:44:44Z'}

        mock_call.return_value = previous_output

        output, state = self.action.run(state=expected_state)

        self.assertDictEqual(state, expected_state)
        self.assertListEqual(output, expected_output)

    @patch(GET_USER_ACTIVITY_EVENTS_PATH)
    def test_first_and_subsequent_runs(self, mock_call):
        # First API call patch
        first_event_set = [{
            "client_type": "mac",
            "email": "test@test.com",
            "ip_address": "11.11.11.11",
            "time": "2023-02-22T21:44:44Z",
            "type": "Sign in",
            "version": "5.13.7.15481"
        }, {
            "client_type": "mac",
            "email": "test@test.com",
            "ip_address": "22.22.22.22",
            "time": "2023-02-22T21:44:44Z",
            "type": "Sign in",
            "version": "5.13.7.15481"
        }, {
            "client_type": "mac",
            "email": "test@test.com",
            "ip_address": "33.33.33.33",
            "time": "2023-02-22T21:45:00Z",
            "type": "Sign in",
            "version": "5.13.7.15481"
        }]
        # Second API call patch
        second_event_set = [
            {
                "client_type": "mac",
                "email": "test@test.com",
                "ip_address": "55.55.55.55",
                "time": "2023-02-23T21:44:44Z",
                "type": "Sign in",
                "version": "5.13.7.15481"
            }, {
                "client_type": "mac",
                "email": "test@test.com",
                "ip_address": "11.11.11.11",
                "time": "2023-02-22T21:44:44Z",
                "type": "Sign in",
                "version": "5.13.7.15481"
            }
        ]
        first_expected_output = [{
            "client_type": "mac",
            "email": "test@test.com",
            "ip_address": "11.11.11.11",
            "time": "2023-02-22T21:44:44Z",
            "type": "Sign in",
            "version": "5.13.7.15481"
        }, {
            "client_type": "mac",
            "email": "test@test.com",
            "ip_address": "22.22.22.22",
            "time": "2023-02-22T21:44:44Z",
            "type": "Sign in",
            "version": "5.13.7.15481"
        }, {
            "client_type": "mac",
            "email": "test@test.com",
            "ip_address": "33.33.33.33",
            "time": "2023-02-22T21:45:00Z",
            "type": "Sign in",
            "version": "5.13.7.15481"
        }]
        second_expected_output = [{
            "client_type": "mac",
            "email": "test@test.com",
            "ip_address": "55.55.55.55",
            "time": "2023-02-23T21:44:44Z",
            "type": "Sign in",
            "version": "5.13.7.15481"
        }]
        first_expected_state = {
            "boundary_events": ["197f96ef45ad08592bfea604f60b6abcfc7d4bf2", "3a28377b757a9185440cc939842067c72d13a054"],
            "last_event_time": "2023-02-22T21:44:44Z"
        }
        second_expected_state = {
            "boundary_events": ["b308ba69b3beb7207f8271ef7a78f84da98bed67"],
            "last_event_time": "2023-02-23T21:44:44Z"
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

    def test_get_boundary_hashes_two_same_time(self):
        samples = [{
            "client_type": "mac",
            "email": "test@test.com",
            "ip_address": "11.11.11.11",
            "time": "2023-02-22T21:44:44Z",
            "type": "Sign in",
            "version": "5.13.7.15481"
        }, {
            "client_type": "windows",
            "email": "test2@test.com",
            "ip_address": "192.168.1.1",
            "time": "2023-02-22T21:44:44Z",
            "type": "Sign in",
            "version": "5.13.7.15481"
        }, {
            "client_type": "mac",
            "email": "test@test.com",
            "ip_address": "11.11.11.11",
            "time": "2023-02-22T21:41:41Z",
            "type": "Sign out",
            "version": "5.13.7.15481"
        }, {
            "client_type": "mac",
            "email": "test@test.com",
            "ip_address": "11.11.11.11",
            "time": "2023-02-22T21:40:41Z",
            "type": "Sign out",
            "version": "5.13.7.15481"
        }]

        events = [Event(**s) for s in samples]
        task = MonitorSignInOutActivity()
        got = task._get_boundary_event_hashes(latest_event_time="2023-02-22T21:44:44Z", events=events)

        expected = [
            "197f96ef45ad08592bfea604f60b6abcfc7d4bf2",
            "8c68922ce0e81f42e4db701317aa7f219049b144"
        ]

        self.assertEqual(got, expected)

    def test_dedupe_events(self):
        samples = [{
            "client_type": "mac",
            "email": "test@test.com",
            "ip_address": "11.11.11.11",
            "time": "2023-02-22T21:44:44Z",
            "type": "Sign in",
            "version": "5.13.7.15481"
        }, {
            "client_type": "windows",
            "email": "test2@test.com",
            "ip_address": "192.168.1.1",
            "time": "2023-02-22T21:44:44Z",
            "type": "Sign in",
            "version": "5.13.7.15481"
        }, {
            "client_type": "mac",
            "email": "test@test.com",
            "ip_address": "11.11.11.11",
            "time": "2023-02-22T21:41:41Z",
            "type": "Sign out",
            "version": "5.13.7.15481"
        }, {
            "client_type": "mac",
            "email": "test@test.com",
            "ip_address": "11.11.11.11",
            "time": "2023-02-22T21:40:41Z",
            "type": "Sign out",
            "version": "5.13.7.15481"
        }]

        deduped_event_samples = [{
            "client_type": "mac",
            "email": "test@test.com",
            "ip_address": "11.11.11.11",
            "time": "2023-02-22T21:41:41Z",
            "type": "Sign out",
            "version": "5.13.7.15481"
        }, {
            "client_type": "mac",
            "email": "test@test.com",
            "ip_address": "11.11.11.11",
            "time": "2023-02-22T21:40:41Z",
            "type": "Sign out",
            "version": "5.13.7.15481"
        }]

        all_events = [Event(**s) for s in samples]
        boundary_hashes = [
            "197f96ef45ad08592bfea604f60b6abcfc7d4bf2",
            "8c68922ce0e81f42e4db701317aa7f219049b144"
        ]

        task = MonitorSignInOutActivity()
        expected = [Event(**s) for s in deduped_event_samples]
        got = task._dedupe_events(boundary_event_hashes=boundary_hashes, new_events=all_events)

        self.assertEqual(expected, got)

    def test_dedupe_events_no_dupes(self):
        samples = [{
            "client_type": "mac",
            "email": "test@test.com",
            "ip_address": "11.11.11.11",
            "time": "2023-02-22T21:44:44Z",
            "type": "Sign in",
            "version": "5.13.7.15481"
        }, {
            "client_type": "windows",
            "email": "test2@test.com",
            "ip_address": "192.168.1.1",
            "time": "2023-02-22T21:44:44Z",
            "type": "Sign in",
            "version": "5.13.7.15481"
        }, {
            "client_type": "mac",
            "email": "test@test.com",
            "ip_address": "11.11.11.11",
            "time": "2023-02-22T21:41:41Z",
            "type": "Sign out",
            "version": "5.13.7.15481"
        }, {
            "client_type": "mac",
            "email": "test@test.com",
            "ip_address": "11.11.11.11",
            "time": "2023-02-22T21:40:41Z",
            "type": "Sign out",
            "version": "5.13.7.15481"
        }]

        all_events = [Event(**s) for s in samples]
        boundary_hashes = [
            "197f96ef45ad08592bfea604f60b6abcfc7d4bfc",
            "8c68922ce0e81f42e4db701317aa7f219049b146"
        ]

        task = MonitorSignInOutActivity()
        got = task._dedupe_events(boundary_event_hashes=boundary_hashes, new_events=all_events)

        self.assertEqual(all_events, got)


if __name__ == '__main__':
    unittest.main()
