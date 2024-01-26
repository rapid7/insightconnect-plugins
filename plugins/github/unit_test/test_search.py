import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from komand_github.actions.search.action import Search
from komand_github.actions.search.schema import SearchInput, SearchOutput
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from jsonschema import validate
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("komand_github.connection.connection.github.Auth.Token", side_effect=Util.mock_github_auth_token)
@patch("komand_github.connection.connection.github.Github", side_effect=Util.mock_github)
@patch("requests.get", side_effect=Util.mock_get_request)
class TestSearch(TestCase):
    @classmethod
    @patch("komand_github.connection.connection.github.Auth.Token", side_effect=Util.mock_github_auth_token)
    @patch("komand_github.connection.connection.github.Github", side_effect=Util.mock_github)
    def setUpClass(cls, _mock_github: MagicMock, _mock_github_auth_token: MagicMock) -> None:
        cls.action = Util.default_connector(Search())

    @parameterized.expand(
        [
            [
                "valid_search",
                {"search_type": "Issues", "query": "repo:integrationalliance/Test_new_repo test"},
                Util.read_file_to_dict("expected/search_valid.json.exp"),
            ],
        ]
    )
    def test_search_valid(
        self,
        _mock_request: MagicMock,
        _mock_github: MagicMock,
        _mock_github_auth_token: MagicMock,
        _test_name: str,
        input_params: dict,
        expected: dict,
    ):
        validate(input_params, SearchInput.schema)
        actual = self.action.run(input_params)

        self.assertDictEqual(actual, expected)
        validate(actual, SearchOutput.schema)

    @parameterized.expand(
        [
            [
                "invalid_search_500",
                {"search_type": "Issues", "query": "repo:integrationalliance/Test_new_repo test"},
                {"credentials": {"username": "usename", "personal_token": {"secretKey": "error_500"}}},
                "A status code of 500 was returned from Github",
                "Please check that the provided inputs are correct and try again.",
                "",
            ],
            [
                "invalid_search",
                {"search_type": "Issues", "query": "repo:integrationalliance/Test_new_repo test"},
                {"credentials": {"username": "usename", "personal_token": {"secretKey": "error_bad_json"}}},
                "Error occoured when trying to perfom a search",
                "Please check that the provided inputs are correct and try again.",
                "Expecting value: line 1 column 1 (char 0)",
            ],
        ]
    )
    def test_search_invalid(
        self,
        _mock_request: MagicMock,
        _mock_github: MagicMock,
        _mock_github_auth_token: MagicMock,
        _test_name: str,
        input_params: dict,
        input_connection: dict,
        cause: str,
        assistance: str,
        data: list,
    ):
        validate(input_params, SearchInput.schema)
        with self.assertRaises(PluginException) as error:
            Util.default_connector(Search(), input_connection).run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)
