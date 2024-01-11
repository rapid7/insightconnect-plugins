import os
import sys
from jsonschema import validate
from unittest import TestCase
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))

from komand_mimecast.actions import CreateBlockedSenderPolicy
from komand_mimecast.actions.create_blocked_sender_policy.schema import (
    CreateBlockedSenderPolicyOutput,
    CreateBlockedSenderPolicyInput,
)
from util import Util


@patch("requests.request", side_effect=Util.mocked_request)
class TestCreateBlockedSenderPolicy(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateBlockedSenderPolicy())

    def test_create_blocked_sender_policy(self, _mocked_request):
        input_data = Util.load_json("inputs/create_blocked_sender_policy.json.exp")
        actual = self.action.run(input_data)
        validate(input_data, CreateBlockedSenderPolicyInput.schema)
        expect = Util.load_json("expected/create_blocked_sender_policy.json.exp")
        self.assertEqual(expect, actual)
        validate(actual, CreateBlockedSenderPolicyOutput.schema)
