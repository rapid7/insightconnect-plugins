import sys
import os
from unittest.mock import patch
from komand_elasticsearch.actions import SearchDocuments
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_elasticsearch.actions.search_documents.schema import Input, Output
from unit_test.util import Util
from unittest import TestCase

sys.path.append(os.path.abspath("../"))


class TestSearchDocuments(TestCase):
    expected = {
        Output.TOOK: 2,
        Output.TIMED_OUT: False,
        Output.SHARDS: {"total": 1, "successful": 1, "skipped": 0, "failed": 0},
        Output.HITS: {
            "total": {"value": 2},
            "max_score": 1.0,
            "hits": [
                {
                    "_index": "test-index",
                    "_type": "_doc",
                    "_id": "VWx5O3oBrBTgS4Hhf6Hp",
                    "_score": 1.0,
                    "_source": {"id": 1, "message": "Some message"},
                },
                {
                    "_index": "test-index",
                    "_type": "_doc",
                    "_id": "Vmx6O3oBrBTgS4HhWKFJ",
                    "_score": 1.0,
                    "_source": {"id": 1, "message": "Some message"},
                },
            ],
        },
    }

    expected_with_route = {
        Output.TOOK: 2,
        Output.TIMED_OUT: False,
        Output.SHARDS: {"total": 1, "successful": 1, "skipped": 0, "failed": 0},
        Output.HITS: {
            "total": {"value": 2},
            "max_score": 1.0,
            "hits": [
                {
                    "_index": "test-index",
                    "_type": "_doc",
                    "_id": "VWx5O3oBrBTgS4Hhf6Hp",
                    "_score": 1.0,
                    "_routing": "test-route",
                    "_source": {"id": 1, "message": "Some message"},
                },
            ],
        },
    }

    @classmethod
    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(SearchDocuments())

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_search_documents(self, mock_request):
        actual = self.action.run({Input.INDEX: "search", Input.QUERY: {"match_all": {}}, Input.ROUTING: None})
        self.assertEqual(actual, self.expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_search_documents_with_route(self, mock_request):
        actual = self.action.run(
            {Input.INDEX: "search-with-route", Input.QUERY: {"match_all": {}}, Input.ROUTING: "test-route"}
        )
        self.assertEqual(actual, self.expected_with_route)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_search_documents_without_route(self, mock_request):
        actual = self.action.run({Input.INDEX: "search-without-route", Input.QUERY: {"match_all": {}}})
        self.assertEqual(actual, self.expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_search_documents_with_route_none(self, mock_request):
        actual = self.action.run(
            {Input.INDEX: "search-without-route", Input.QUERY: {"match_all": {}}, Input.ROUTING: None}
        )
        self.assertEqual(actual, self.expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_search_documents_empty(self, mock_request):
        actual = self.action.run({Input.INDEX: "empty", Input.QUERY: {"match_all": {}}, Input.ROUTING: None})

        self.assertEqual(
            actual,
            {
                "hits": {"hits": [], "max_score": 0, "total": {"value": 0}},
                "shards": {},
                "timed_out": "false",
                "took": 0,
            },
        )

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_search_documents_wrong_object(self, mock_request):
        actual = self.action.run({Input.INDEX: "wrong_object", Input.QUERY: {"match_all": {}}, Input.ROUTING: None})

        self.assertEqual(
            {
                "hits": {
                    "hits": [{"_score": 0}, {".name": 1.0, "_score": 0, "name": 1}],
                    "max_score": 0,
                    "total": {"value": 0},
                },
                "shards": {},
                "timed_out": "false",
                "took": 0,
            },
            actual,
        )

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_index_document_with_empty_response(self, mock_request):
        with self.assertRaises(PluginException) as error:
            self.action.run(
                {Input.INDEX: "wrong_object", Input.QUERY: {"query": {"match_all": {}}}, Input.ROUTING: None}
            )

        self.assertEqual(error.exception.cause, "Wrong input query format")
        self.assertEqual(
            error.exception.assistance,
            "Old query style detected during input. The input shouldn't contain {'query': {'query': ...}}. "
            "Please refer to the help.md for more details or to the Elasticsearch API documentation: "
            "https://www.elastic.co/guide/en/elasticsearch/reference/current/query-filter-context.html#query-filter-context-ex",
        )
