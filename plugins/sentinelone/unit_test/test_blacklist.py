import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from komand_sentinelone.actions.blacklist import Blacklist
from util import Util
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestBlacklist(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(Blacklist())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/blacklist.json.inp"),
                Util.read_file_to_dict("expected/blacklist.json.exp"),
            ],
            [
                "already_blacklisted",
                Util.read_file_to_dict("inputs/blacklist_already_blacklisted.json.inp"),
                Util.read_file_to_dict("expected/blacklist_already_blacklisted.json.exp"),
            ],
            [
                "unblacklist",
                Util.read_file_to_dict("inputs/unblacklist.json.inp"),
                Util.read_file_to_dict("expected/unblacklist.json.exp"),
            ],
            [
                "unblacklist_not_exist",
                Util.read_file_to_dict("inputs/unblacklist_not_exist.json.inp"),
                Util.read_file_to_dict("expected/unblacklist_not_exist.json.exp"),
            ],
        ]
    )
    def test_blacklist(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            [
                "invalid_hash",
                Util.read_file_to_dict("inputs/blacklist_invalid_hash.json.inp"),
                "An invalid hash was provided.",
                "Please enter a SHA1 hash and try again.",
            ]
        ]
    )
    def test_blacklist_raise_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
