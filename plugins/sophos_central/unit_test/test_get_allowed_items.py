import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unit_test.util import Util
from parameterized import parameterized
from icon_sophos_central.actions.get_allowed_items.action import GetAllowedItems


@patch("requests.request", side_effect=Util.mock_request)
class TestGetAllowedItems(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAllowedItems())

    @parameterized.expand(
        [
            [
                "all",
                Util.read_file_to_dict("inputs/get_allowed_items_all.json.inp"),
                Util.read_file_to_dict("expected/get_allowed_items_all.json.exp"),
            ],
            [
                "with_page_total",
                Util.read_file_to_dict("inputs/get_allowed_items_with_page_total.json.inp"),
                Util.read_file_to_dict("expected/get_allowed_items_with_page_total.json.exp"),
            ],
        ]
    )
    def test_get_allowed_items(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
