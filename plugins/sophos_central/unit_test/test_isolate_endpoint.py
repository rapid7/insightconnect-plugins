import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_sophos_central.actions.isolate_endpoint import IsolateEndpoint
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mock_request)
class TestIsolateEndpoint(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(IsolateEndpoint())

    @parameterized.expand(
        [
            [
                "enable_isolation",
                Util.read_file_to_dict("inputs/enable_isolation.json.inp"),
                Util.read_file_to_dict("expected/enable_isolation.json.exp"),
            ],
            [
                "disable_isolation",
                Util.read_file_to_dict("inputs/disable_isolation.json.inp"),
                Util.read_file_to_dict("expected/disable_isolation.json.exp"),
            ],
        ]
    )
    def test_isolate_endpoint(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_endpoint_id",
                Util.read_file_to_dict("inputs/enable_isolation_invalid_endpoint.json.inp"),
                "Not found.",
                "The requested resource wasn't found. The resource ID provided may be invalid, or the resource may have been deleted, or is no longer addressable.",
            ]
        ]
    )
    def test_isolate_endpoint_bad(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
