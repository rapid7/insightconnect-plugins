import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from komand_sentinelone.actions.activities_list import ActivitiesList
from util import Util
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestActivitiesList(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(ActivitiesList())

    @parameterized.expand(
        [
            [
                "all",
                Util.read_file_to_dict("inputs/activities_list_all.json.inp"),
                Util.read_file_to_dict("expected/activities_list_all.json.exp"),
            ],
            [
                "success",
                Util.read_file_to_dict("inputs/activities_list.json.inp"),
                Util.read_file_to_dict("expected/activities_list.json.exp"),
            ],
            [
                "success_2",
                Util.read_file_to_dict("inputs/activities_list_2.json.inp"),
                Util.read_file_to_dict("expected/activities_list.json.exp"),
            ],
            [
                "success_3",
                Util.read_file_to_dict("inputs/activities_list_3.json.inp"),
                Util.read_file_to_dict("expected/activities_list.json.exp"),
            ],
            [
                "count_only",
                Util.read_file_to_dict("inputs/activities_list_count_only.json.inp"),
                Util.read_file_to_dict("expected/activities_list_count_only.json.exp"),
            ],
            [
                "skip_count",
                Util.read_file_to_dict("inputs/activities_list_skip_count.json.inp"),
                Util.read_file_to_dict("expected/activities_list_skip_count.json.exp"),
            ],
            [
                "empty",
                Util.read_file_to_dict("inputs/activities_list_empty.json.inp"),
                Util.read_file_to_dict("expected/activities_list_empty.json.exp"),
            ],
        ]
    )
    def test_activities_list(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(expected, actual)
