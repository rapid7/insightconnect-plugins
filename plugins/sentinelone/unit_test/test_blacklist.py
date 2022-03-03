import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from komand_sentinelone.actions.blacklist import Blacklist
from komand_sentinelone.actions.blacklist.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util
from unittest import TestCase


class TestBlacklist(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(Blacklist())

    def test_should_fail_when_wrong_api_version(self):
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.HASH: "wrong_hash"})

        self.assertEqual("An invalid hash was provided.", error.exception.cause)
        self.assertEqual("Please enter a SHA1 hash and try again.", error.exception.assistance)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_should_success_when_blacklist(self, mock_request):
        expected = {"success": True}
        actual = self.action.run({Input.HASH: "3395856ce81f2b7382dee72602f798b642f14140", Input.BLACKLIST_STATE: True})
        self.assertEqual(expected, actual)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_should_success_when_unblacklist(self, mock_request):
        expected = {"success": True}
        actual = self.action.run({Input.HASH: "3395856ce81f2b7382dee72602f798b642f14140", Input.BLACKLIST_STATE: False})
        self.assertEqual(expected, actual)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_should_success_when_blacklist_and_description(self, mock_request):
        expected = {"success": True}
        actual = self.action.run(
            {
                Input.HASH: "3395856ce81f2b7382dee72602f798b642f14140",
                Input.BLACKLIST_STATE: True,
                Input.DESCRIPTION: "Description",
            }
        )
        self.assertEqual(expected, actual)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_should_success_when_unblacklist_and_description(self, mock_request):
        expected = {"success": True}
        actual = self.action.run(
            {
                Input.HASH: "3395856ce81f2b7382dee72602f798b642f14140",
                Input.BLACKLIST_STATE: False,
                Input.DESCRIPTION: "Description",
            }
        )
        self.assertEqual(expected, actual)
