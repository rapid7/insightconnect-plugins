import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_cloudflare.actions.getAccounts import GetAccounts
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mock_request)
class TestGetAccounts(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAccounts())

    @parameterized.expand(
        [
            [
                "success1",
                Util.read_file_to_dict("inputs/list_accounts1.json.inp"),
                Util.read_file_to_dict("expected/list_accounts.json.exp"),
            ],
            [
                "success2",
                Util.read_file_to_dict("inputs/list_accounts2.json.inp"),
                Util.read_file_to_dict("expected/list_accounts.json.exp"),
            ],
            [
                "not_found",
                Util.read_file_to_dict("inputs/list_accounts_empty.json.inp"),
                Util.read_file_to_dict("expected/list_accounts_empty.json.exp"),
            ],
        ]
    )
    def test_get_accounts(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
