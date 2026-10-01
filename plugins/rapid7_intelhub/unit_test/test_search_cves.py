import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_rapid7_intelhub.actions.search_cves import SearchCves
from komand_rapid7_intelhub.actions.search_cves.schema import Input

from util import STUB_INVALID_LAST_UPDATED, Util


class TestSearchCves(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(SearchCves())

    @patch("requests.request", side_effect=Util.mock_request)
    def test_search_cves(self, mock_request: MagicMock) -> None:
        input_params = {Input.SEARCH: "CVE-2024-340", Input.PAGE: 1, Input.PAGE_SIZE: 3}
        validate(input_params, self.action.input.schema)
        response = self.action.run(input_params)
        validate(response, self.action.output.schema)
        self.assertEqual(Util.read_file_to_dict("expected/search_cves.json.exp"), response)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_search_cves_with_filters(self, mock_request: MagicMock) -> None:
        input_params = {
            Input.SEARCH: "CVE-2024",
            Input.PAGE: 2,
            Input.PAGE_SIZE: 3,
            Input.CVSS_SCORE: "informational",
            Input.EXPLOITABLE: False,
            Input.EPSS_SCORE: "0.5-1",
            Input.CISA_KEV: True,
            Input.LAST_UPDATED: "last 24 hours",
        }
        validate(input_params, self.action.input.schema)
        self.action.run(input_params)
        self.assertEqual(
            {
                "page": 2,
                "page-size": 3,
                "search": "CVE-2024",
                "cvss-score": "informational",
                "exploitable": "false",
                "epss-score": "0.5-1",
                "cisa-kev": "true",
                "last-updated": "last 24 hours",
            },
            mock_request.call_args.kwargs["params"],
        )

    @patch("requests.request", side_effect=Util.mock_request)
    def test_search_cves_raise_exception(self, mock_request: MagicMock) -> None:
        # The validation message of the API has to reach the user for status codes the plugin does not map
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.LAST_UPDATED: STUB_INVALID_LAST_UPDATED})
        self.assertEqual("Unknown error occurred. Status code: 422", context.exception.cause)
        self.assertIn("Input should be 'last 20 minutes'", context.exception.assistance)
