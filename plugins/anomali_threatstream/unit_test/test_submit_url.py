import sys
import os

sys.path.append(os.path.abspath("../"))

from komand_anomali_threatstream.actions.submit_url import SubmitUrl
from unittest import TestCase
from util import Util
from unittest.mock import patch
from parameterized import parameterized


@patch("requests.Session.send", side_effect=Util.mock_request)
class TestSubmitUrl(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(SubmitUrl())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("inputs/submit_url_success.json.inp"),
                Util.read_file_to_dict("expected/submit_url_success.json.exp"),
            ],
        ]
    )
    def test_submit_url(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(expected, actual)
