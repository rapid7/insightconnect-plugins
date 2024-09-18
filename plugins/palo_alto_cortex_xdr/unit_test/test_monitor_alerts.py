import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock

from icon_palo_alto_cortex_xdr.tasks.monitor_alerts import MonitorAlerts
from icon_palo_alto_cortex_xdr.tasks.monitor_alerts.schema import MonitorAlertsOutput

from icon_palo_alto_cortex_xdr.connection.schema import Input

from parameterized import parameterized
from jsonschema import validate
from freezegun import freeze_time
from util import Util
from mock import mock_request_200, mocked_request


class TestMonitorAlerts(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        _, cls.task = Util.default_connector(
            MonitorAlerts(),
            connect_params={
                Input.API_KEY: {"secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"},
                Input.API_KEY_ID: 15,
                Input.SECURITY_LEVEL: "Advanced",
                Input.URL: "https://example.com/",
            },
        )

    @parameterized.expand(Util.load_parameters("monitor_alerts").get("parameters"))
    @patch("requests.Session.send", side_effect=mock_request_200)
    def test_monitor_alerts(
        self,
        test_name,
        start_time,
        input_state,
        expected_has_more_pages,
        expected_output,
        expected_state,
        expected_status_code,
        expected_error,
        mock_post,
    ) -> None:

        with freeze_time(start_time):

            mocked_request(mock_post)

            actual, actual_state, has_more_pages, status_code, error = self.task.run(state=input_state)
            self.assertEqual(actual, expected_output)
            self.assertEqual(actual_state, expected_state)
            self.assertEqual(has_more_pages, expected_has_more_pages)
            self.assertEqual(status_code, expected_status_code)
            self.assertEqual(error, expected_error)
            validate(actual, MonitorAlertsOutput.schema)

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
    # def test_monitor_alerts_error(
    #     self,
    #     mock_request: Mock,
    #     mock_post: Mock,
    #     test_name,
    #     start_time,
    #     input_state,
    #     expected_has_more_pages,
    #     expected_status_code,
    #     expected_error,
    # ) -> None:
    #     with freeze_time(start_time):
    #         actual, actual_state, has_more_pages, status_code, error = self.task.run(state=input_state)
    #         self.assertEqual(has_more_pages, expected_has_more_pages)
    #         self.assertEqual(status_code, expected_status_code)
    #         self.assertEqual(error.cause, expected_error.get("cause"))
    #         self.assertEqual(error.data, expected_error.get("data"))
    #         validate(actual, MonitorAlertsOutput.schema)
