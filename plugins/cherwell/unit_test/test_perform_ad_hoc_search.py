import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_cherwell.actions.perform_ad_hoc_search import PerformAdHocSearch
from komand_cherwell.actions.perform_ad_hoc_search.schema import PerformAdHocSearchOutput
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from jsonschema import validate


class TestPerformAdHocSearch(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(PerformAdHocSearch())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("input/perform_ad_hoc_search_success.json.inp"),
                Util.read_file_to_dict("expected/perform_ad_hoc_search_success.json.exp"),
            ],
        ]
    )
    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_file(self, test_name, input, expected, mock_request):
        actual = self.action.run(input)
        self.assertEqual(expected, actual)
        validate(actual, PerformAdHocSearchOutput.schema)