import sys
import os
from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized

from insightconnect_plugin_runtime.exceptions import PluginException

from unit_test.util import Util
from icon_topdesk.actions.listSuppliers import ListSuppliers
from icon_topdesk.util.constants import Cause, Assistance

sys.path.append(os.path.abspath("../"))


@patch("requests.request", side_effect=Util.mock_request)
class TestListSuppliers(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListSuppliers())

    @parameterized.expand(
        [
            [
                "default_params",
                Util.read_file_to_dict("inputs/list_suppliers_default_params.json.inp"),
                Util.read_file_to_dict("expected/list_suppliers_10_items.json.exp"),
            ],
            [
                "2_items_per_page",
                Util.read_file_to_dict("inputs/list_suppliers_page_size_2.json.inp"),
                Util.read_file_to_dict("expected/list_suppliers_2_items.json.exp"),
            ],
            [
                "11_items_per_page",
                Util.read_file_to_dict("inputs/list_suppliers_page_size_11.json.inp"),
                Util.read_file_to_dict("expected/list_suppliers_11_items.json.exp"),
            ],
            [
                "query_name",
                Util.read_file_to_dict("inputs/list_suppliers_query_name.json.inp"),
                Util.read_file_to_dict("expected/list_suppliers_query_name.json.exp"),
            ],
            [
                "query_not_found",
                Util.read_file_to_dict("inputs/list_suppliers_query_not_found.json.inp"),
                Util.read_file_to_dict("expected/list_suppliers_query_not_found.json.exp"),
            ],
            [
                "query_first_line",
                Util.read_file_to_dict("inputs/list_suppliers_query_first_line.json.inp"),
                Util.read_file_to_dict("expected/list_suppliers_query_first_line.json.exp"),
            ],
            [
                "mix_query",
                Util.read_file_to_dict("inputs/list_suppliers_mix.json.inp"),
                Util.read_file_to_dict("expected/list_suppliers_mix.json.exp"),
            ],
        ]
    )
    def test_list_suppliers(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_query",
                Util.read_file_to_dict("inputs/list_suppliers_query_bad.json.inp"),
                Cause.INVALID_REQUEST,
                Assistance.VERIFY_INPUT,
            ],
            [
                "bad_page_size",
                Util.read_file_to_dict("inputs/list_suppliers_query_page_size_bad.json.inp"),
                Cause.INVALID_REQUEST,
                Assistance.VERIFY_INPUT,
            ],
        ]
    )
    def test_list_supplier_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
