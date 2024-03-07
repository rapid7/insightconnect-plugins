import sys
import os

sys.path.append(os.path.abspath("../"))

from komand_anomali_threatstream.actions.submit_file import SubmitFile
from unittest import TestCase
from util import Util
from unittest.mock import patch
from parameterized import parameterized


@patch("requests.Session.send", side_effect=Util.mock_request)
class TestSubmitFile(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(SubmitFile())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("inputs/submit_file_success.json.inp"),
                Util.read_file_to_dict("expected/submit_file_success.json.exp"),
            ],
        ]
    )
    def test_submit_file(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(expected, actual)
