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
from util import EXPIRED_ACCESS_TOKEN, Util


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

    def test_create_blocked_sender_policy_token_expired(self, mocked_request):
        # The stored token is expired so the action re-authenticates and retries the call
        self.action.connection.client.access_token = EXPIRED_ACCESS_TOKEN
        actual = self.action.run(Util.load_json("inputs/create_blocked_sender_policy.json.exp"))
        self.assertEqual(Util.load_json("expected/create_blocked_sender_policy.json.exp"), actual)
        self.assertEqual(mocked_request.call_count, 3)
        validate(actual, CreateBlockedSenderPolicyOutput.schema)
