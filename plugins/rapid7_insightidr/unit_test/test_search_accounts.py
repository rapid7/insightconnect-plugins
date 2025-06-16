import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_rapid7_insightidr.actions.search_accounts import SearchAccounts
from komand_rapid7_insightidr.actions.search_accounts.schema import Input, SearchAccountsInput, SearchAccountsOutput
from util import Util
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate


@patch("requests.Session.send", side_effect=Util.mocked_requests)
class TestSearchAccounts(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(SearchAccounts())

    @parameterized.expand(Util.load_parameters("search_accounts").get("parameters"))
    def test_search_accounts(
        self,
        mock_request: MagicMock,
        search: list,
        sort: list,
        size: int,
        index: int,
        expected: dict,
    ) -> None:
        test_input = {
            Input.SEARCH: search,
            Input.SORT: sort,
            Input.SIZE: size,
            Input.INDEX: index,
        }
        validate(test_input, SearchAccountsInput.schema)
        actual = self.action.run(test_input)
        self.assertEqual(actual, expected)
        validate(actual, SearchAccountsOutput.schema)
