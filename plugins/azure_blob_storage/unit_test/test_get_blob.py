import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from util import Util
from parameterized import parameterized
from icon_azure_blob_storage.actions.get_blob import GetBlob


@patch("requests.request", side_effect=Util.mock_request)
class TestGetBlob(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mock_request)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(GetBlob())

    @parameterized.expand(
        [
            [
                "base_blob",
                Util.read_file_to_dict("inputs/get_blob.json.inp"),
                Util.read_file_to_dict("expected/get_blob.json.exp"),
            ],
            [
                "blob_snapshot",
                Util.read_file_to_dict("inputs/get_blob_snapshot.json.inp"),
                Util.read_file_to_dict("expected/get_blob.json.exp"),
            ],
            [
                "blob_version",
                Util.read_file_to_dict("inputs/get_blob_version.json.inp"),
                Util.read_file_to_dict("expected/get_blob.json.exp"),
            ],
        ]
    )
    def test_get_blob(self, mock_request, test_name, input_parameters, expected):
        actual = self.action.run(input_parameters)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "version_and_snapshot_used_together",
                Util.read_file_to_dict("inputs/get_blob_snapshot_version_used_together.json.inp"),
                "Invalid input parameters.",
                "Please verify inputs and if the issue persists, contact support.",
                Util.read_file_to_string("expected/blob_snapshot_version_used_together.json.exp"),
            ],
            [
                "container_not_found",
                Util.read_file_to_dict("inputs/get_blob_container_not_found.json.inp"),
                "Resource not found.",
                "Please verify inputs and if the issue persists, contact support.",
                Util.read_file_to_string("expected/container_not_found.json.exp"),
            ],
            [
                "blob_not_found",
                Util.read_file_to_dict("inputs/get_blob_blob_not_found.json.inp"),
                "Resource not found.",
                "Please verify inputs and if the issue persists, contact support.",
                Util.read_file_to_string("expected/blob_not_found.json.exp"),
            ],
        ]
    )
    def test_get_blob_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance, data):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)
