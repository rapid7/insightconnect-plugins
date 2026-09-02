import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized
from jsonschema.validators import validate

from insightconnect_plugin_runtime.exceptions import PluginException

from util import Util
from icon_sophos_central.actions.blacklist import Blacklist


@patch("requests.request", side_effect=Util.mock_request)
class TestBlacklist(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(Blacklist())

    @parameterized.expand(
        [
            [
                "blacklist_hash",
                Util.read_file_to_dict("inputs/blacklist.json.inp"),
                Util.read_file_to_dict("expected/blacklist.json.exp"),
            ],
            [
                "unblacklist_hash_found_on_second_page",
                Util.read_file_to_dict("inputs/unblacklist.json.inp"),
                Util.read_file_to_dict("expected/unblacklist.json.exp"),
            ],
        ]
    )
    def test_blacklist(self, mock_request, test_name: str, input_params: dict, expected: dict) -> None:
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
        validate(actual, self.action.output.schema)

    def test_unblacklist_requests_every_page_until_hash_is_found(self, mock_request) -> None:
        self.action.run(Util.read_file_to_dict("inputs/unblacklist.json.inp"))

        requested_pages = [
            (call.kwargs.get("params") or {}).get("page")
            for call in mock_request.call_args_list
            if (call.kwargs.get("params") or {}).get("page")
        ]
        self.assertEqual(requested_pages, [1, 2])

    @parameterized.expand(
        [
            [
                "hash_not_in_blacklist",
                Util.read_file_to_dict("inputs/unblacklist_not_found.json.inp"),
                "Unable to unblacklist a hash that is not in the blacklist.",
                "Please provide a hash that is already blacklisted.",
            ],
            [
                "invalid_hash",
                Util.read_file_to_dict("inputs/blacklist_invalid_hash.json.inp"),
                "An invalid hash was provided.",
                "Please enter a SHA256 hash and try again.",
            ],
        ]
    )
    def test_blacklist_raise_exception(
        self, mock_request, test_name: str, input_params: dict, cause: str, assistance: str
    ) -> None:
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)

        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
