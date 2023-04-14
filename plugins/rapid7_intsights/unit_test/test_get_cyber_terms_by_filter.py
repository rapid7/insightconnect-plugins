import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from unit_test.util import Util
from parameterized import parameterized
from icon_rapid7_intsights.actions.get_cyber_terms_by_filter import GetCyberTermsByFilter


@patch("requests.request", side_effect=Util.mock_request)
class TestGetCyberTermsByFilter(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetCyberTermsByFilter())

    @parameterized.expand(
        [
            [
                "without_filters",
                Util.read_file_to_dict("inputs/get_cyber_terms_no_filters.json.inp"),
                Util.read_file_to_dict("expecteds/get_cyber_terms_no_filters.json.exp"),
            ],
            [
                "next_page",
                Util.read_file_to_dict("inputs/get_cyber_terms_next_page.json.inp"),
                Util.read_file_to_dict("expecteds/get_cyber_terms_next_page.json.exp"),
            ],
            [
                "time_range",
                Util.read_file_to_dict("inputs/get_cyber_terms_time_range.json.inp"),
                Util.read_file_to_dict("expecteds/get_cyber_terms_time_range.json.exp"),
            ],
            [
                "by_id",
                Util.read_file_to_dict("inputs/get_cyber_terms_by_id.json.inp"),
                Util.read_file_to_dict("expecteds/get_cyber_terms_by_filters.json.exp"),
            ],
            [
                "success",
                Util.read_file_to_dict("inputs/get_cyber_terms_by_filters.json.inp"),
                Util.read_file_to_dict("expecteds/get_cyber_terms_by_filters.json.exp"),
            ],
            [
                "invalid_name",
                Util.read_file_to_dict("inputs/get_cyber_terms_invalid_name.json.inp"),
                Util.read_file_to_dict("expecteds/get_cyber_terms_invalid_name.json.exp"),
            ],
        ]
    )
    def test_get_cyber_terms_by_filter(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
