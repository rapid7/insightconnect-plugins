import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from komand_base64.actions.encode import Encode
from komand_base64.actions.encode.schema import Input, Output

STUB_INPUT_PARAMS = {Input.CONTENT: "Rapid7"}


class TestEncode(TestCase):
    def setUp(self) -> None:
        self.action = Encode()

    def test_encode(self) -> None:
        response = self.action.run(STUB_INPUT_PARAMS)
        expected = "UmFwaWQ3"
        self.assertEqual(expected, response.get(Output.DATA))
