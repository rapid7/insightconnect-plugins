import json
import sys
import os

sys.path.append(os.path.abspath('../'))
# Custom Imports

from unittest.mock import patch
from icon_cybereason.actions.search_for_files.schema import Input
from unittest import TestCase
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_cybereason.actions.search_for_files import SearchForFiles
from unit_test.util import Util


class TestSearchForFiles(TestCase):
    @classmethod
    @patch("requests.sessions.Session.post", side_effect=Util.mocked_requests_session)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(SearchForFiles())

    @patch("requests.sessions.Session.request", side_effect=Util.mocked_requests_session)
    def test_search_for_files(self, mock_request):
        actual = self.action.run(
            {
                Input.SERVER_FILTER: 'machineName: ["rapid7-windows"]',
                Input.FILE_FILTER: 'fileName Equals: ["sample.py"]'
            }
        )
        expected = '"totalNumberOfProbes": 1'
        assert json.dumps(actual).__contains__(expected)

    # def test_search_for_files_bad(self):
    #     with self.assertRaises(PluginException):
    #         actual = self.action.run(
    #             {
    #                 Input.SERVER_FILTER: 'machineName: ["rapid7-windows"]',
    #                 Input.FILE_FILTER: ""
    #             }
    #         )
