import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_sophos_central.actions.add_endpoint_group import AddEndpointGroup
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mock_request)
class TestAddEndpointGroup(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(AddEndpointGroup())

    @parameterized.expand(
        [
            [
                "without_endpoints",
                Util.read_file_to_dict("inputs/add_endpoint_group.json.inp"),
                Util.read_file_to_dict("expected/endpoint_group.json.exp"),
            ],
            [
                "with_endpoint",
                Util.read_file_to_dict("inputs/add_endpoint_group2.json.inp"),
                Util.read_file_to_dict("expected/endpoint_group2.json.exp"),
            ],
        ]
    )
    def test_add_endpoint_group(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "endpoint_not_found",
                Util.read_file_to_dict("inputs/add_endpoint_group_with_invalid_endpoint.json.inp"),
                "Not found.",
                "The requested resource wasn't found. The resource ID provided may be invalid, or the resource may have been deleted, or is no longer addressable.",
            ]
        ]
    )
    def test_add_endpoint_group_bad(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
