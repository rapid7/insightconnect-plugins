import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_easyvista.actions.search_tickets import SearchTickets
from icon_easyvista.actions.search_tickets.schema import Input
from util import Util
from unittest.mock import patch
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mocked_requests)
class TestSearchTickets(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(SearchTickets())

    @parameterized.expand(Util.load_parameters("search_ticket").get("parameters"))
    def test_search_tickets(self, mock_request, name, query, expected):
        actual = self.action.run({Input.QUERY: query})
        self.assertEqual(actual, expected)
