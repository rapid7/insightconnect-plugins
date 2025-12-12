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
