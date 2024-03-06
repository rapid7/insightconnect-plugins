import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_anomali_threatstream.actions.get_sandbox_report import GetSandboxReport
from util import Util
from unittest.mock import patch
from parameterized import parameterized


@patch("requests.Session.send", side_effect=Util.mock_request)
class TestGetSandboxReport(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetSandboxReport())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("inputs/get_sandbox_report_success.json.inp"),
                Util.read_file_to_dict("expected/get_sandbox_report_success.json.exp"),
            ],
        ]
    )
    def test_get_sandbox_report(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(expected, actual)
