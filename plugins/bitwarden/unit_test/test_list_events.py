import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_bitwarden.actions.listEvents import ListEvents
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mock_request)
class TestListEvents(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListEvents())

    @parameterized.expand(
        [
            [
                "success1",
                Util.read_file_to_dict("inputs/list_events1.json.inp"),
                Util.read_file_to_dict("expected/list_events1.json.exp"),
            ],
            [
                "success2",
                Util.read_file_to_dict("inputs/list_events2.json.inp"),
                Util.read_file_to_dict("expected/list_events2.json.exp"),
            ],
            [
                "success3",
                Util.read_file_to_dict("inputs/list_events3.json.inp"),
                Util.read_file_to_dict("expected/list_events3.json.exp"),
            ],
            [
                "success4",
                Util.read_file_to_dict("inputs/list_events4.json.inp"),
                Util.read_file_to_dict("expected/list_events1.json.exp"),
            ],
            [
                "events_not_found",
                Util.read_file_to_dict("inputs/list_events_empty.json.inp"),
                Util.read_file_to_dict("expected/list_events_empty.json.exp"),
            ],
        ]
    )
    def test_list_events(self, mock_request, test_name, inputs, expected):
        actual = self.action.run(inputs)
        self.assertEqual(actual, expected)
