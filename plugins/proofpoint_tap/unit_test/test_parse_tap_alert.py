import os
import sys
from unittest import TestCase
from unittest.mock import patch

from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from komand_proofpoint_tap.actions import ParseTapAlert
from test_util import Util


class TestParseTapAlert(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ParseTapAlert())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/parse_tap_alert_success.json.inp"),
                Util.read_file_to_dict("expected/parse_tap_alert_success.json.exp"),
            ],
            [
                "success_empty",
                Util.read_file_to_dict("inputs/parse_tap_alert_success_empty.json.inp"),
                Util.read_file_to_dict("expected/parse_tap_alert_success_empty.json.exp"),
            ],
        ]
    )
    @patch("urlextract.urlextract_core.URLExtract.__new__")
    def test_parse_tap_alert(self, _test_name, input_params, expected, mock_url_extract):
        # GH actions fails on finding a cachefile for URLExtract and has no impact on this unit test mock it.
        mock_url_extract.return_value = MockURLExtract()

        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)


class MockURLExtract:
    def __init__(self):
        pass

    @staticmethod
    def find_urls(_input):
        return []
