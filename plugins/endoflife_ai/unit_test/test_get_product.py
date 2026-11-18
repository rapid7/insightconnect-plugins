import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock

from insightconnect_plugin_runtime.exceptions import PluginException
from icon_endoflife_ai.actions.get_product import GetProduct
from icon_endoflife_ai.actions.get_product.schema import Input, Output

from util import default_connector, mocked_requests_request


class TestGetProduct(TestCase):
    def setUp(self) -> None:
        self.action = default_connector(GetProduct())

    @mock.patch("requests.request", side_effect=mocked_requests_request)
    def test_get_product(self, mock_request):
        results = self.action.run({Input.PRODUCT: "nodejs"})
        self.assertTrue(results[Output.FOUND])
        self.assertEqual("nodejs", results[Output.PRODUCT])
        self.assertEqual(4, results[Output.VERSION_COUNT])
        self.assertEqual("https://endoflife.ai/nodejs", results[Output.PRODUCT_URL])
        self.assertEqual(4, len(results[Output.VERSIONS]))
        first = results[Output.VERSIONS][0]
        for field in ("version", "status", "score", "band", "grade", "score_card_url", "eol_date_source"):
            self.assertIn(field, first)
        self.assertNotIn("product", first, "product-level fields are not repeated per row")
        self.assertNotIn("factors", first, "the nested factors object is flattened to cisa_kev_exposure")
        self.assertIn("cisa_kev_exposure", first)
        self.action.output.validate(results)

    @mock.patch("requests.request", side_effect=mocked_requests_request)
    def test_get_product_not_found(self, mock_request):
        results = self.action.run({Input.PRODUCT: "not-a-product"})
        self.assertEqual({Output.FOUND: False, Output.MESSAGE: 'Product "not-a-product" not found'}, results)
        self.action.output.validate(results)

    def test_get_product_requires_product(self):
        with self.assertRaises(PluginException):
            self.action.run({Input.PRODUCT: ""})
