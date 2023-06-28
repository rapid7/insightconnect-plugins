import sys
import os
from unittest import TestCase
from unittest.mock import patch
from komand_proofpoint_tap.actions.url_decode import UrlDecode
from komand_proofpoint_tap.actions.url_decode.schema import Input, Output
from test_util import Util
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestUrlDecode(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(UrlDecode())

    @parameterized.expand(
        [
            [
                "single_url",
                Util.read_file_to_dict("inputs/url_decode_single_url.json.inp"),
                Util.read_file_to_dict("expected/url_decode_single_url.json.exp"),
            ],
            [
                "few_urls",
                Util.read_file_to_dict("inputs/url_decode_few_urls.json.inp"),
                Util.read_file_to_dict("expected/url_decode_few_urls.json.exp"),
            ],
            [
                "invalid_url",
                Util.read_file_to_dict("inputs/url_decode_invalid_url.json.inp"),
                Util.read_file_to_dict("expected/url_decode_invalid_url.json.exp"),
            ],
        ]
    )
    def test_url_decode(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)
