import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_broadcom_symantec_endpoint_protection.actions.blacklist import Blacklist
from util import Util
from unittest.mock import patch
from parameterized import parameterized


class TestBlacklist(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mock_request)
    def setUpClass(
        cls,
        mock_request,
    ) -> None:
        cls.action = Util.default_connector(Blacklist())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("input/blacklist_success.json.inp"),
                Util.read_file_to_dict("expected/blacklist_success.json.exp"),
            ],
        ]
    )
    @patch("aiohttp.ClientSession.post", side_effect=Util.async_mock_request)
    def test_blacklist(self, test_name, input_params, expected, mock_request):
        actual = self.action.run(input_params)
        print(actual)
        self.assertEqual(expected, actual)
