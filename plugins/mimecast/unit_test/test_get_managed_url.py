import os
import sys
from jsonschema import validate
from unittest import TestCase
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))

from komand_mimecast.actions import GetManagedUrl
from komand_mimecast.actions.get_managed_url.schema import GetManagedUrlOutput, GetManagedUrlInput

from util import Util


@patch("requests.request", side_effect=Util.mocked_request)
class TestGetManagedUrl(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetManagedUrl())

    def test_get_managed_url_no_filter(self, _mocked_request):
        input_data = Util.load_json("inputs/get_managed_url.json.exp")
        validate(input_data, GetManagedUrlInput.schema)
        actual = self.action.run(input_data)
        expect = Util.load_json("expected/get_managed_url.json.exp")
        self.assertEqual(expect, actual)
        validate(actual, GetManagedUrlOutput.schema)

    def test_get_managed_url_filtered_by_action(self, _mocked_request):
        input_data = Util.load_json("inputs/get_managed_url_filtered_by_action.json.exp")
        validate(input_data, GetManagedUrlInput.schema)
        actual = self.action.run(input_data)
        expect = Util.load_json("expected/get_managed_url_filtered_by_action.json.exp")
        self.assertEqual(expect, actual)
        validate(actual, GetManagedUrlOutput.schema)

    def test_get_managed_url_filtered_by_scheme(self, _mocked_request):
        input_data = Util.load_json("inputs/get_managed_url_filtered_by_schema.json.exp")
        validate(input_data, GetManagedUrlInput.schema)
        actual = self.action.run(input_data)
        expect = Util.load_json("expected/get_managed_url_filtered_by_scheme.json.exp")
        self.assertEqual(expect, actual)
        validate(actual, GetManagedUrlOutput.schema)

    def test_get_managed_url_filtered_by_math_type(self, _mocked_request):
        input_data = Util.load_json("inputs/get_managed_url_filtered_by_mathtype.json.exp")
        validate(input_data, GetManagedUrlInput.schema)
        actual = self.action.run(input_data)
        expect = Util.load_json("expected/get_managed_url_empty_response.json.exp")
        self.assertEqual(expect, actual)
        validate(actual, GetManagedUrlOutput.schema)

    def test_get_managed_url_filtered_by_disabled(self, _mocked_request):
        input_data = Util.load_json("inputs/get_managed_url_filtered_by_disabled.json.exp")
        validate(input_data, GetManagedUrlInput.schema)
        actual = self.action.run(input_data)
        expect = Util.load_json("expected/get_managed_url.json.exp")
        self.assertEqual(expect, actual)
        validate(actual, GetManagedUrlOutput.schema)

    def test_get_managed_url_filtered_by_id(self, _mocked_request):
        input_data = Util.load_json("inputs/get_managed_url_filtered_by_id.json.exp")
        validate(input_data, GetManagedUrlInput.schema)
        actual = self.action.run(input_data)
        expect = Util.load_json("expected/get_managed_url_filtered_by_id.json.exp")
        self.assertEqual(expect, actual)
        validate(actual, GetManagedUrlOutput.schema)

    def test_empty_response(self, _mocked_request):
        input_data = Util.load_json("inputs/get_managed_url_with_filter.json.exp")
        validate(input_data, GetManagedUrlInput.schema)
        actual = self.action.run(input_data)
        expect = Util.load_json("expected/get_managed_url_empty_response.json.exp")
        self.assertEqual(expect, actual)
        validate(actual, GetManagedUrlOutput.schema)
