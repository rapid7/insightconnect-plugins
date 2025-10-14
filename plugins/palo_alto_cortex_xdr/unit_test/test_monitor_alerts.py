import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock

from icon_palo_alto_cortex_xdr.tasks.monitor_alerts import MonitorAlerts

from parameterized import parameterized
from freezegun import freeze_time
from taskutil import TaskUtil, mock_conditions, mocked_response_type
from insightconnect_plugin_runtime.exceptions import PluginException
from typing import Union
from mock_helper import MockResponse

STUB_STATE_EXPECTED_SECOND_PAGE = {
    "current_count": 100,
    "last_search_from": 100,
    "last_search_to": 200,
    "query_end_time": 1706539560000,
    "query_start_time": 1706453160000,
    "last_alert_hash": ["f4ef7617f46fef7b78410498f563e01df2a5f030"],
}

STUB_STATE_NO_PAGES = {
    "query_end_time": 1706539560000,
    "last_alert_hash": ["a502a9c50798186882ad8dc91ac2b38eb185c404"],
}

STUB_STATE_MORE_PAGES = {
    "current_count": 100,
    "last_search_to": 100,
    "last_search_from": 0,
    "query_start_time": 1706453160000,
    "query_end_time": 1706539560000,
    "last_alert_hash": ["a502a9c50798186882ad8dc91ac2b38eb185c403"],
}

STUB_STATE_EXPECTED_NO_PAGE = {
    "last_alert_hash": ["f4ef7617f46fef7b78410498f563e01df2a5f030"],
    "last_alert_time": 1706540499609,
}

STUB_STATE_ERROR = {
    "last_search_from": 300,
    "last_search_to": 400,
}

STUB_STATE_DEDUPE = {
    "current_count": 100,
    "last_search_to": 100,
    "last_search_from": 0,
    "query_start_time": 1706453160000,
    "query_end_time": 1706539560000,
    "last_alert_hash": ["a502a9c50798186882ad8dc91ac2b38eb185c404"],
}

STUB_STATE_EXCEED_LOOKBACK = {
    "query_end_time": 1706539560000,
    "last_alert_hash": ["a502a9c50798186882ad8dc91ac2b38eb185c404"],
}

STUB_STATE_EXCEED_LOOKBACK_PAGINATING = {
    "current_count": 100,
    "last_search_to": 100,
    "last_search_from": 0,
    "query_start_time": 1705439560000,
    "query_end_time": 1705539560000,
    "last_alert_hash": ["a502a9c50798186882ad8dc91ac2b38eb185c404"],
}

STUB_STATE_EXCEED_LOOKBACK_NO_RESULTS = {
    "query_end_time": 1706539560000,
    "last_alert_hash": ["a502a9c50798186882ad8dc91ac2b38eb185c404"],
}


@freeze_time("2024-01-29T15:01:00.000000Z")
@patch("requests.Session.send")
class TestMonitorAlerts(TestCase):
    def setUp(self) -> None:
        self.task = TaskUtil.default_connector(MonitorAlerts())

    @parameterized.expand(
        [
            [
                "starting",
                {},
                TaskUtil.load_expected("monitor_alerts"),
                False,
                "monitor_alerts",
                STUB_STATE_NO_PAGES,
                200,
            ],
            [
                "starting_more_pages",
                {},
                TaskUtil.load_expected("monitor_alerts_full_page"),
                True,
                "monitor_alerts_full_page",
                TaskUtil.load_expected("monitor_alerts_full_page_state"),
                200,
            ],
            [
                "next_page_more_pages",
                STUB_STATE_MORE_PAGES.copy(),
                TaskUtil.load_expected("monitor_alerts_full_page"),
                True,
                "monitor_alerts_full_page",
                TaskUtil.load_expected("monitor_alerts_full_next_page_state"),
                200,
            ],
            [
                "next_page_final_page",
                STUB_STATE_EXPECTED_SECOND_PAGE.copy(),
                TaskUtil.load_expected("monitor_alerts"),
                False,
                "monitor_alerts",
                STUB_STATE_NO_PAGES,
                200,
            ],
        ]
    )
    def test_monitor_alerts_pagination(
        self,
        mock_req: MagicMock,
        test_name: str,
        state: dict,
        expected_output: list,
        expected_has_more_pages: bool,
        response_file: str,
        expected_state: dict,
        expected_status_code: int,
    ) -> None:

        mock_req.return_value = mock_conditions(200, file_name=response_file)
        self.maxDiff = None
        output, state, has_more_pages, status_code, _ = self.task.run(state=state)
        self.assertEqual(expected_output, output)
        self.assertEqual(expected_has_more_pages, has_more_pages)
        self.assertEqual(expected_state, state)
        self.assertEqual(expected_status_code, status_code)

    @parameterized.expand(
        [
            [
                "Bad Request",
                STUB_STATE_ERROR,
                PluginException(
                    cause=PluginException.causes.get(PluginException.Preset.INVALID_JSON),
                    assistance="Bad request, invalid JSON.",
                ),
                400,
            ],
            [
                "Wrong License",
                STUB_STATE_ERROR,
                PluginException(
                    cause=PluginException.causes.get(PluginException.Preset.UNAUTHORIZED),
                    assistance="Unauthorized access. User does not have the required license type to run this API.",
                ),
                402,
            ],
            [
                "Unauthorized",
                {},
                PluginException(
                    cause=PluginException.causes.get(PluginException.Preset.API_KEY),
                    assistance=PluginException.assistances.get(PluginException.Preset.API_KEY),
                    data='{"reply": {"err_code": 401, "err_msg": "Public API request unauthorized", "err_extra": null}}',
                ),
                401,
            ],
            [
                "Forbidden",
                STUB_STATE_ERROR,
                PluginException(
                    cause=PluginException.causes.get(PluginException.Preset.UNAUTHORIZED),
                    assistance="Forbidden. The provided API Key does not have the required RBAC permissions to run this API.",
                ),
                403,
            ],
            [
                "Not Found",
                STUB_STATE_ERROR,
                PluginException(
                    cause=PluginException.causes.get(PluginException.Preset.NOT_FOUND),
                    assistance="The object at https://example.com/public_api/v1/alerts/get_alerts does not exist. Check the FQDN connection setting and try again.",
                ),
                404,
            ],
            [
                "error.data is not of type response",
                STUB_STATE_ERROR,
                PluginException(
                    cause="Failed to connect to the server.",
                    assistance="Please check your network connection and try again.",
                ),
                699,
            ],
            ["regular exception", STUB_STATE_ERROR, "'list' object has no attribute 'get'", 500],
        ]
    )
    def test_monitor_alerts_error_handling(
        self,
        mock_req: MagicMock,
        test_name: str,
        input_state: dict,
        error_msg: Union[str, PluginException],
        error_code: int,
    ) -> None:

        # This if statement is to handle the "if not type response" statement specifically
        if error_code == 500:
            mocked_response = mock_conditions(200, file_name="monitor_alerts_faulty_response")

        elif error_code == 401:
            mocked_response = MockResponse(
                filename="monitor_alerts_faulty_response",
                status_code=401,
                text='{"reply": {"err_code": 401, "err_msg": "Public API request unauthorized", "err_extra": null}}',
            )

        # This else applies to every other usual exception
        else:
            mocked_response = mocked_response_type(error_code)

        if error_code != 699:
            mock_req.return_value = mocked_response
        else:
            from requests import ConnectionError

            mock_req.side_effect = ConnectionError
            error_code = 500

        output, state, has_more_pages, status_code, error = self.task.run(state=input_state)
        self.assertEqual(output, [])
        self.assertEqual(input_state, state)
        self.assertEqual(error_code, status_code)

        # We make an if statement here because of the above if statement
        # Every error comes back as type pluginException
        if isinstance(error_msg, PluginException):
            self.assertEqual(error_msg.data, error.data)

        # For our 'not type response' error, it is just a string
        else:
            self.assertEqual(error_msg, error.data)

        self.assertEqual(False, has_more_pages)

    @parameterized.expand(
        [
            [
                "Load first",
                STUB_STATE_DEDUPE,
                "monitor_alerts",
                200,
            ]
        ]
    )
    def test_monitor_alerts_dedupe(
        self,
        mock_req: MagicMock,
        test_name: str,
        input_state: dict,
        response_file: str,
        expected_status_code,
    ) -> None:

        mock_req.return_value = mock_conditions(200, file_name=response_file)

        output, state, has_more_pages, status_code, _ = self.task.run(state=input_state)
        self.assertEqual(status_code, expected_status_code)
        self.assertEqual(STUB_STATE_NO_PAGES, state)
        self.assertEqual(has_more_pages, False)
        self.assertEqual(output, [])

    @parameterized.expand(
        [
            [
                "custom_config_last_alert_time",
                {},
                TaskUtil.load_expected("monitor_alerts"),
                "monitor_alerts",
                200,
                {
                    "lookback": {
                        "date": {
                            "year": 2024,
                            "month": 8,
                            "day": 1,
                            "hour": 1,
                            "minute": 2,
                            "second": 3,
                            "microsecond": 0,
                        }
                    },
                    "alert_limit": 10,
                },
            ],
            [
                "custom_config_max_alert_time",
                {},
                TaskUtil.load_expected("monitor_alerts"),
                "monitor_alerts",
                200,
                {
                    "max_lookback_date_time": {
                        "year": 2024,
                        "month": 8,
                        "day": 2,
                        "hour": 3,
                        "minute": 4,
                        "second": 5,
                        "microsecond": 0,
                    },
                    "alert_limit": 10,
                },
            ],
            [
                "custom_config_comparison_time_exceeds_saved_time",
                STUB_STATE_EXCEED_LOOKBACK,
                TaskUtil.load_expected("monitor_alerts_empty"),
                "monitor_alerts",
                200,
                {
                    "max_lookback_date_time": {
                        "year": 2024,
                        "month": 10,
                        "day": 2,
                        "hour": 3,
                        "minute": 4,
                        "second": 5,
                        "microsecond": 0,
                    },
                    "alert_limit": 10,
                },
            ],
            [
                "custom_config_comparison_time_exceeds_saved_time_paginating",
                STUB_STATE_EXCEED_LOOKBACK_PAGINATING,
                TaskUtil.load_expected("monitor_alerts_empty"),
                "monitor_alerts",
                200,
                {
                    "max_lookback_date_time": {
                        "year": 2024,
                        "month": 10,
                        "day": 2,
                        "hour": 3,
                        "minute": 4,
                        "second": 5,
                        "microsecond": 0,
                    },
                    "alert_limit": 10,
                },
            ],
            [
                "custom_config_alert_limit_exceeds_100",
                STUB_STATE_EXCEED_LOOKBACK,
                TaskUtil.load_expected("monitor_alerts_empty"),
                "monitor_alerts",
                200,
                {
                    "max_lookback_date_time": {
                        "year": 2024,
                        "month": 10,
                        "day": 2,
                        "hour": 3,
                        "minute": 4,
                        "second": 5,
                        "microsecond": 0,
                    },
                    "alert_limit": 101,
                },
            ],
        ]
    )
    def test_monitor_alerts_custom_config(
        self,
        mock_req: MagicMock,
        test_name: str,
        input_state: dict,
        expected_output: list,
        response_file: str,
        expected_status_code: int,
        custom_config: dict,
    ) -> None:

        mock_req.return_value = mock_conditions(200, file_name=response_file)

        output, state, has_more_pages, status_code, _ = self.task.run(state=input_state, custom_config=custom_config)
        print(state)
        self.assertEqual(output, expected_output)
        self.assertEqual(status_code, expected_status_code)
        self.assertEqual(STUB_STATE_EXCEED_LOOKBACK_NO_RESULTS, state)
        self.assertEqual(has_more_pages, False)
