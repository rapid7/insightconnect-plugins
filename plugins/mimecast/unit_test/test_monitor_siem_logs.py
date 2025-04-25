import datetime
import os
import sys
import logging
from jsonschema import validate
from unittest import TestCase
from unittest.mock import patch
from freezegun import freeze_time
from time import time

sys.path.append(os.path.abspath("../"))

from komand_mimecast.util.event import EventLogs
from komand_mimecast.util.exceptions import ApiClientException
from komand_mimecast.tasks import MonitorSiemLogs
from komand_mimecast.tasks.monitor_siem_logs.schema import MonitorSiemLogsOutput
from util import Util, FILE_ZIP_CONTENT_1, FILE_ZIP_CONTENT_2, FILE_ZIP_CONTENT_3, SIEM_LOGS_HEADERS_RESPONSE


@freeze_time("2022-01-01T12:00:00")
@patch("requests.request", side_effect=Util.mocked_request)
class TestMonitorSiemLogs(TestCase):
    def setUp(self) -> None:
        self.task = Util.default_connector(MonitorSiemLogs())

    @patch("logging.Logger.warning")
    def test_monitor_siem_logs_success(self, mock_logger, _mock_data):
        content = [FILE_ZIP_CONTENT_1, FILE_ZIP_CONTENT_2, FILE_ZIP_CONTENT_3]
        token = SIEM_LOGS_HEADERS_RESPONSE.get("mc-siem-token")
        tests = [
            {"next_token": "happy_token", "resp": content, "has_more_pages": True, "token": token},
            {"next_token": "force_json_error", "resp": [], "has_more_pages": True, "token": "force_json_error"},
            {"next_token": "no_results", "resp": [], "has_more_pages": False, "token": token},
            {"next_token": "force_single_json_error", "resp": [], "has_more_pages": True, "token": token},
        ]
        for test in tests:
            with self.subTest(f"Success test with token: {test.get('next_token')}"):
                test_state = {"next_token": test.get("next_token")}
                response, new_state, has_more_pages, status_code, _ = self.task.run(params={}, state=test_state)
                self.assertEqual(has_more_pages, test.get("has_more_pages"))
                self.assertEqual(response, test.get("resp"))
                self.assertEqual(status_code, 200)
                if test.get("has_more_pages") == False:
                    self.assertEqual(
                        new_state, {"next_token": token, "normal_running_cutoff": True, "last_log_line": 0}
                    )
                else:
                    self.assertEqual(new_state, {"next_token": token, "last_log_line": 0})
                if test.get("next_token") == "happy_token":
                    mock_logger.assert_called()
                    self.assertIn(
                        "There was no datetime key for the following event: {'acc': 'ABC12345'}",
                        mock_logger.call_args[0][0],
                    )
                validate(response, MonitorSiemLogsOutput.schema)

    def test_monitor_siem_logs_raises_401(self, _mock_data):
        # TODO: update 401 logic to successfully check is_last_token that was introduced in 5.3.3
        state_params = {"next_token": "force_401", "last_log_line": 0}

        response, new_state, has_more_pages, status_code, error = self.task.run(params={}, state=state_params)

        self.assertEqual(status_code, 401)
        self.assertEqual(response, [])
        self.assertEqual(new_state, state_params)  # we shouldn't change the state if we encounter an error
        self.assertEqual(type(error), ApiClientException)

    def test_monitor_siem_logs_custom_message(self, _mock_data):
        custom_config = {"custom_log_message": "Test", "custom_status": 400, "custom_assistance": "Test assistance"}
        response, new_state, has_more_pages, status_code, error = self.task.run(
            params={}, state={}, custom_config=custom_config
        )

        self.assertEqual(status_code, 400)
        self.assertEqual(response, [])
        self.assertEqual(new_state, {})
        self.assertEqual(error.cause, "Test")
        self.assertEqual(error.assistance, "Test assistance")

    def test_monitor_siem_logs_raises_429(self, _mock_data):
        state_params = {"next_token": "force_429", "last_log_line": 0}
        expected_state = state_params.copy()
        expected_state.update({"rate_limit_datetime": 1641039600.0})  # current time + header value of 5 minutes
        response, new_state, has_more_pages, status_code, error = self.task.run(params={}, state=state_params)
        self.assertEqual(status_code, 200)
        self.assertEqual(has_more_pages, True)
        self.assertEqual(response, [])
        self.assertEqual(new_state, expected_state)
        self.assertEqual(error, None)

        # Second run should return 429 status code
        _, new_state_2, has_more_pages, exp_status_code, error = self.task.run(params={}, state=expected_state)
        self.assertEqual(429, exp_status_code)
        self.assertEqual(new_state_2, expected_state)  # state doesn't change until the time has passed

    @patch("logging.Logger.error")
    def test_monitor_siem_logs_raises_429_and_errors(self, mocked_logger, _mock_data):
        state_params = {"next_token": "force_429_error", "last_log_line": 0}
        response, new_state, has_more_pages, status_code, error = self.task.run(params={}, state=state_params)
        self.assertEqual(status_code, 200)
        self.assertEqual(has_more_pages, True)
        self.assertEqual(response, [])
        self.assertEqual(new_state, state_params)
        self.assertEqual(error, None)
        mocked_logger.assert_called()
        self.assertIn(
            "Unable to calculate new run time, no rate limiting applied to the state", mocked_logger.call_args[0][0]
        )

    def test_monitor_siem_logs_raises_429_no_header(self, _mock_data):
        state_params = {"next_token": "force_429_no_header", "last_log_line": 0}
        expected_state = state_params.copy()
        expected_state.update({"rate_limit_datetime": 1641039000})  # uses current time + 10 minutes
        response, new_state, has_more_pages, status_code, error = self.task.run(params={}, state=state_params)
        self.assertEqual(status_code, 200)
        self.assertEqual(has_more_pages, True)
        self.assertEqual(response, [])
        self.assertEqual(new_state, expected_state)
        self.assertEqual(error, None)

    @patch("logging.Logger.info")
    def test_monitor_logs_rate_limit_has_passed(self, mock_logger, _mock_data):
        # force the time to be the pasts then next run is able to run again
        state = {"rate_limit_datetime": time()}
        _, rate_limit_passed_state, _, status_code, _ = self.task.run(params={}, state=state)
        self.assertEqual(200, status_code)
        self.assertNotIn("rate_limit_datetime", rate_limit_passed_state.keys())

        self.assertIn(
            "However no longer in rate limiting period, so task can be executed...", mock_logger.call_args_list[0][0][0]
        )

    @patch("logging.Logger.error")
    def test_monitor_siem_logs_stops_path_traversal(self, mock_logger, _mock_data):
        test_state = {
            "next_token": "path_traversal",
            "last_log_line": 0,
        }  # this forces our mock util to append `../` into filenames
        response, new_state, has_more_pages, status_code, error = self.task.run(params={}, state=test_state)
        self.assertEqual(status_code, 200)
        self.assertEqual(has_more_pages, True)
        self.assertEqual(response, [])  # no logs will be parsed as we raise error after catching BadZipFile
        self.assertEqual(new_state, test_state)  # we shouldn't change the state if we encounter an error
        mock_logger.assert_called()
        self.assertIn(
            "There is no item named 'filename-2-from-mimecast.json' in the archive", mock_logger.call_args[0][0]
        )

    @patch("logging.Logger.error")
    def test_monitor_siem_logs_raises_json_error(self, mock_logger, _mock_data):
        test_state = {
            "next_token": "request.json error",
            "last_log_line": 0,
        }  # this forces our mocked response to raise JSON encode error
        response, new_state, has_more_pages, status_code, error = self.task.run(params={}, state=test_state)
        self.assertEqual(status_code, 200)
        self.assertEqual(has_more_pages, False)
        self.assertEqual(response, [])  # no logs will be parsed as we raise error after catching JSONDecodeError
        self.assertEqual(new_state, test_state)  # we shouldn't change the state if we encounter an error
        mock_logger.assert_called()
        self.assertIn("JSON", mock_logger.call_args[0][0])

    @patch("logging.Logger.debug")
    @patch("komand_mimecast.util.api.MimecastAPI.get_siem_logs", side_effect=Exception("negative seek"))
    def test_monitor_siem_logs_raises_negative_seek(self, mock_siem_logs, mock_logger, _mock_data):
        test_state = {
            "next_token": "negative_seek error",
            "last_log_line": 0,
        }  # this forces our mocked response to raise negative seek
        response, new_state, has_more_pages, status_code, error = self.task.run(params={}, state=test_state)
        self.assertEqual(status_code, 500)
        self.assertEqual(has_more_pages, False)
        self.assertEqual(response, [])  # no logs will be parsed as we raise error after catching negative seek
        self.assertEqual(new_state, test_state)  # we shouldn't change the state if we encounter an error
        mock_logger.assert_called()
        self.assertIn("negative seek", mock_logger.call_args[0][0])

    @patch("logging.Logger.info")
    @patch("insightconnect_plugin_runtime.helper.get_time_now", return_value=datetime.datetime(2022, 1, 1, 0, 0, 0))
    def test_monitor_siem_logs_get_filter_time(self, mock_time, mock_logger, _mock_data):
        content = [FILE_ZIP_CONTENT_1, FILE_ZIP_CONTENT_2, FILE_ZIP_CONTENT_3]
        token = SIEM_LOGS_HEADERS_RESPONSE.get("mc-siem-token")

        tests = [
            {
                "resp": content,
                "has_more_pages": True,
                "token": token,
                "custom_config": {},
                "expected_filter_time": "2021-12-31 00:00:00",
            },
            {
                "resp": content,
                "has_more_pages": True,
                "token": token,
                "custom_config": {
                    "lookback": {"year": 2021, "month": 1, "day": 23, "hour": 22, "minute": 0, "second": 0}
                },
                "expected_filter_time": "2021-01-23 22:00:00",
            },
            {
                "resp": content,
                "has_more_pages": True,
                "token": token,
                "custom_config": {
                    "cutoff": {"date": {"year": 2021, "month": 1, "day": 23, "hour": 22, "minute": 0, "second": 0}}
                },
                "expected_filter_time": "2021-01-23 22:00:00",
            },
            {
                "resp": content,
                "has_more_pages": True,
                "token": token,
                "custom_config": {"cutoff": {"hours": 72}},
                "expected_filter_time": "2021-12-29 00:00:00",
            },
        ]

        for test in tests:
            with self.subTest(f"Success test with token: {test.get('next_token')}"):
                # test_state = {"next_token": test.get("next_token")}
                response, new_state, has_more_pages, status_code, _ = self.task.run(
                    params={}, state={}, custom_config=test.get("custom_config", {})
                )
                self.assertEqual(has_more_pages, test.get("has_more_pages"))
                self.assertEqual(response, test.get("resp"))
                self.assertEqual(status_code, 200)
                if test.get("has_more_pages") == False:
                    self.assertEqual(
                        new_state, {"next_token": token, "normal_running_cutoff": True, "last_log_line": 0}
                    )
                else:
                    self.assertEqual(new_state, {"next_token": token, "last_log_line": 0})
                validate(response, MonitorSiemLogsOutput.schema)

                self.assertIn(f"{test.get('expected_filter_time')}", mock_logger.mock_calls[-6][1][0])

    @patch("logging.Logger.warning")
    @patch("komand_mimecast.tasks.monitor_siem_logs.task.MAX_EVENTS_PER_RUN_DEFAULT", new=1)
    def test_monitor_siem_logs_success_split_files_across_runs(self, mock_logger, _mock_data):
        content = [FILE_ZIP_CONTENT_1, FILE_ZIP_CONTENT_2, FILE_ZIP_CONTENT_3]
        token = SIEM_LOGS_HEADERS_RESPONSE.get("mc-siem-token")
        tests = [
            {
                "next_token": "test_multi_log_lines",
                "resp": content,
                "has_more_pages": True,
                "token": token,
                "state": {},
                "run": 1,
            },
            {
                "next_token": "test_multi_log_lines",
                "resp": content,
                "has_more_pages": True,
                "token": token,
                "state": {
                    "last_log_line": 1,
                    "last_runs_filter_time": "2022-01-01T12:00:00",
                    "previous_file_hash": "9aabf6ac8a53ef0b93664b6507d2ce38",
                },
                "run": 2,
            },
        ]
        for test in tests:
            with self.subTest(f"Success test with token: {test.get('next_token')}"):
                response, new_state, has_more_pages, status_code, _ = self.task.run(params={}, state=test.get("state"))

                self.assertEqual(has_more_pages, test.get("has_more_pages"))
                self.assertEqual(status_code, 200)

                if test.get("run") == 1:
                    self.assertEqual(response, [FILE_ZIP_CONTENT_1])
                elif test.get("run") == 2:
                    self.assertEqual(response, [FILE_ZIP_CONTENT_2])

                validate(response, MonitorSiemLogsOutput.schema)


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
        self.logger = logging.getLogger("abc")

    def test_event_logs_get_dict(self):
        event = EventLogs(data=self.output_data, logger=self.logger)

        self.assertEqual(event.get_dict(), self.output_data)

    def test_event_logs_compare_to_datetime_when_event_is_newer(self):
        event = EventLogs(data=self.output_data, logger=self.logger)

        expected_result = event.compare_datetime(datetime.datetime(2023, 4, 1))
        self.assertTrue(expected_result)

    def test_event_logs_compare_to_datetime_when_event_is_older(self):
        event = EventLogs(data=self.output_data, logger=self.logger)

        expected_result = event.compare_datetime(datetime.datetime(2023, 6, 1))
        self.assertFalse(expected_result)
