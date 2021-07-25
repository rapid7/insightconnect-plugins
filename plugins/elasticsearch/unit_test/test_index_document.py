import sys
import os
from unittest.mock import patch
from komand_elasticsearch.actions import IndexDocument
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_elasticsearch.actions.index_document.schema import Input
from unit_test.util import Util
from unittest import TestCase

sys.path.append(os.path.abspath("../"))


class TestIndexDocument(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(IndexDocument())

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_index_document_without_id(self, mock_request):
        actual = self.action.run({Input.INDEX: "test-index"})
        expected = {
            "index_response": {
                "_id": "VWx5O3oBrBTgS4Hhf6Hp",
                "_index": "test-index",
                "_primary_term": 1,
                "_seq_no": 0,
                "_shards": {"failed": 0, "successful": 1, "total": 2},
                "_type": "_doc",
                "_version": 1,
                "result": "created",
            }
        }
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_index_document_with_id(self, mock_request):
        actual = self.action.run({Input.INDEX: "test-index2", Input.ID: "VWx5O3oBrBTgS4Hhf6Hp"})
        expected = {
            "index_response": {
                "_id": "Vmx6O3oBrBTgS4HhWKFJ",
                "_index": "test-index",
                "_primary_term": 1,
                "_seq_no": 2,
                "_shards": {"failed": 0, "successful": 2, "total": 2},
                "_type": "_doc",
                "_version": 2,
                "result": "updated",
            }
        }
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_index_document_with_empty_response(self, mock_request):
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.INDEX: "empty", Input.ID: "VWx5O3oBrBTgS4Hhf6Hp"})

        self.assertEqual(error.exception.cause, "Document was not indexed. ")
        self.assertEqual(error.exception.assistance, "Please check provided data and try again.")
