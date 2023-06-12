import os
import sys
from unittest import TestCase
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))

from komand_mimecast.actions import CreateBlockedSenderPolicy

from util import Util


@patch("requests.request", side_effect=Util.mocked_request)
class TestCreateBlockedSenderPolicy(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateBlockedSenderPolicy())

    def test_create_blocked_sender_policy(self, mocked_request):
        actual = self.action.run(Util.load_json("inputs/create_blocked_sender_policy.json.exp"))
        expect = Util.load_json("expected/create_blocked_sender_policy.json.exp")
        self.assertEqual(expect, actual)
