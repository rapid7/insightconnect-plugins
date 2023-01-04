import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_happyfox.actions.list_tickets import ListTickets
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mocked_requests)
class TestListTickets(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListTickets())

    @parameterized.expand(Util.load_parameters("list_tickets").get("parameters"))
    def test_list_tickets(self, mock_request, name, inputs, expected):
        actual = self.action.run(inputs)
        self.assertEqual(actual, expected)
