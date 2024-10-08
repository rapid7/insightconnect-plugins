import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_rapid7_vulndb.actions.search_db import SearchDb
from komand_rapid7_vulndb.actions.search_db.schema import Input, SearchDbInput, SearchDbOutput

from mock import mock_request


class TestSearchDb(TestCase):
    @classmethod
    def setUp(self) -> None:
        self.params = {
            "database": "3395856ce81f2b7382dee72602f798b642f14140-cve",
            "vulnerability_database": "Vulnerability Database",
            "metasploit_database": "Metasploit Modules",
            "search": "4416967df92g3c8493eff83513g819c753g23241-cve",
            "search_test": "testingStubIdentifier-cve",
            "search_no_results": "5527178eg13h4d9514egg94624h921d864h34352-cve",
            "search_404": "3395856ce81f2b7382dee72602f798b642f14140-cve",
            "search_504": "6628289fh24g5e1625fhh15735i132e97i45463-cve",
        }
        self.params_list = [
            (
                "404",
                "3395856ce81f2b7382dee72602f798b642f14140-cve",
                "Vulnerability Database",
                "The requested resource could not be found.",
            ),
            ("504", "6628289fh24g5e1625fhh15735i132e97i45463-cve", "Vulnerability Database", "Server error occurred"),
        ]
        self.action = SearchDb()

    @patch("requests.get", side_effect=mock_request)
    def test_search_db(self, mock_requests: MagicMock) -> None:
        input_searchdb = {
            Input.SEARCH: self.params.get("search_test"),
            Input.DATABASE: self.params.get("vulnerability_database"),
        }
        validate(input_searchdb, SearchDbInput.schema)
        actual = self.action.run(input_searchdb)
        expected = {
            "results_found": True,
            "search_results": [
                {
                    "identifier": "test_identifier_2",
                    "title": "test_title_2",
                    "published_at": "2022-01-01T00:00:00.000Z",
                    "link": "https://vdb-kasf1i23nr1kl2j4.rapid7.com/v1/content/test_identifier_2",
                    "solutions": "test_solution_3,test_solution_4",
                },
                {
                    "identifier": "test_identifier_3",
                    "title": "test_title_3",
                    "published_at": "2022-01-01T00:00:00.000Z",
                    "link": "https://vdb-kasf1i23nr1kl2j4.rapid7.com/v1/content/test_identifier_3",
                    "solutions": "test_solution_1,test_solution_2",
                },
            ],
        }
        self.assertEqual(actual, expected)
        validate(actual, SearchDbOutput.schema)
        mock_requests.assert_called()

    @patch("requests.get", side_effect=mock_request)
    def test_search_db_no_results(self, mock_requests: MagicMock) -> None:
        input_data = {
            Input.SEARCH: self.params.get("search_no_results"),
            Input.DATABASE: self.params.get("vulnerability_database"),
        }
        validate(input_data, SearchDbInput.schema)
        actual = self.action.run(input_data)
        expected = {"results_found": False, "search_results": []}
        self.assertEqual(actual, expected)
        validate(actual, SearchDbOutput.schema)
        mock_requests.assert_called()

    @patch("requests.get", side_effect=mock_request)
    def test_search_db_vulnerability_nexpose(self, mock_requests: MagicMock) -> None:
        input_data = {
            Input.SEARCH: self.params.get("search"),
            Input.DATABASE: self.params.get("vulnerability_database"),
        }
        actual = self.action.run(input_data)
        expected = {
            "results_found": True,
            "search_results": [
                {
                    "identifier": "test_identifier_6",
                    "title": "test_title_6",
                    "published_at": "2019-01-01T00:00:00.000Z",
                    "link": "https://vdb-kasf1i23nr1kl2j4.rapid7.com/v1/content/test_identifier_6",
                    "solutions": "test_solution_1,test_solution_2",
                }
            ],
        }
        self.assertEqual(actual, expected)
        validate(actual, SearchDbOutput.schema)
        mock_requests.assert_called()

    @patch("requests.get", side_effect=mock_request)
    def test_search_db_metasploit(self, mock_requests: MagicMock) -> None:
        actual = self.action.run(
            {Input.SEARCH: self.params.get("search"), Input.DATABASE: self.params.get("metasploit_database")}
        )
        expected = {
            "results_found": True,
            "search_results": [
                {
                    "identifier": "test_identifier_5",
                    "title": "test_title_5",
                    "published_at": "2018-01-01T00:00:00.000Z",
                    "link": "https://vdb-kasf1i23nr1kl2j4.rapid7.com/v1/content/test_identifier_5",
                }
            ],
        }
        self.assertEqual(actual, expected)
        validate(actual, SearchDbOutput.schema)
        mock_requests.assert_called()

    @patch("requests.get", side_effect=mock_request)
    def test_get_content_error(self, mock_requests: MagicMock) -> None:
        for error, identifier, db_type, expected in self.params_list:
            with self.assertRaises(PluginException) as exception:
                input_data = {Input.SEARCH: identifier, Input.DATABASE: db_type}
                validate(input_data, SearchDbInput.schema)
                self.action.run(input_data)
            self.assertEqual(exception.exception.cause, expected)
        mock_requests.assert_called()
