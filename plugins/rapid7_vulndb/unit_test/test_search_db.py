import sys
import os

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from komand_rapid7_vulndb.actions.search_db import SearchDb
from komand_rapid7_vulndb.actions.search_db.schema import Input
from unit_test.mock import (
    mock_request,
)


class TestSearchDb(TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.params = {
            "database": "3395856ce81f2b7382dee72602f798b642f14140-cve",
            "vulnerability_database": "Vulnerability Database",
            "metasploit_database": "Metasploit Modules",
            "search": "4416967df92g3c8493eff83513g819c753g23241-cve",
            "search_no_results": "5527178eg13h4d9514egg94624h921d864h34352-cve",
            "search_404": "3395856ce81f2b7382dee72602f798b642f14140-cve",
            "search_504": "6628289fh24g5e1625fhh15735i132e97i45463-cve",
        }
        self.params_list = [
            ("404", "3395856ce81f2b7382dee72602f798b642f14140-cve", "The requested resource could not be found."),
            ("504", "6628289fh24g5e1625fhh15735i132e97i45463-cve", "Server error occurred"),
        ]
        self.action = SearchDb()

    @patch("requests.get", side_effect=mock_request)
    def test_search_db(self, mock_req):
        actual = self.action.run({Input.SEARCH: self.params.get("search"), Input.DATABASE: self.params.get("database")})
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

    @patch("requests.get", side_effect=mock_request)
    def test_search_db_no_results(self, mock_req):
        actual = self.action.run(
            {Input.SEARCH: self.params.get("search_no_results"), Input.DATABASE: self.params.get("database")}
        )
        expected = {"results_found": False, "search_results": []}
        self.assertEqual(actual, expected)

    @patch("requests.get", side_effect=mock_request)
    def test_search_db_vulnerability_nexpose(self, mock_req):
        actual = self.action.run(
            {Input.SEARCH: self.params.get("search"), Input.DATABASE: self.params.get("vulnerability_database")}
        )
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

    @patch("requests.get", side_effect=mock_request)
    def test_search_db_metasploit(self, mock_req):
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
                    "solutions": None,
                }
            ],
        }
        self.assertEqual(actual, expected)

    @patch("requests.get", side_effect=mock_request)
    def test_get_content_error(self, mock_req):
        for error, identifier, expected in self.params_list:
            with self.assertRaises(PluginException) as exception:
                self.action.run({Input.SEARCH: identifier, Input.DATABASE: self.params.get("database")})
            self.assertEqual(exception.exception.cause, expected)
