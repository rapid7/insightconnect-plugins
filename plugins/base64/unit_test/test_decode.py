import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from komand_base64.actions.decode import Decode
from komand_base64.actions.decode.schema import Input, Output

STUB_INPUT_PARAMS = {
    Input.BASE64: "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cgo=",
    Input.ERRORS: "nothing",
}


class TestDecode(TestCase):
    def setUp(self) -> None:
        self.action = Decode()

    def test_decode(self):
        response = self.action.run(STUB_INPUT_PARAMS)
        expected = "Rapid7 InsightConnect\n\n"
        self.assertEqual(expected, response.get(Output.DATA))
