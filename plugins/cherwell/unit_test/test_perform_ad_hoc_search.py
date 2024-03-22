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


@patch("requests.Session.send", side_effect=Util.mock_request)
class TestPerformAdHocSearch(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(PerformAdHocSearch())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("inputs/perform_ad_hoc_search_success.json.inp"),
                Util.read_file_to_dict("expected/perform_ad_hoc_search_success.json.exp"),
            ],
        ]
    )
    def test_perform_adhoc_search(self, mock_request, test_name, input, expected):
        actual = self.action.run(input)
        self.assertEqual(expected, actual)
        validate(actual, PerformAdHocSearchOutput.schema)
