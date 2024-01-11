import os
import sys
from jsonschema import validate
from unittest import TestCase
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))

from komand_mimecast.actions import DecodeUrl
from komand_mimecast.actions.decode_url.schema import DecodeUrlOutput, DecodeUrlInput

from util import Util


@patch("requests.request", side_effect=Util.mocked_request)
class TestDecodeURL(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DecodeUrl())

    def test_decode_url(self, _mocked_request):
        input_data = Util.load_json("inputs/decode_url.json.exp")
        validate(input_data, DecodeUrlInput.schema)
        actual = self.action.run(input_data)
        expect = Util.load_json("expected/decode_url.json.exp")
        self.assertEqual(expect, actual)
        validate(actual, DecodeUrlOutput.schema)
