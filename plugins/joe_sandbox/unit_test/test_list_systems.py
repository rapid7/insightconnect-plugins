import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_joe_sandbox.actions.list_systems import ListSystems
from icon_joe_sandbox.actions.list_systems.schema import Output
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request


class TestListSystems(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(ListSystems())

    @patch("requests.request", side_effect=mock_request_200)
    def test_list_systems(self, mock_get):
        mocked_request(mock_get)
        response = self.action.run()

        expected = {
            Output.SYSTEMS: [
                {"name": "system1", "description": "system1desc", "arch": "WINDOWS", "count": 1},
                {"name": "system2", "description": "system2desc", "arch": "MAC", "count": 1},
            ]
        }
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
