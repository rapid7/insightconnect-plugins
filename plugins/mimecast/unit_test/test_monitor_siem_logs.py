import datetime
import os
import sys
from unittest import TestCase
from unittest.mock import patch

from dateutil.parser import parse

sys.path.append(os.path.abspath("../"))

from komand_mimecast.util.event import EventLogs
from komand_mimecast.tasks import MonitorSiemLogs
from unit_test.util import Util, FILE_ZIP_CONTENT_1, FILE_ZIP_CONTENT_2, SIEM_LOGS_HEADERS_RESPONSE


@patch("requests.request", side_effect=Util.mocked_request)
class TestMonitorSiemLogs(TestCase):
    def setUp(self) -> None:
        self.task = Util.default_connector(MonitorSiemLogs())

    def test_monitor_siem_logs(self, mock_data):
        response, new_state, has_more_pages = self.task.run()

        expected_response = [FILE_ZIP_CONTENT_1, FILE_ZIP_CONTENT_2]
        expected_state = {"next_token": SIEM_LOGS_HEADERS_RESPONSE.get("mc-siem-token"), "status_code": 200}

        self.assertEqual(has_more_pages, True)
        self.assertEqual(response, expected_response)
        self.assertEqual(new_state, expected_state)


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

    def test_event_logs_datetime(self):
        event = EventLogs(data=self.output_data)

        expected_date = parse(self.datetime_str, ignoretz=True)
        self.assertEqual(event.data["datetime"], expected_date)

    def test_event_logs_without_datetime(self):
        event = EventLogs(data=self.output_without_datetime)

        expected_date = ""
        self.assertEqual(event.data["datetime"], expected_date)

    def test_event_logs_get_dict(self):
        event = EventLogs(data=self.output_data)

        expected_date = event.data["datetime"].isoformat()
        self.assertEqual(event.get_dict()["datetime"], expected_date)

    def test_event_logs_compare_to_datetime_when_event_is_newer(self):
        event = EventLogs(data=self.output_data)

        expected_result = event.compare_datetime(datetime.datetime(2023, 4, 1))
        self.assertTrue(expected_result)

    def test_event_logs_compare_to_datetime_when_event_is_older(self):
        event = EventLogs(data=self.output_data)

        expected_result = event.compare_datetime(datetime.datetime(2023, 6, 1))
        self.assertFalse(expected_result)
