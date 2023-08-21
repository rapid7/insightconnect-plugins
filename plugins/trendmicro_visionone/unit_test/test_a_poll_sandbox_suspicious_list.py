from unittest import TestCase, skip
from unittest.mock import patch

from timeout_decorator import timeout_decorator

from icon_trendmicro_visionone.triggers import PollSandboxSuspiciousList
from .tmv1_mock import mock_connection, mock_params


class TestPollSandboxSuspiciousList(TestCase):
    def setUp(self):
        self.action = PollSandboxSuspiciousList()
        self.connection = mock_connection()
        self.action.connection = self.connection
        self.mock_params = mock_params("poll_sandbox_suspicious_list")

    @timeout_decorator.timeout(15)
    @patch(
        "icon_trendmicro_visionone.triggers.poll_sandbox_suspicious_list.PollSandboxSuspiciousList.send",
        side_effect=lambda output: None,
    )
    @skip("Integration test - we don't want to run this, and it is getting 500 from endpoint causing a failure.")
    def test_integration_poll_sandbox_suspicious_list(self, mock_send):
        try:
            self.action.run(self.mock_params["input"])
        except timeout_decorator.TimeoutError as e:
            self.assertIsInstance(e, timeout_decorator.TimeoutError)
        else:
            self.fail("Expected TimeoutError was not raised.")
