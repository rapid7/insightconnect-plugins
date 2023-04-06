import sys
import os

from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized

from unit_test.util import Util
from icon_sophos_central.actions.get_blocked_items import GetBlockedItems

sys.path.append(os.path.abspath("../"))


@patch("requests.request", side_effect=Util.mock_request)
class TestGetBlockedItems(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.action = Util.default_connector(GetBlockedItems())

    @parameterized.expand(
        [
            [
                "default_params",
                Util.read_file_to_dict("inputs/get_blocked_items.json.inp"),
                Util.read_file_to_dict("expected/get_blocked_items.json.exp"),
            ],
            [
                "no_params",
                Util.read_file_to_dict("inputs/get_blocked_items_no_params.json.inp"),
                Util.read_file_to_dict("expected/get_blocked_items_no_params.json.exp"),
            ],
        ]
    )
    def test_get_blocked_items(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
