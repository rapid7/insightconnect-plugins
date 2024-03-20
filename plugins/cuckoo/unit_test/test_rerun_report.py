import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_cuckoo.actions.rerun_report import RerunReport
from komand_cuckoo.actions.vpn_status.schema import VpnStatusOutput
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from jsonschema import validate


class TestRerunReport(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(RerunReport())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("input/rerun_report_success.json.inp"),
                Util.read_file_to_dict("expected/rerun_report_success.json.exp"),
            ],
        ]
    )
    @patch("requests.request", side_effect=Util.mock_request)
    def test_rerun_report(self, test_name, input, expected, mock_request):
        actual = self.action.run(input)
        self.assertEqual(expected, actual)
        validate(actual, VpnStatusOutput.schema)
