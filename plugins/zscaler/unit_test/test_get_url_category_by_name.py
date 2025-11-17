import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

from unit_test.util import Util
from parameterized import parameterized
from icon_zscaler.actions.get_url_category_by_name import GetUrlCategoryByName
from icon_zscaler.util.constants import Cause, Assistance


@patch("requests.request", side_effect=Util.mock_request)
class TestGetUrlCategoryByName(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetUrlCategoryByName())

    @parameterized.expand(
        [
            [
                "custom",
                Util.read_file_to_dict("inputs/get_url_category_by_name_custom.json.inp"),
                Util.read_file_to_dict("expected/get_url_category_by_name_custom.json.exp"),
            ],
            [
                "predefined",
                Util.read_file_to_dict("inputs/get_url_category_by_name_predefined.json.inp"),
                Util.read_file_to_dict("expected/get_url_category_by_name_predefined.json.exp"),
            ],
        ]
    )
    def test_get_url_category_by_name(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "not_found",
                Util.read_file_to_dict("inputs/get_url_category_by_name_not_found.json.inp"),
                Cause.CATEGORY_NOT_FOUND,
                Assistance.VERIFY_INPUT,
            ],
        ]
    )
    def test_get_url_category_by_name_raise_exception(
        self, mock_request, test_name, input_parameters, cause, assistance
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
