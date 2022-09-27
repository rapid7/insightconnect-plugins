import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from unit_test.util import Util
from icon_rapid7_intsights.actions.get_cve_list import GetCveList
from icon_rapid7_intsights.actions.get_cve_list.schema import Input


class TestGetCveByID(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mock_request)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(GetCveList())

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_cve_list(self, make_request):
        actual = self.action.run({Input.OFFSET: "2000-00-00T00:00:00.000Z::614b8972da44a60005036b01"})
        expected = Util.read_file_to_dict("expecteds/get_cve_list.json.resp")
        self.assertEqual(expected, actual)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_cve_list_no_offset(self, make_request):
        actual = self.action.run()
        expected = Util.read_file_to_dict("expecteds/get_cve_by_id_all.json.resp")
        expected["next_offset"] = "2000-00-00T00:00:00.000Z::614b8972da44a60005036b01"
        self.assertEqual(expected, actual)
