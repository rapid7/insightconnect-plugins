import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from icon_palo_alto_cortex_xdr.tasks.monitor_alerts import MonitorAlerts
from icon_palo_alto_cortex_xdr.tasks.monitor_alerts.schema import MonitorAlertsOutput

from icon_palo_alto_cortex_xdr.connection.schema import Input

from parameterized import parameterized
from jsonschema import validate
from freezegun import freeze_time
from util import Util

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


@freeze_time("2024-01-29T15:01:00.000000Z")
@patch("icon_palo_alto_cortex_xdr.util.api.CortexXdrAPI.build_request", side_effect=Util.mocked_requests)
class TestMonitorAlerts(TestCase):

    @classmethod
    @patch("icon_palo_alto_cortex_xdr.util.api.CortexXdrAPI.build_request", side_effect=Util.mocked_requests)
    def setUpClass(cls, mock_post) -> None:
        _, cls.task = Util.default_connector(
            MonitorAlerts(),
            connect_params={
                Input.API_KEY: {"secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"},
                Input.API_KEY_ID: 15,
                Input.SECURITY_LEVEL: "Advanced",
                Input.URL: "https://example.com/",
            },
        )

    @parameterized.expand(
        [
            [
                "starting",
                {},
                {},
                True,
                Util.load_expected("monitor_alerts"),
                STUB_STATE_MORE_PAGES,
                200,
                None,
            ],
            [
                "next_page",
                STUB_STATE_MORE_PAGES,
                {},
                True,
                Util.load_expected("monitor_alert_two"),
                STUB_STATE_EXPECTED_SECOND_PAGE,
                200,
                None,
            ],
            ["final_page", STUB_STATE_EXPECTED_SECOND_PAGE, {}, False, [], STUB_STATE_EXPECTED_NO_PAGE, 200, None],
        ]
    )
    def test_monitor_alerts(
        self,
        mock_post,
        test_name,
        state,
        custom_config,
        expected_has_more_pages,
        expected_output,
        expected_state,
        expected_status_code,
        expected_error,
    ) -> None:
        self.maxDiff = None

        output, state, has_more_pages, status_code, error = self.task.run(
            params={}, state=state, custom_config=custom_config
        )
        # breakpoint()
        self.assertEqual(output, expected_output)
        self.assertEqual(state, expected_state)
        self.assertEqual(has_more_pages, expected_has_more_pages)
        self.assertEqual(status_code, expected_status_code)
        self.assertEqual(error, expected_error)
        validate(output, MonitorAlertsOutput.schema)

    # @parameterized.expand(
    #     [
    #         [
    #             "400",
    #             {},
    #             400,
    #             "The server is unable to process the request.",
    #             "Verify your plugin input is correct and not malformed and try again. If the issue persists, please contact support.",
    #         ],
    #         [
    #             "401",
    #             {},
    #             401,
    #             "The account configured in your connection is unauthorized to access this service.",
    #             "Verify the permissions for your account and try again.",
    #         ],
    #         [
    #             "403",
    #             {},
    #             401,
    #             "The account configured in your connection is unauthorized to access this service.",
    #             "Verify the permissions for your account and try again.",
    #         ],
    #         [
    #             "404",
    #             {},
    #             404,
    #             "Invalid or unreachable endpoint provided.",
    #             "Verify the URLs or endpoints in your configuration are correct.",
    #         ],
    #         [
    #             "500",
    #             {},
    #             500,
    #             "Server error occurred",
    #             "Verify your plugin connection inputs are correct and not malformed and try again. If the issue persists, please contact support.",
    #         ],
    #     ]
    # )
    # def test_errors(
    #         self,
    #         mock_post,
    #         test_name,
    #         state,
    #         expected_status_code,
    #         expected_cause,
    #         expected_assistance,
    # ) -> None:

    #     output, state, has_more_pages, status_code, error = self.task.run(
    #         params={}, state=state
    #     )

    #     self.assertEqual(False, has_more_pages)
    #     self.assertEqual(expected_status_code, status_code)
    #     self.assertEqual(expected_cause, error.cause)
    #     self.assertEqual(expected_assistance, error.assistance)
