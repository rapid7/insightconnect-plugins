import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock

from insightconnect_plugin_runtime.exceptions import PluginException
from icon_endoflife_ai.actions.check_batch import CheckBatch
from icon_endoflife_ai.actions.check_batch.schema import Input, Output

from util import default_connector, mocked_requests_request


class TestCheckBatch(TestCase):
    def setUp(self) -> None:
        self.action = default_connector(CheckBatch())

    @mock.patch("requests.request", side_effect=mocked_requests_request)
    def test_check_batch(self, mock_request):
        items = [
            {"product": "nodejs", "version": "20"},
            {"product": "postgresql", "version": "13"},
            {"product": "nodejs", "version": "99"},
            {"product": "not-a-product", "version": "1"},
        ]
        results = self.action.run({Input.ITEMS: items})
        self.assertEqual(4, results[Output.COUNT])
        self.assertEqual(2, results[Output.FOUND_COUNT])
        self.assertEqual(
            2, results[Output.EOL_COUNT], "Node.js 20 and PostgreSQL 13 are both past end of life in the fixture"
        )
        rows = results[Output.RESULTS]
        self.assertEqual(["nodejs", "postgresql", "nodejs", "not-a-product"], [r["product"] for r in rows])
        self.assertEqual([True, True, False, False], [r["found"] for r in rows])
        self.assertEqual("eol", rows[0]["status"])
        self.assertEqual(60, rows[0]["score"])
        self.assertEqual(0, rows[0]["cisa_kev_exposure"])
        self.assertEqual("Version not found", rows[2]["message"])
        self.assertEqual("99", rows[2]["version"])
        self.assertEqual("Product not found", rows[3]["message"])
        self.assertEqual("1", rows[3]["version"], "the submitted version is kept on an unknown product")
        self.assertEqual(1, mock_request.call_count, "four items fit in one batch call")
        self.action.output.validate(results)

    @mock.patch("requests.request", side_effect=mocked_requests_request)
    def test_check_batch_chunks_at_five(self, mock_request):
        items = [{"product": "nodejs", "version": "20"}] * 12
        results = self.action.run({Input.ITEMS: items})
        self.assertEqual(12, results[Output.COUNT])
        self.assertEqual(12, results[Output.FOUND_COUNT])
        self.assertEqual(3, mock_request.call_count, "12 items are sent as chunks of 5, 5 and 2")
        sizes = [len(call[1]["json"]["products"]) for call in mock_request.call_args_list]
        self.assertEqual([5, 5, 2], sizes)
        body = mock_request.call_args_list[0][1]["json"]
        self.assertEqual({"slug": "nodejs", "version": "20"}, body["products"][0])

    @mock.patch("requests.request", side_effect=mocked_requests_request)
    def test_check_batch_version_optional(self, mock_request):
        results = self.action.run({Input.ITEMS: [{"product": "NodeJS"}]})
        body = mock_request.call_args[1]["json"]
        self.assertEqual({"slug": "nodejs"}, body["products"][0], "slugs are lowercased and version is omitted")
        self.assertTrue(results[Output.RESULTS][0]["found"])
        self.assertEqual("NodeJS", results[Output.RESULTS][0]["product"], "the submitted spelling is kept")

    @mock.patch("requests.request", side_effect=mocked_requests_request)
    def test_check_batch_empty(self, mock_request):
        results = self.action.run({Input.ITEMS: []})
        self.assertEqual({Output.RESULTS: [], Output.COUNT: 0, Output.FOUND_COUNT: 0, Output.EOL_COUNT: 0}, results)
        self.assertEqual(0, mock_request.call_count)
        self.action.output.validate(results)

    def test_check_batch_rejects_item_without_product(self):
        with self.assertRaises(PluginException):
            self.action.run({Input.ITEMS: [{"version": "20"}]})
