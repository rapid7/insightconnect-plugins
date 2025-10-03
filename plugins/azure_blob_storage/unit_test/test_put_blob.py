import os
import sys
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from typing import Any

from icon_azure_blob_storage.actions.put_blob import PutBlob
from icon_azure_blob_storage.actions.put_blob.schema import Output
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mock_request)
class TestPutBlob(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mock_request)
    def setUpClass(cls, mock_request: MagicMock) -> None:
        cls.action = Util.default_connector(PutBlob())

    @parameterized.expand(
        [
            [
                "page_blob",
                Util.read_file_to_dict("inputs/put_blob_page_blob.json.inp"),
            ],
            [
                "block_blob",
                Util.read_file_to_dict("inputs/put_blob_block_blob.json.inp"),
            ],
            [
                "append_blob",
                Util.read_file_to_dict("inputs/put_blob_append_blob.json.inp"),
            ],
        ]
    )
    def test_put_blob(self, mock_request: MagicMock, test_name: str, input_parameters: dict[str, Any]) -> None:
        actual = self.action.run(input_parameters)
        self.assertEqual(
            actual,
            {Output.SUCCESS: True, Output.MESSAGE: "Blob was successfully created."},
        )

    @parameterized.expand(
        [
            [
                "access_tier_not_supported",
                Util.read_file_to_dict("inputs/put_blob_access_tier_not_supported.json.inp"),
                "Invalid input parameters.",
                "Please verify inputs and if the issue persists, contact support.",
                Util.read_file_to_string("expected/put_blob_access_tier_not_supported.json.exp"),
            ],
            [
                "container_not_found",
                Util.read_file_to_dict("inputs/put_blob_container_not_found.json.inp"),
                "Resource not found.",
                "Please verify inputs and if the issue persists, contact support.",
                Util.read_file_to_string("expected/container_not_found.json.exp"),
            ],
            [
                "invalid_blob_type",
                Util.read_file_to_dict("inputs/put_blob_invalid_blob_type.json.inp"),
                "Request made conflicts with an existing resource.",
                "Please verify inputs and if the issue persists, contact support.",
                Util.read_file_to_string("expected/put_blob_invalid_blob_type.json.exp"),
            ],
        ]
    )
    def test_put_blob_raise_exception(
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
