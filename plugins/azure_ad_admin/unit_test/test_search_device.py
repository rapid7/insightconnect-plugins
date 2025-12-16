import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_azure_ad_admin.actions.search_device import SearchDevice
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mocked_requests)
class TestSearchDevice(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests)
    def setUpClass(cls, mock_request: MagicMock) -> None:
        cls.action = Util.default_connector(SearchDevice())

    @parameterized.expand(
        [
            [
                "no_parameters",
                Util.read_file_to_dict("inputs/search_device_no_parameters.json.inp"),
                Util.read_file_to_dict("expected/search_device_no_parameters.json.exp"),
            ],
            [
                "all_parameters",
                Util.read_file_to_dict("inputs/search_device_all_parameters.json.inp"),
                Util.read_file_to_dict("expected/search_device_all_parameters.json.exp"),
            ],
            [
                "pagination_two_pages",
                Util.read_file_to_dict("inputs/search_device_pagination.json.inp"),
                Util.read_file_to_dict("expected/search_device_pagination.json.exp"),
            ],
            [
                "pagination_single_page",
                Util.read_file_to_dict("inputs/search_device_pagination_single_page.json.inp"),
                Util.read_file_to_dict("expected/search_device_pagination_single_page.json.exp"),
            ],
            [
                "pagination_multiple_pages",
                Util.read_file_to_dict("inputs/search_device_pagination_multiple_pages.json.inp"),
                Util.read_file_to_dict("expected/search_device_pagination_multiple_pages.json.exp"),
            ],
        ]
    )
    def test_search_device(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], expected: Dict[str, Any]
    ) -> None:
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_parameters",
                Util.read_file_to_dict("inputs/search_device_invalid_parameters.json.inp"),
                PluginException.causes.get(PluginException.Preset.BAD_REQUEST),
                PluginException.assistances.get(PluginException.Preset.BAD_REQUEST),
            ],
        ]
    )
    def test_search_device_raise_exception(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], cause: str, assistance: str
    ) -> None:
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)

    def test_search_device_pagination_loop_limit(self, mock_request: MagicMock) -> None:
        input_params = Util.read_file_to_dict("inputs/search_device_pagination_loop_limit.json.inp")
        actual = self.action.run(input_params)

        # Should return 1000 devices (1 device per page * 1000 iterations)
        # Even though the API keeps returning nextLink
        self.assertEqual(len(actual["devices"]), 1000)

        # All devices should have the same structure
        for device in actual["devices"]:
            self.assertEqual(device["displayName"], "DummyLoopLimitDevice")
            self.assertEqual(device["id"], "00000000-0000-0000-0000-000000000999")

    def test_search_device_pagination_stops_at_last_page(self, mock_request: MagicMock) -> None:
        input_params = Util.read_file_to_dict("inputs/search_device_pagination_single_page.json.inp")
        actual = self.action.run(input_params)

        # Should have exactly 1 device since there's only one page
        self.assertEqual(len(actual["devices"]), 1)
        self.assertEqual(actual["devices"][0]["id"], "00000000-0000-0000-0000-000000000001")
        self.assertEqual(actual["devices"][0]["displayName"], "DummySinglePageDevice")
