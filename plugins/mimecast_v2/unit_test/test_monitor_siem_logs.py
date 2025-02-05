import sys
import os

sys.path.append(os.path.abspath("../"))

from icon_mimecast_v2.tasks.monitor_siem_logs import MonitorSiemLogs
from icon_mimecast_v2.tasks.monitor_siem_logs.schema import MonitorSiemLogsOutput

from unittest import TestCase
from unittest.mock import patch
from util import Util
from parameterized import parameterized
from jsonschema import validate
from freezegun import freeze_time


STUB_STATE_EXPECTED = {
    "log_hashes": [
        "d98dafb4f13b3bb70539a6c251a8a9b42ea80de1",
        "d98dafb4f13b3bb70539a6c251a8a9b42ea80de1",
        "d98dafb4f13b3bb70539a6c251a8a9b42ea80de1",
    ],
    "query_config": {
        "attachment protect": {"caught_up": True, "next_page": "NDU1NA==", "query_date": "2000-01-06"},
        "receipt": {"caught_up": True, "next_page": "NDU1NA==", "query_date": "2000-01-06"},
        "url protect": {"caught_up": True, "next_page": "NDU1NA==", "query_date": "2000-01-06"},
    },
}

STUB_STATE_PAGINATING = {
    "log_hashes": [],
    "query_config": {
        "attachment protect": {"caught_up": False, "next_page": "NDU1NA==", "query_date": "2000-01-06"},
        "receipt": {"caught_up": False, "next_page": "NDU1NA==", "query_date": "2000-01-06"},
        "url protect": {"caught_up": False, "next_page": "NDU1NA==", "query_date": "2000-01-06"},
    },
}

STUB_STATE_PAGINATING_LAST_PAGE = {
    "log_hashes": [],
    "query_config": {
        "attachment protect": {"caught_up": True, "next_page": "NDU1NA==", "query_date": "2000-01-06"},
        "receipt": {"caught_up": True, "next_page": "NDU1NA==", "query_date": "2000-01-06"},
        "url protect": {"caught_up": True, "next_page": "NDU1NA==", "query_date": "2000-01-06"},
    },
}

STUB_STATE_SECOND_RUN_EXPECTED = {
    "log_hashes": [
        "d98dafb4f13b3bb70539a6c251a8a9b42ea80de1",
        "d98dafb4f13b3bb70539a6c251a8a9b42ea80de1",
        "d98dafb4f13b3bb70539a6c251a8a9b42ea80de1",
    ],
    "query_config": {
        "attachment protect": {"caught_up": True, "next_page": "NDU1NA==", "query_date": "2000-01-07"},
        "receipt": {"caught_up": True, "next_page": "NDU1NA==", "query_date": "2000-01-07"},
        "url protect": {"caught_up": True, "next_page": "NDU1NA==", "query_date": "2000-01-07"},
    },
}

STUB_STATE_EXPECTED_CUSTOM_CONFIG = {
    "log_hashes": [
        "d98dafb4f13b3bb70539a6c251a8a9b42ea80de1",
        "d98dafb4f13b3bb70539a6c251a8a9b42ea80de1",
        "d98dafb4f13b3bb70539a6c251a8a9b42ea80de1",
    ],
    "query_config": {
        "attachment protect": {"caught_up": True, "next_page": "NDU1NA==", "query_date": "1999-12-31"},
        "receipt": {"caught_up": True, "next_page": "NDU1NA==", "query_date": "1999-12-31"},
        "url protect": {"caught_up": True, "next_page": "NDU1NA==", "query_date": "1999-12-31"},
    },
}

STUB_CUSTOM_CONFIG = {
    "query_config": {
        "attachment protect": {"caught_up": True, "next_page": "NDU1NA==", "query_date": "1999-12-31"},
        "receipt": {"caught_up": True, "next_page": "NDU1NA==", "query_date": "1999-12-31"},
        "url protect": {"caught_up": True, "next_page": "NDU1NA==", "query_date": "1999-12-31"},
    },
    "page_size": 1,
    "thread_count": 1,
}

STUB_CUSTOM_CONFIG_EXCEED_DATE = {
    "query_config": {
        "attachment protect": {"caught_up": True, "next_page": "NDU1NA==", "query_date": "1999-12-30"},
        "receipt": {"caught_up": True, "next_page": "NDU1NA==", "query_date": "1999-12-30"},
        "url protect": {"caught_up": True, "next_page": "NDU1NA==", "query_date": "1999-12-30"},
    },
    "page_size": 1,
    "thread_count": 1,
}


@freeze_time("2000-01-07T00:00:00.000000Z")
class TestMonitorLogs(TestCase):
    @classmethod
    @patch("requests.Session.send", side_effect=Util.mocked_request)
    def setUpClass(cls, mocked_request) -> None:
        cls.task = Util.default_connector(MonitorSiemLogs())

    @parameterized.expand(
        [
            [
                "starting",
                {},
                {},
                Util.read_file_to_dict("expected/monitor_siem_logs.json.exp"),
                STUB_STATE_EXPECTED,
                True,
                200,
                None,
            ],
            [
                "paginating",
                STUB_STATE_PAGINATING,
                {},
                Util.read_file_to_dict("expected/monitor_siem_logs.json.exp"),
                STUB_STATE_EXPECTED,
                True,
                200,
                None,
            ],
            [
                "paginating_last_page",
                STUB_STATE_PAGINATING_LAST_PAGE,
                {},
                Util.read_file_to_dict("expected/monitor_siem_logs.json.exp"),
                STUB_STATE_SECOND_RUN_EXPECTED,
                False,
                200,
                None,
            ],
            [
                "custom_config",
                {},
                STUB_CUSTOM_CONFIG,
                Util.read_file_to_dict("expected/monitor_siem_logs.json.exp"),
                STUB_STATE_EXPECTED_CUSTOM_CONFIG,
                True,
                200,
                None,
            ],
            [
                "custom_config_past_cutoff",
                {},
                STUB_CUSTOM_CONFIG_EXCEED_DATE,
                Util.read_file_to_dict("expected/monitor_siem_logs.json.exp"),
                STUB_STATE_EXPECTED_CUSTOM_CONFIG,
                True,
                200,
                None,
            ],
        ]
    )
    @patch("requests.Session.send", side_effect=Util.mocked_request)
    def test_monitor_logs(
        self,
        test_name,
        state,
        custom_config,
        expected_output,
        expected_state,
        expected_has_more_pages,
        expected_status_code,
        expected_error,
        mock_request,
    ):
        output, state, has_more_pages, status_code, error = self.task.run(
            params={}, state=state, custom_config=custom_config
        )
        self.assertEqual(expected_output, output)
        self.assertEqual(expected_state, state)
        self.assertEqual(expected_has_more_pages, has_more_pages)
        self.assertEqual(expected_status_code, status_code)
        self.assertEqual(expected_error, error)
        validate(output, MonitorSiemLogsOutput.schema)

    @parameterized.expand(
        [
            [
                "401",
                {"query_config": {"receipt": {"caught_up": True, "next_page": "NDU1NA==", "query_date": "2000-01-01"}}},
                "Invalid API key provided.",
                "Verify your API key configured in your connection is correct.",
                401,
            ],
            [
                "500",
                {"query_config": {"receipt": {"caught_up": True, "next_page": "NDU1NA==", "query_date": "2000-01-02"}}},
                "Something unexpected occurred.",
                "Check the logs and if the issue persists please contact support.",
                500,
            ],
            [
                "json_decode",
                {"query_config": {"receipt": {"caught_up": True, "next_page": "NDU1NA==", "query_date": "2000-01-03"}}},
                "Received an unexpected response from the server.",
                "(non-JSON or no response was received).",
                500,
            ],
            [
                "unknown",
                {"query_config": {"receipt": {"caught_up": True, "next_page": "NDU1NA==", "query_date": "2000-01-04"}}},
                "Something unexpected occurred.",
                "Check the logs and if the issue persists please contact support.",
                500,
            ],
        ]
    )
    @patch("requests.Session.send", side_effect=Util.mocked_request)
    def test_monitor_logs_errors(
        self,
        test_name,
        state,
        expected_cause,
        expected_assistance,
        expected_status_code,
        mock_request,
    ):
        output, state, has_more_pages, status_code, error = self.task.run(params={}, state=state)
        self.assertEqual(expected_status_code, status_code)
        self.assertEqual(expected_cause, error.cause)
        self.assertEqual(expected_assistance, error.assistance)
        validate(output, MonitorSiemLogsOutput.schema)
