from unittest import TestCase
from unittest.mock import patch
from .mock import mock_connection, mock_action, mock_params
from timeout_decorator import timeout_decorator


class TestPollSandboxSuspiciousList(TestCase):
    def setUp(self):
        self.action_name = "PollSandboxSuspiciousList"
        self.connection = mock_connection()
        self.action = mock_action(self.connection, self.action_name)
        self.mock_params = mock_params("poll_sandbox_suspicious_list")

    @timeout_decorator.timeout(15)
    @patch(
        "icon_trendmicro_visionone.triggers.poll_sandbox_suspicious_list.PollSandboxSuspiciousList.send",
        side_effect=lambda output: None,
    )
    def test_integration_poll_sandbox_suspicious_list(self, mock_send):
        try:
            self.action.run(self.mock_params["input"])
        except timeout_decorator.TimeoutError as e:
            self.assertIsInstance(e, timeout_decorator.TimeoutError)
        else:
            self.fail("Expected TimeoutError was not raised.")
