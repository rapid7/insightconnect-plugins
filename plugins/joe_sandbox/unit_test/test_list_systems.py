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
                {
                    "name": "w10x64_office",
                    "description": "Windows 10 64 bit (version 1803) with <b>Office 2016</b> Adobe Reader DC 19, Chrome 104, Firefox 63, Java 8.171, Flash 30.0.0.113",
                    "arch": "WINDOWS",
                    "count": 8,
                },
                {
                    "name": "w7_1",
                    "description": "Windows 7 (<b>Office 2010 SP2</b>, Java 1.8.0_40 1.8.0_191, Flash 16.0.0.305, Acrobat Reader 11.0.08, Internet Explorer 11, Chrome 55, Firefox 43)",
                    "arch": "WINDOWS",
                    "count": 8,
                },
            ]
        }
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
