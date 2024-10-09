import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from util import Util
from parameterized import parameterized
from icon_azure_blob_storage.actions.delete_blob import DeleteBlob


@patch("requests.request", side_effect=Util.mock_request)
class TestDeleteBlob(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mock_request)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(DeleteBlob())

    @parameterized.expand(
        [
            [
                "delete_snapshot",
                Util.read_file_to_dict("inputs/delete_blob_snapshot.json.inp"),
                Util.read_file_to_dict("expected/delete_blob.json.exp"),
            ],
            [
                "delete_version",
                Util.read_file_to_dict("inputs/delete_blob_version.json.inp"),
                Util.read_file_to_dict("expected/delete_blob.json.exp"),
            ],
            [
                "delete_only_snapshots",
                Util.read_file_to_dict("inputs/delete_blob_only_snapshots.json.inp"),
                Util.read_file_to_dict("expected/delete_blob.json.exp"),
            ],
            [
                "delete_include_snapshots",
                Util.read_file_to_dict("inputs/delete_blob_include_snapshots.json.inp"),
                Util.read_file_to_dict("expected/delete_blob.json.exp"),
            ],
        ]
    )
    def test_delete_blob(self, mock_request, test_name, input_parameters, expected):
        actual = self.action.run(input_parameters)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "version_and_snapshot_used_together",
                Util.read_file_to_dict("inputs/delete_blob_snapshot_version_used_together.json.inp"),
                "Invalid input parameters.",
                "Please verify inputs and if the issue persists, contact support.",
                Util.read_file_to_string("expected/blob_snapshot_version_used_together.json.exp"),
            ],
            [
                "container_not_found",
                Util.read_file_to_dict("inputs/delete_blob_container_not_found.json.inp"),
                "Resource not found.",
                "Please verify inputs and if the issue persists, contact support.",
                Util.read_file_to_string("expected/container_not_found.json.exp"),
            ],
            [
                "blob_not_found",
                Util.read_file_to_dict("inputs/delete_blob_blob_not_found.json.inp"),
                "Resource not found.",
                "Please verify inputs and if the issue persists, contact support.",
                Util.read_file_to_string("expected/blob_not_found.json.exp"),
            ],
            [
                "snapshots_not_specified",
                Util.read_file_to_dict("inputs/delete_blob_no_snapshots.json.inp"),
                "Request made conflicts with an existing resource.",
                "Please verify inputs and if the issue persists, contact support.",
                Util.read_file_to_string("expected/delete_blob_no_snapshots.json.exp"),
            ],
        ]
    )
    def test_delete_blob_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance, data):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)
