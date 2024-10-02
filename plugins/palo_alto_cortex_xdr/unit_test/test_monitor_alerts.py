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
from mock import mock_request_200

STUB_STATE_EXPECTED = {
    "last_alert_time": 1706540499609,
    "last_alert_hash": ["a502a9c50798186882ad8dc91ac2b38eb185c404"],
}


@freeze_time("2024-01-29T15:01:00.000000Z")
@patch("requests.Session.send", side_effect=mock_request_200)
class TestMonitorAlerts(TestCase):
    @classmethod
    @patch("requests.Session.send", side_effect=mock_request_200)
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
                "initial_run_has_no_more_pages",
                {},
                {},
                False,
                Util.load_expected("monitor_alerts"),
                STUB_STATE_EXPECTED,
                200,
                None,
            ],
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

        output, state, has_more_pages, status_code, error = self.task.run(
            params={}, state=state, custom_config=custom_config
        )
        self.assertEqual(output, expected_output)
        self.assertEqual(state, expected_state)
        self.assertEqual(has_more_pages, expected_has_more_pages)
        self.assertEqual(status_code, expected_status_code)
        self.assertEqual(error, expected_error)
        validate(output, MonitorAlertsOutput.schema)


# @parameterized.expand(Util.load_parameters("monitor_alerts_custom_config").get("parameters"))
# def test_monitor_alerts_custm_config(
#     self,
#     mock_request: Mock,
#     mock_post: Mock,
#     test_name,
#     start_time,
#     input_state,
#     input_config,
#     expected_has_more_pages,
#     expected_output,
#     expected_state,
#     expected_status_code,
#     expected_error,
# ) -> None:
#     with freeze_time(start_time):
#         actual, actual_state, has_more_pages, status_code, error = self.task.run(
#             state=input_state, custom_config=input_config
#         )
#         self.assertEqual(actual, expected_output)
#         self.assertEqual(actual_state, expected_state)
#         self.assertEqual(has_more_pages, expected_has_more_pages)
#         self.assertEqual(status_code, expected_status_code)
#         self.assertEqual(error, expected_error)

# @parameterized.expand(Util.load_parameters("monitor_alerts_error").get("parameters"))
# @patch("requests.Session.send", side_effect=mock_request_500)

# def test_monitor_alerts_error(
#     self,
#     test_name,
#     start_time,
#     input_state,
#     expected_has_more_pages,
#     expected_output,
#     expected_state,
#     expected_status_code,
#     expected_error,
#     mock_post,
# ) -> None:
#     with freeze_time(start_time):

#         mocked_request(mock_post)

#         actual, actual_state, has_more_pages, status_code, error = self.task.run(state=input_state)
#         self.assertEqual(actual, expected_output)
#         self.assertEqual(actual_state, expected_state)
#         self.assertEqual(has_more_pages, expected_has_more_pages)
#         self.assertEqual(status_code, expected_status_code)
#         self.assertEqual(error, expected_error)
#         validate(actual, MonitorAlertsOutput.schema)

# @parameterized.expand(
#         [
#             [
#                 "400",
#                 {},
#                 400,
#                 "The server is unable to process the request.",
#                 "Verify your plugin input is correct and not malformed and try again. If the issue persists, please contact support.",
#             ]
#         ]
# )
# @patch("requests.Session.send", side_effect=mock_request_error)


# def test_monitor_logs_api_errors(

#     self,
#     test_name,
#     start_time,
#     input_state,
#     expected_status_code,
#     expected_cause,
#     expected_assistance,
#     mock_post
# ):
#     with freeze_time(start_time):

#         output, state, has_more_pages, status_code, error = self.task.run(state=input_state)

#         mocked_request(mock_post)

#         self.assertEqual(False, has_more_pages)
#         self.assertEqual(expected_status_code, status_code)
#         self.assertEqual(expected_cause, error.cause)
#         self.assertEqual(expected_assistance, error.assistance)
