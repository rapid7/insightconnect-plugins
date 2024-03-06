import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_joe_sandbox.actions.list_countries import ListCountries
from icon_joe_sandbox.actions.list_countries.schema import Output
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request, MagicMock


class TestListCountries(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(ListCountries())

    @patch("requests.request", side_effect=mock_request_200)
    def test_list_countries(self, mock_get: MagicMock) -> None:
        mocked_request(mock_get)
        response = self.action.run()

        expected = {Output.COUNTRIES: [{"name": "Argentina"}, {"name": "Australia"}]}
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
