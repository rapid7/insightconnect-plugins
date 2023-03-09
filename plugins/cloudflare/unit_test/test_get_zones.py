import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_cloudflare.actions.getZones import GetZones
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mock_request)
class TestGetZones(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetZones())

    @parameterized.expand(
        [
            [
                "all",
                Util.read_file_to_dict("inputs/get_zones_all.json.inp"),
                Util.read_file_to_dict("expected/get_zones_all.json.exp"),
            ],
            [
                "by_name",
                Util.read_file_to_dict("inputs/get_zones_by_name.json.inp"),
                Util.read_file_to_dict("expected/get_zones_by_name.json.exp"),
            ],
            [
                "empty",
                Util.read_file_to_dict("inputs/get_zones_empty.json.inp"),
                Util.read_file_to_dict("expected/get_zones_empty.json.exp"),
            ],
        ]
    )
    def test_get_zones(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
