import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import Mock, patch

from icon_palo_alto_cortex_xdr.tasks.monitor_alerts import MonitorAlerts
from icon_palo_alto_cortex_xdr.tasks.monitor_alerts.schema import MonitorAlertsOutput

from parameterized import parameterized
from jsonschema import validate
from freezegun import freeze_time
from util import Util


@patch("requests.request", side_effect=Util.mocked_requests)
@patch("requests.post", side_effect=Util.mocked_requests)
class TestMonitorAlerts(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.task = Util.default_connector(MonitorAlerts())

    def test_monitor_alerts(
        self,
        mock_request: Mock,
        mock_post: Mock,
        test_name,
        start_time,
        input_state,
        expected_has_more_pages,
        expected_output,
        expected_state,
        expected_status_code,
        expected_error,
    ) -> None:
        with freeze_time(start_time):
            actual, actual_state, has_more_pages, status_code, error = self.task.run(state=input_state)
            self.assertEqual(actual, expected_output)
            self.assertEqual(actual_state, expected_state)
            self.assertEqual(has_more_pages, expected_has_more_pages)
            self.assertEqual(status_code, expected_status_code)
            self.assertEqual(error, expected_error)
            validate(actual, MonitorAlertsOutput.schema)

    @parameterized.expand(Util.load_parameters("monitor_alerts_custom_config").get("parameters"))
    def test_monitor_alerts_custm_config(
        self,
        mock_request: Mock,
        mock_post: Mock,
        test_name,
        start_time,
        input_state,
        input_config,
        expected_has_more_pages,
        expected_output,
        expected_state,
        expected_status_code,
        expected_error,
    ) -> None:
        with freeze_time(start_time):
            actual, actual_state, has_more_pages, status_code, error = self.task.run(
                state=input_state, custom_config=input_config
            )
            self.assertEqual(actual, expected_output)
            self.assertEqual(actual_state, expected_state)
            self.assertEqual(has_more_pages, expected_has_more_pages)
            self.assertEqual(status_code, expected_status_code)
            self.assertEqual(error, expected_error)

    @parameterized.expand(Util.load_parameters("monitor_alerts_error").get("parameters"))
    def test_monitor_alerts_error(
        self,
        mock_request: Mock,
        mock_post: Mock,
        test_name,
        start_time,
        input_state,
        expected_has_more_pages,
        expected_status_code,
        expected_error,
    ) -> None:
        with freeze_time(start_time):
            actual, actual_state, has_more_pages, status_code, error = self.task.run(state=input_state)
            self.assertEqual(has_more_pages, expected_has_more_pages)
            self.assertEqual(status_code, expected_status_code)
            self.assertEqual(error.cause, expected_error.get("cause"))
            self.assertEqual(error.data, expected_error.get("data"))
            validate(actual, MonitorAlertsOutput.schema)
