from unittest import TestCase
from unittest.mock import patch

from timeout_decorator import timeout_decorator

from icon_trendmicro_visionone.triggers import PollOatList
from mock import mock_connection, mock_params


class TestPollOatList(TestCase):
    def setUp(self):
        self.action = PollOatList()
        self.connection = mock_connection()
        self.action.connection = self.connection
        self.mock_params = mock_params("poll_oat_list")

    @timeout_decorator.timeout(15)
    @patch(
        "icon_trendmicro_visionone.triggers.poll_oat_list.PollOatList.send",
        side_effect=lambda output: None,
    )
    def test_integration_poll_oat_list(self, mock_send):
        try:
            self.action.run(self.mock_params["input"])
        except timeout_decorator.TimeoutError as e:
            self.assertIsInstance(e, timeout_decorator.TimeoutError)
        else:
            self.fail("Expected TimeoutError was not raised.")
