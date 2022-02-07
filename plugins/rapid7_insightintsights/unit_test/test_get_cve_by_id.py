import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from unit_test.util import Util
from icon_rapid7_intsights.actions.get_cve_by_id import GetCveById
from icon_rapid7_intsights.actions.get_cve_by_id.schema import Input


class TestGetCveByID(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mock_request)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(GetCveById())

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_cve_by_id_empty(self, make_request):
        actual = self.action.run()
        expected = Util.read_file_to_dict("expecteds/get_cve_by_id_all.json.resp")
        self.assertEqual(expected, actual)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_cve_with_offset(self, make_request):
        self.maxDiff = None
        actual = self.action.run({Input.CVE_ID: ["CVE-2021-7064"]})
        expected = Util.read_file_to_dict("expecteds/get_cve_by_id_with_offset.json.resp")
        self.assertEqual(expected, actual)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_cve_by_id_with_one_id(self, make_request):
        actual = self.action.run({Input.CVE_ID: ["CVE-2020-7064"]})
        expected = Util.read_file_to_dict("expecteds/get_cve_by_id.json.resp")
        self.assertEqual(expected, actual)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_cve_by_id_with_many_id(self, make_request):
        actual = self.action.run({Input.CVE_ID: ["CVE-2021-3739", "CVE-2020-7064"]})
        expected = Util.read_file_to_dict("expecteds/get_cve_by_id_all.json.resp")
        self.assertEqual(expected, actual)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_cve_by_id_empty_response(self, make_request):
        actual = self.action.run({Input.CVE_ID: ["empty"]})
        expected = {"content": []}
        self.assertEqual(expected, actual)
