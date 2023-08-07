import os
import sys
from unittest import TestCase

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
    def test_parse_tap_alert(self, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)
