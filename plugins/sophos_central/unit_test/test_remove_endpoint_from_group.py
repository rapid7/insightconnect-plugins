import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_sophos_central.actions.remove_endpoint_from_group import RemoveEndpointFromGroup
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mock_request)
class TestRemoveEndpointFromGroup(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(RemoveEndpointFromGroup())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/remove_endpoint_from_group.json.inp"),
                Util.read_file_to_dict("expected/remove_endpoint_from_group.json.exp"),
            ],
            [
                "invalid_endpoint",
                Util.read_file_to_dict("inputs/remove_endpoint_from_group_invalid_endpoint.json.inp"),
                Util.read_file_to_dict("expected/remove_endpoint_from_group_endpoint_not_found.json.exp"),
            ],
        ]
    )
    def test_remove_endpoint_from_group(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "endpoint_group_not_found",
                Util.read_file_to_dict("inputs/remove_endpoint_from_group_invalid_group.json.inp"),
                "Not found.",
                "The requested resource wasn't found. The resource ID provided may be invalid, or the resource may have been deleted, or is no longer addressable.",
            ]
        ]
    )
    def test_remove_endpoint_from_group_bad(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
