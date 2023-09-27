import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_microsoft_intune.actions.search_devices import SearchDevices
from util import Util
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mocked_requests)
class TestSearchDevices(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mocked_requests)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(SearchDevices())

    @parameterized.expand(
        [
            [
                "by_id",
                Util.read_file_to_dict("inputs/search_devices_by_id.json.inp"),
                Util.read_file_to_dict("expected/search_devices_by_id.json.exp"),
            ],
            [
                "by_name",
                Util.read_file_to_dict("inputs/search_devices_by_name.json.inp"),
                Util.read_file_to_dict("expected/search_devices_by_id.json.exp"),
            ],
            [
                "by_email",
                Util.read_file_to_dict("inputs/search_devices_by_email_address.json.inp"),
                Util.read_file_to_dict("expected/search_devices_by_id.json.exp"),
            ],
            [
                "by_user_principal_name",
                Util.read_file_to_dict("inputs/search_devices_by_user_principal_name.json.inp"),
                Util.read_file_to_dict("expected/search_devices_by_id.json.exp"),
            ],
            [
                "empty",
                Util.read_file_to_dict("inputs/search_devices_empty.json.inp"),
                Util.read_file_to_dict("expected/search_devices_empty.json.exp"),
            ],
        ]
    )
    def test_search_devices(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
