import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_salesforce.actions.advanced_search import AdvancedSearch
from komand_salesforce.actions.advanced_search.schema import AdvancedSearchOutput
from komand_salesforce.util.exceptions import ApiException
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mock_request)
class TestAdvancedSearch(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(AdvancedSearch())

    @parameterized.expand(
        [
            [
                "all",
                Util.read_file_to_dict("inputs/advanced_search_all.json.inp"),
                Util.read_file_to_dict("expected/advanced_search_all.json.exp"),
            ],
            [
                "by_name",
                Util.read_file_to_dict("inputs/advanced_search_by_name.json.inp"),
                Util.read_file_to_dict("expected/advanced_search_by_name.json.exp"),
            ],
            [
                "more_pages",
                Util.read_file_to_dict("inputs/advanced_search_more_pages.json.inp"),
                Util.read_file_to_dict("expected/advanced_search_more_pages.json.exp"),
            ],
            [
                "empty",
                Util.read_file_to_dict("inputs/advanced_search_empty.json.inp"),
                Util.read_file_to_dict("expected/advanced_search_empty.json.exp"),
            ],
        ]
    )
    def test_advanced_search(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], expected: Dict[str, Any]
    ) -> None:
        actual = self.action.run(input_params)
        validate(actual, AdvancedSearchOutput.schema)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_query",
                Util.read_file_to_dict("inputs/advanced_search_invalid_query.json.inp"),
                PluginException.causes[PluginException.Preset.BAD_REQUEST],
                PluginException.assistances[PluginException.Preset.BAD_REQUEST],
            ]
        ]
    )
    def test_advanced_search_raise_api_exception(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], cause: str, assistance: str
    ) -> None:
        with self.assertRaises(ApiException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
