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
            "total": {"value": 2, "relation": "eq"},
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

    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(SearchDocuments())

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_search_documents(self, mock_request):
        actual = self.action.run(
            {Input.INDEX: "search", Input.QUERY: {"query": {"match_all": {}}}, Input.ROUTING: None}
        )
        self.assertEqual(actual, self.expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_search_documents_without_route(self, mock_request):
        actual = self.action.run(
            {Input.INDEX: "search-without-route", Input.QUERY: {"query": {"match_all": {}}}, Input.ROUTING: None}
        )
        self.assertEqual(actual, self.expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_search_documents_empty(self, mock_request):
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.INDEX: "empty", Input.QUERY: {"query": {"match_all": {}}}, Input.ROUTING: None})

        self.assertEqual(error.exception.cause, "Document search not run. ")
        self.assertEqual(error.exception.assistance, "Please check provided data and try again.")
