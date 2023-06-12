import os
import sys
from unittest import TestCase
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))

from komand_mimecast.actions import DecodeUrl

from util import Util


@patch("requests.request", side_effect=Util.mocked_request)
class TestDecodeURL(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DecodeUrl())

    def test_decode_url(self, mocked_request):
        actual = self.action.run(Util.load_json("inputs/decode_url.json.exp"))
        expect = Util.load_json("expected/decode_url.json.exp")
        self.assertEqual(expect, actual)
