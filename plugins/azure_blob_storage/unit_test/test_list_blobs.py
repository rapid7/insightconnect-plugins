import os
import sys
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from typing import Any

from icon_azure_blob_storage.actions.list_blobs import ListBlobs
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mock_request)
class TestListBlobs(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mock_request)
    def setUpClass(cls, mock_request: MagicMock) -> None:
        cls.action = Util.default_connector(ListBlobs())

    @parameterized.expand(
        [
            [
                "all_parameters",
                Util.read_file_to_dict("inputs/list_blobs.json.inp"),
                Util.read_file_to_dict("expected/list_blobs.json.exp"),
            ],
            [
                "without_include",
                Util.read_file_to_dict("inputs/list_blobs_without_include.json.inp"),
                Util.read_file_to_dict("expected/list_blobs_without_include.json.exp"),
            ],
            [
                "without_prefix",
                Util.read_file_to_dict("inputs/list_blobs_without_prefix.json.inp"),
                Util.read_file_to_dict("expected/list_blobs_without_prefix.json.exp"),
            ],
            [
                "without_delimiter",
                Util.read_file_to_dict("inputs/list_blobs_without_delimiter.json.inp"),
                Util.read_file_to_dict("expected/list_blobs_without_delimiter.json.exp"),
            ],
        ]
    )
    def test_list_blobs(
        self, mock_request: MagicMock, test_name: str, input_parameters: dict[str, Any], expected: dict[str, Any]
    ) -> None:
        actual = self.action.run(input_parameters)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_include",
                Util.read_file_to_dict("inputs/list_blobs_invalid_include.json.inp"),
                "Invalid input parameters.",
                "Please verify inputs and if the issue persists, contact support.",
                Util.read_file_to_string("expected/list_blobs_invalid_include.json.exp"),
            ],
            [
                "container_not_found",
                Util.read_file_to_dict("inputs/list_blobs_container_not_found.json.inp"),
                "Resource not found.",
                "Please verify inputs and if the issue persists, contact support.",
                Util.read_file_to_string("expected/container_not_found.json.exp"),
            ],
        ]
    )
    def test_list_blobs_raise_exception(
        self,
        mock_request: MagicMock,
        test_name: str,
        input_parameters: dict[str, Any],
        cause: str,
        assistance: str,
        data: dict[str, Any],
    ) -> None:
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)
