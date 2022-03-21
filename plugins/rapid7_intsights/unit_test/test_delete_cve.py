import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from unit_test.util import Util
from icon_rapid7_intsights.actions.delete_cve import DeleteCve
from icon_rapid7_intsights.actions.delete_cve.schema import Input


class TestGetCveByID(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mock_request)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(DeleteCve())

    @patch("requests.request", side_effect=Util.mock_request)
    def test_delete_cve_empty(self, make_request):
        actual = self.action.run()
        expected = Util.read_file_to_dict("expecteds/delete_cve_empty.json.resp")
        self.assertEqual(expected, actual)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_delete_cve_with_one_id(self, make_request):
        actual = self.action.run({"cve_id": ["CVE-1999-0003"]})
        expected = Util.read_file_to_dict("expecteds/delete_cve_with_one_id.json.resp")
        self.assertEqual(expected, actual)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_delete_cve_with_many_id(self, make_request):
        actual = self.action.run({Input.CVE_ID: ["CVE-2021-3739", "CVE-2020-7064", "CVE-1999-003"]})
        expected = Util.read_file_to_dict("expecteds/delete_cve_with_many_id.json.resp")
        self.assertEqual(expected, actual)
