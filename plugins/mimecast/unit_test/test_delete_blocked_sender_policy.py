import os
import sys
from unittest import TestCase
from unittest.mock import patch, MagicMock

sys.path.append(os.path.abspath("../"))
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_mimecast.actions import DeleteBlockedSenderPolicy
from komand_mimecast.util.constants import BASIC_ASSISTANCE_MESSAGE, ERROR_CASES, MANAGED_URL_NOT_FOUND_ERROR

from unit_test.util import Util


@patch("requests.request", side_effect=Util.mocked_request)
class TestDeleteBlockedSenderPolicy(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DeleteBlockedSenderPolicy())

    def test_delete_blocked_sender_policy(self, mocked_request: MagicMock):
        actual = self.action.run(Util.load_json("inputs/delete_blocked_sender_policy.json.exp"))
        expect = Util.load_json("expected/delete_blocked_sender_policy.json.exp")
        self.assertEqual(expect, actual)

    def test_bad_delete_blocked_sender_policy(self, mocked_request: MagicMock):
        with self.assertRaises(PluginException) as exception:
            self.action.run(Util.load_json("inputs/delete_blocked_sender_policy_bad.json.exp"))
        self.assertEqual(exception.exception.cause, PluginException.causes[PluginException.Preset.NOT_FOUND])
        self.assertEqual(exception.exception.assistance, PluginException.assistances[PluginException.Preset.NOT_FOUND])
