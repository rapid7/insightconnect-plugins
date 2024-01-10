import datetime
import os
import sys
from insightconnect_plugin_runtime.exceptions import PluginException
from unittest import TestCase
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))

from komand_mimecast.util.event import EventLogs
from komand_mimecast.util.exceptions import ApiClientException
from komand_mimecast.tasks import MonitorSiemLogs
from util import Util, FILE_ZIP_CONTENT_1, FILE_ZIP_CONTENT_2, SIEM_LOGS_HEADERS_RESPONSE


@patch("requests.request", side_effect=Util.mocked_request)
class TestMonitorSiemLogs(TestCase):
    def setUp(self) -> None:
        self.task = Util.default_connector(MonitorSiemLogs())

    def test_monitor_siem_logs_success(self, _mock_data):
        content = [FILE_ZIP_CONTENT_1, FILE_ZIP_CONTENT_2]
        token = SIEM_LOGS_HEADERS_RESPONSE.get("mc-siem-token")
        tests = [
            {"next_token": "happy_token", "resp": content, "has_more_pages": True, "token": token},
            {"next_token": "force_json_error", "resp": content, "has_more_pages": True, "token": token},
            {"next_token": "no_results", "resp": [], "has_more_pages": False, "token": "no_results"},
        ]
        for test in tests:
            with self.subTest(f"Success test with token: {test.get('next_token')}"):
                test_state = {"next_token": test.get("next_token")}
                response, new_state, has_more_pages, status_code, _ = self.task.run(params={}, state=test_state)

                self.assertEqual(has_more_pages, test.get("has_more_pages"))
                self.assertEqual(response, test.get("resp"))
                self.assertEqual(new_state, {"next_token": test.get("token")})
                self.assertEqual(status_code, 200)

    def test_monitor_siem_logs_raises_401(self, _mock_data):
        state_params = {"next_token": "force_401"}

        response, new_state, has_more_pages, status_code, error = self.task.run(params={}, state=state_params)

        self.assertEqual(status_code, 401)
        self.assertEqual(response, [])
        self.assertEqual(new_state, state_params)  # we shouldn't change the state if we encounter an error
        self.assertEqual(type(error), ApiClientException)


class TestEventLogs(TestCase):
    def setUp(self) -> None:
        self.datetime_str = "2023-05-01T12:00:00-0400"
        self.output_data = {
            "acc": "ABC123",
            "Sender": "user@example.com",
            "datetime": self.datetime_str,
            "Rcpt": "user1@example.com",
            "aCode": "abcd123_abcd1234",
            "Dir": "Internal",
            "RcptHdrType": "To",
        }

        self.output_without_datetime = {
            "acc": "ABC123",
            "Sender": "user@example.com",
            "datetime": "",
            "Rcpt": "user1@example.com",
            "aCode": "abcd123_abcd1234",
            "Dir": "Internal",
            "RcptHdrType": "To",
        }

    def test_event_logs_get_dict(self):
        event = EventLogs(data=self.output_data)

        self.assertEqual(event.get_dict(), self.output_data)

    def test_event_logs_compare_to_datetime_when_event_is_newer(self):
        event = EventLogs(data=self.output_data)

        expected_result = event.compare_datetime(datetime.datetime(2023, 4, 1))
        self.assertTrue(expected_result)

    def test_event_logs_compare_to_datetime_when_event_is_older(self):
        event = EventLogs(data=self.output_data)

        expected_result = event.compare_datetime(datetime.datetime(2023, 6, 1))
        self.assertFalse(expected_result)
