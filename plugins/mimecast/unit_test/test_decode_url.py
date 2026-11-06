import os
import sys
from jsonschema import validate
from unittest import TestCase
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))

from komand_mimecast.actions import DecodeUrl
from komand_mimecast.actions.decode_url.schema import DecodeUrlOutput, DecodeUrlInput

from util import EXPIRED_ACCESS_TOKEN, Util


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

    def test_decode_url_token_expired(self, mocked_request):
        # The stored token is expired so the action re-authenticates and retries the call
        self.action.connection.client.access_token = EXPIRED_ACCESS_TOKEN
        actual = self.action.run(Util.load_json("inputs/decode_url.json.exp"))
        self.assertEqual(Util.load_json("expected/decode_url.json.exp"), actual)
        self.assertEqual(mocked_request.call_count, 3)
        validate(actual, DecodeUrlOutput.schema)
