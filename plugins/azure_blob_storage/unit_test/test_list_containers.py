import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unit_test.util import Util
from parameterized import parameterized
from icon_azure_blob_storage.actions.list_containers import ListContainers


@patch("requests.request", side_effect=Util.mock_request)
class TestListContainers(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mock_request)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(ListContainers())

    @parameterized.expand(
        [
            [
                "all_parameters",
                Util.read_file_to_dict("inputs/list_containers.json.inp"),
                Util.read_file_to_dict("expected/list_containers.json.exp"),
            ],
            [
                "without_include",
                Util.read_file_to_dict("inputs/list_containers_without_include.json.inp"),
                Util.read_file_to_dict("expected/list_containers_without_include.json.exp"),
            ],
            [
                "without_prefix",
                Util.read_file_to_dict("inputs/list_containers_without_prefix.json.inp"),
                Util.read_file_to_dict("expected/list_containers_without_prefix.json.exp"),
            ],
        ]
    )
    def test_list_containers(self, mock_request, test_name, input_parameters, expected):
        actual = self.action.run(input_parameters)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            ["no_parameters", {}, "No input parameters provided.", "Please provide at least one input parameter.", ""],
            [
                "invalid_include",
                Util.read_file_to_dict("inputs/list_containers_invalid_include.json.inp"),
                "Invalid input parameters.",
                "Please verify inputs and if the issue persists, contact support.",
                Util.read_file_to_string("expected/list_containers_invalid_include.json.exp"),
            ],
        ]
    )
    def test_list_containers_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance, data):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)
