from unittest import TestCase, skip
from unittest.mock import patch

from timeout_decorator import timeout_decorator

from icon_trendmicro_visionone.triggers import PollAlertList
from mock import mock_connection, mock_params


class TestPollAlertList(TestCase):
    def setUp(self):
        self.action = PollAlertList()
        self.connection = mock_connection()
        self.action.connection = self.connection
        self.mock_params = mock_params("poll_alert_list")

    @skip("Integration test - we don't want to run this, and it is getting 500 from endpoint causing a failure.")
    @timeout_decorator.timeout(15)
    @patch(
        "icon_trendmicro_visionone.triggers.poll_alert_list.PollAlertList.send",
        side_effect=lambda output: None,
    )
    def test_integration_poll_alert_list(self, mock_send):
        try:
            self.action.run(self.mock_params["input"])
        except timeout_decorator.TimeoutError as error:
            self.assertIsInstance(error, timeout_decorator.TimeoutError)
        else:
            self.fail("Expected TimeoutError was not raised.")
