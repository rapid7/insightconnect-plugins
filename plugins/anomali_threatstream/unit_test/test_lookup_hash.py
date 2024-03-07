import sys
import os

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from komand_anomali_threatstream.actions.lookup_hash import LookupHash
from util import Util
from unittest.mock import patch
from parameterized import parameterized


@patch("requests.Session.send", side_effect=Util.mock_request)
class TestLookupHash(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(LookupHash())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("inputs/lookup_hash_success.json.inp"),
                Util.read_file_to_dict("expected/lookup_hash_success.json.exp"),
            ],
        ]
    )
    def test_lookup_hash(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(expected, actual)
