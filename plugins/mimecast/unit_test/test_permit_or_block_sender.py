import os
import sys
from jsonschema import validate
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))
from komand_mimecast.actions import PermitOrBlockSender
from komand_mimecast.actions.permit_or_block_sender.schema import PermitOrBlockSenderOutput, PermitOrBlockSenderInput
from komand_mimecast.util.constants import BASIC_ASSISTANCE_MESSAGE, ERROR_CASES, VALIDATION_INVALID_EMAIL_ADDRESS_ERROR

from util import Util


@patch("requests.request", side_effect=Util.mocked_request)
class TestPermitOrBlockSender(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(PermitOrBlockSender())

    def test_permit_user(self, _mocked_request):
        input_data = Util.load_json("inputs/permit_or_block_sender.json.exp")
        validate(input_data, PermitOrBlockSenderInput.schema)
        actual = self.action.run(input_data)
        expect = Util.load_json("expected/permit_or_block_sender.json.exp")
        self.assertEqual(expect, actual)
        validate(actual, PermitOrBlockSenderOutput.schema)

    def test_block_user(self, _mocked_request):
        input_data = Util.load_json("inputs/block_sender.json.exp")
        validate(input_data, PermitOrBlockSenderInput.schema)
        actual = self.action.run(input_data)
        expect = Util.load_json("expected/block_sender.json.exp")
        self.assertEqual(expect, actual)
        validate(actual, PermitOrBlockSenderOutput.schema)

    def test_bad_email(self, _mock_request):
        with self.assertRaises(PluginException) as exception:
            self.action.run(Util.load_json("inputs/permit_or_block_sender_bad.json.exp"))
        self.assertEqual(exception.exception.cause, ERROR_CASES.get(VALIDATION_INVALID_EMAIL_ADDRESS_ERROR))
        self.assertEqual(exception.exception.assistance, BASIC_ASSISTANCE_MESSAGE)
