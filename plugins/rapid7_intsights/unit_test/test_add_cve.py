import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from util import Util
from icon_rapid7_intsights.actions.add_cve import AddCve
from icon_rapid7_intsights.actions.add_cve.schema import Input, AddCveInput, AddCveOutput
from jsonschema import validate


class TestGetCveByID(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mock_request)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(AddCve())

    @patch("requests.request", side_effect=Util.mock_request)
    def test_add_cve_empty(self, make_request):
        validate({}, AddCveInput.schema)
        actual = self.action.run()
        expected = Util.read_file_to_dict("expecteds/add_cve_empty.json.resp")
        self.assertEqual(expected, actual)
        validate(actual, AddCveOutput.schema)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_add_cve_empty_list(self, make_request):
        input_params = {Input.CVE_ID: []}
        validate(input_params, AddCveInput.schema)
        actual = self.action.run(input_params)
        expected = Util.read_file_to_dict("expecteds/add_cve_empty.json.resp")
        self.assertEqual(expected, actual)
        validate(actual, AddCveOutput.schema)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_add_cve_with_one_id(self, make_request):
        input_params = {Input.CVE_ID: ["CVE-1999-0003"]}
        validate(input_params, AddCveInput.schema)
        actual = self.action.run(input_params)
        expected = Util.read_file_to_dict("expecteds/add_cve_with_one_id.json.resp")
        self.assertEqual(expected, actual)
        validate(actual, AddCveOutput.schema)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_add_cve_with_many_id(self, make_request):
        input_params = {Input.CVE_ID: ["CVE-2021-3739", "CVE-2020-7064", "CVE-1999-003"]}
        validate(input_params, AddCveInput.schema)
        actual = self.action.run(input_params)
        expected = Util.read_file_to_dict("expecteds/add_cve_with_many_id.json.resp")
        self.assertEqual(expected, actual)
        validate(actual, AddCveOutput.schema)
