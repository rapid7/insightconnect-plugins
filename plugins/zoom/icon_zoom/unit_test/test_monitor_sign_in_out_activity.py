import unittest
from icon_zoom.util.event import Event
from icon_zoom.tasks.monitor_sign_in_out_activity.task import MonitorSignInOutActivity


class TestGetUserActivityEvents(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
