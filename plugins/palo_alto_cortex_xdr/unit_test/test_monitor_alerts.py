import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock

from icon_palo_alto_cortex_xdr.tasks.monitor_alerts import MonitorAlerts
from icon_palo_alto_cortex_xdr.tasks.monitor_alerts.schema import MonitorAlertsOutput

from icon_palo_alto_cortex_xdr.connection.schema import Input

from parameterized import parameterized
from jsonschema import validate
from freezegun import freeze_time
from util import Util
from taskutil import TaskUtil, mock_conditions, mocked_response_type


STUB_STATE_EXPECTED_SECOND_PAGE = {
    "current_count": 2,
    "last_search_from": 100,
    "last_search_to": 200,
    "last_alert_time": 1706540499609,
    "query_end_time": 1706539560000,
    "query_start_time": 1706453160000,
    "last_alert_hash": ["f4ef7617f46fef7b78410498f563e01df2a5f030"],
}

STUB_STATE_MORE_PAGES = {
    "current_count": 1,
    "last_search_to": 100,
    "last_search_from": 0,
    "query_start_time": 1706453160000,
    "query_end_time": 1706539560000,
    "last_alert_time": 1706540499609,
    "last_alert_hash": ["a502a9c50798186882ad8dc91ac2b38eb185c404"],
}

STUB_STATE_EXPECTED_NO_PAGE = {
    "last_alert_hash": ["f4ef7617f46fef7b78410498f563e01df2a5f030"],
    "last_alert_time": 1706540499609,
}

STUB_STATE_ERROR_400 = {
    "last_search_from": 300,
    "last_search_to": 400,
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
                True,
                "monitor_alerts",
                STUB_STATE_MORE_PAGES,
                200,
            ],
            [
                "next_page",
                STUB_STATE_MORE_PAGES.copy(),
                TaskUtil.load_expected("monitor_alert_two"),
                True,
                "monitor_alerts_two",
                STUB_STATE_EXPECTED_SECOND_PAGE,
                200,
            ],
            [
                "final_page",
                STUB_STATE_EXPECTED_SECOND_PAGE.copy(),
                TaskUtil.load_expected("monitor_alerts_empty"),
                False,
                "monitor_alerts_empty",
                STUB_STATE_EXPECTED_NO_PAGE,
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

        output, state, has_more_pages, status_code, _ = self.task.run(params={}, state=state)

        self.assertEqual(expected_output, output)
        self.assertEqual(expected_has_more_pages, has_more_pages)
        self.assertEqual(expected_state, state)
        self.assertEqual(expected_status_code, status_code)

    @parameterized.expand(
        [
            [
                "error",
                STUB_STATE_ERROR_400,
                500,
                "A PluginException has occurred.",
                # "Verify your plugin input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
            # [
            #     "401",
            #     {},
            #     401,
            #     "The account configured in your connection is unauthorized to access this service.",
            #     "Verify the permissions for your account and try again.",
            # ],
        ]
    )
    def test_errors(
        self,
        mock_post,
        test_name,
        state,
        expected_status_code,
    ) -> None:
        # breakpoint()
        # with self.assertRaises(PluginException):
        _, state, has_more_pages, status_code, error = self.task.run(params={}, state=state)

        self.assertEqual(False, has_more_pages)
