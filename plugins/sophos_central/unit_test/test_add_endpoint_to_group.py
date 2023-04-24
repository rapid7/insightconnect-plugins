import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_sophos_central.actions.add_endpoint_to_group import AddEndpointToGroup
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mock_request)
class TestAddEndpointToGroup(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(AddEndpointToGroup())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/add_endpoint_to_group.json.inp"),
                Util.read_file_to_dict("expected/add_endpoint_to_group.json.exp"),
            ]
        ]
    )
    def test_add_endpoint_to_group(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "endpoint_group_not_found",
                Util.read_file_to_dict("inputs/add_endpoint_to_group_invalid_group.json.inp"),
                "Not found.",
                "The requested resource wasn't found. The resource ID provided may be invalid, or the resource may have been deleted, or is no longer addressable.",
            ],
            [
                "invalid_endpoint_id",
                Util.read_file_to_dict("inputs/add_endpoint_to_group_invalid_endpoint_id.json.inp"),
                "Not found.",
                "The requested resource wasn't found. The resource ID provided may be invalid, or the resource may have been deleted, or is no longer addressable.",
            ],
        ]
    )
    def test_add_endpoint_to_group_bad(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
