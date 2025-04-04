import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized

from insightconnect_plugin_runtime.exceptions import PluginException

from util import Util
from icon_sophos_central.actions.add_allowed_item import AddAllowedItem


@patch("requests.request", side_effect=Util.mock_request)
class TestAddAllowedItem(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.action = Util.default_connector(AddAllowedItem())

    @parameterized.expand(
        [
            [
                "valid_data_path",
                Util.read_file_to_dict("inputs/add_allowed_item_path.json.inp"),
                Util.read_file_to_dict("expected/add_allowed_item_path.json.exp"),
            ],
            [
                "valid_data_sha256",
                Util.read_file_to_dict("inputs/add_allowed_item_sha256.json.inp"),
                Util.read_file_to_dict("expected/add_allowed_item_sha256.json.exp"),
            ],
            [
                "valid_data_certificate_signer",
                Util.read_file_to_dict("inputs/add_allowed_item_certificate_signer.json.inp"),
                Util.read_file_to_dict("expected/add_allowed_item_certificate_signer.json.exp"),
            ],
        ]
    )
    def test_add_allowed_item(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_data",
                Util.read_file_to_dict("inputs/add_allowed_item_invalid.json.inp"),
                "Bad request.",
                "The API client sent a malformed request.",
            ],
            [
                "duplicated_item",
                Util.read_file_to_dict("inputs/add_allowed_item_duplicate.json.inp"),
                "Conflict.",
                (
                    "Request made conflicts with an existing resource. Please check the API documentation "
                    "or contact Support."
                ),
            ],
        ]
    )
    def test_add_allowed_item_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
