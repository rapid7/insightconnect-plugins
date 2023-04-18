import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_sophos_central.actions.get_endpoints_in_group import GetEndpointsInGroup
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mock_request)
class TestGetEndpointsInGroup(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetEndpointsInGroup())

    @parameterized.expand(
        [
            [
                "all_fields",
                Util.read_file_to_dict("inputs/get_endpoints_in_group.json.inp"),
                Util.read_file_to_dict("expected/get_endpoints_in_group.json.exp"),
            ],
            [
                "selected_fields",
                Util.read_file_to_dict("inputs/get_endpoints_in_group_selected_fields.json.inp"),
                Util.read_file_to_dict("expected/get_endpoints_in_group_selected_fields.json.exp"),
            ],
            [
                "sort_asc",
                Util.read_file_to_dict("inputs/get_endpoints_in_group_sort_asc.json.inp"),
                Util.read_file_to_dict("expected/get_endpoints_in_group_sort_asc.json.exp"),
            ],
            [
                "sort_desc",
                Util.read_file_to_dict("inputs/get_endpoints_in_group_sort_desc.json.inp"),
                Util.read_file_to_dict("expected/get_endpoints_in_group_sort_desc.json.exp"),
            ],
            [
                "next_page",
                Util.read_file_to_dict("inputs/get_endpoints_in_group_next_page.json.inp"),
                Util.read_file_to_dict("expected/get_endpoints_in_group_next_page.json.exp"),
            ],
            [
                "search_hostname",
                Util.read_file_to_dict("inputs/get_endpoints_in_group_search_hostname.json.inp"),
                Util.read_file_to_dict("expected/get_endpoints_in_group_search_hostname.json.exp"),
            ],
            [
                "search_os_name",
                Util.read_file_to_dict("inputs/get_endpoints_in_group_search_os_name.json.inp"),
                Util.read_file_to_dict("expected/get_endpoints_in_group_search_os_name.json.exp"),
            ],
            [
                "search_hostname_not_found",
                Util.read_file_to_dict("inputs/get_endpoints_in_group_search_empty.json.inp"),
                Util.read_file_to_dict("expected/get_endpoints_in_group_search_empty.json.exp"),
            ],
        ]
    )
    def test_get_endpoints_in_group(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
