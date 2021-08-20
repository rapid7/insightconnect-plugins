import sys
import os
from unittest import TestCase
from unittest.mock import patch
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_elasticsearch.actions.update_document import UpdateDocument
from komand_elasticsearch.actions.update_document.schema import Input, Output
from unit_test.util import Util

sys.path.append(os.path.abspath("../"))


class TestUpdateDocument(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(UpdateDocument())

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_update_document(self, mock_request):
        actual = self.action.run(
            {
                Input.INDEX: "update",
                Input.ID: "1",
                Input.SCRIPT: {
                    "source": "ctx._source.counter += params.count",
                    "lang": "painless",
                    "params": {"count": 4},
                },
            }
        )
        expected = {
            "update_response": {
                "_id": "1",
                "_index": "test-index",
                "_primary_term": 1,
                "_seq_no": 4,
                "_shards": {"failed": 0, "successful": 2, "total": 2},
                "_type": "_doc",
                "_version": 2,
                "result": "updated",
            }
        }
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_update_document_empty(self, mock_request):
        with self.assertRaises(PluginException) as error:
            self.action.run(
                {
                    Input.INDEX: "empty",
                    Input.ID: "1",
                    Input.SCRIPT: {
                        "source": "ctx._source.counter += params.count",
                        "lang": "painless",
                        "params": {"count": 4},
                    },
                }
            )

        self.assertEqual(error.exception.cause, "Document was not updated")
        self.assertEqual(error.exception.assistance, "Please check provided data and try again.")

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_update_document_error(self, mock_request):
        with self.assertRaises(PluginException) as error:
            self.action.run(
                {
                    Input.INDEX: "UpdateError",
                    Input.ID: "1",
                    Input.SCRIPT: {
                        "source": "ctx._source.counter += params.count",
                        "lang": "painless",
                        "params": {"count": 4},
                    },
                }
            )

        self.assertEqual(error.exception.cause, "Something unexpected occurred.")
        self.assertEqual(error.exception.assistance, "Check the logs and if the issue persists please contact support.")
