import sys
import os

from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized

from insightconnect_plugin_runtime.exceptions import PluginException

from unit_test.util import Util
from icon_sophos_central.actions.remove_blocked_item import RemoveBlockedItem

sys.path.append(os.path.abspath("../"))


@patch("requests.request", side_effect=Util.mock_request)
class TestRemoveBlockedItem(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.action = Util.default_connector(RemoveBlockedItem())

    @parameterized.expand(
        [
            [
                "valid_id",
                Util.read_file_to_dict("inputs/remove_blocked_item.json.inp"),
                Util.read_file_to_dict("expected/remove_blocked_item.json.exp"),
            ],
        ]
    )
    def test_remove_blocked_item(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_id",
                Util.read_file_to_dict("inputs/remove_blocked_item_bad.json.inp"),
                "Bad request.",
                "The API client sent a malformed request.",
            ],
        ]
    )
    def test_remove_blocked_item_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
