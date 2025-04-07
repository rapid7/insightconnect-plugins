import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from komand_sentinelone.actions.blacklist_by_content_hash import BlacklistByContentHash
from komand_sentinelone.actions.blacklist_by_content_hash.schema import (
    BlacklistByContentHashOutput,
)
from util import Util
from parameterized import parameterized
from jsonschema import validate


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestBlacklistByContentHash(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(BlacklistByContentHash())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/blacklist_by_content_hash.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "invalid_hash",
                Util.read_file_to_dict("inputs/blacklist_by_content_hash_invalid.json.inp"),
                Util.read_file_to_dict("expected/unaffected.json.exp"),
            ],
        ]
    )
    def test_blacklist_by_content_hash(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(expected, actual)
        validate(actual, BlacklistByContentHashOutput.schema)
