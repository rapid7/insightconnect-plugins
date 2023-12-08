import os
import sys

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from jsonschema import validate
from komand_salesforce.actions.simple_search import SimpleSearch
from komand_salesforce.actions.simple_search.schema import SimpleSearchOutput
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mock_request)
class TestSimpleSearch(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mock_request)
    def setUpClass(cls, mock_req) -> None:
        cls.action = Util.default_connector(SimpleSearch())

    @parameterized.expand(
        [
            [
                "valid_text",
                Util.read_file_to_dict("inputs/simple_search_valid_text.json.inp"),
                Util.read_file_to_dict("expected/simple_search_valid_text.json.exp"),
            ]
        ]
    )
    def test_simple_search(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], expected: Dict[str, Any]
    ) -> None:
        actual = self.action.run(input_params)
        validate(actual, SimpleSearchOutput.schema)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "empty_text",
                Util.read_file_to_dict("inputs/simple_search_empty_text.json.inp"),
                PluginException.causes[PluginException.Preset.BAD_REQUEST],
                PluginException.assistances[PluginException.Preset.BAD_REQUEST],
            ]
        ]
    )
    def test_simple_search_raise_exception(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], cause: str, assistance: str
    ) -> None:
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
