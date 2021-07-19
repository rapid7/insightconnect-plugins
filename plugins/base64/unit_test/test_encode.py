from unittest import TestCase
from komand_base64.actions.encode import Encode
import logging


class TestEncode(TestCase):
    def test_encode(self):
        test_encoder = Encode()
        log = logging.getLogger("Test")
        test_encoder.logger = log

        input_params = {"content": "Rapid7"}

        results = test_encoder.run(input_params)
        self.assertEqual("UmFwaWQ3", results.get("data"))
