import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

from util import Util
from parameterized import parameterized
from icon_zscaler.actions.update_urls_of_url_category import UpdateUrlsOfUrlCategory
from icon_zscaler.util.constants import Cause, Assistance


@patch("requests.request", side_effect=Util.mock_request)
class TestUpdateUrlsOfUrlCategory(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(UpdateUrlsOfUrlCategory())

    @parameterized.expand(
        [
            [
                "custom_add",
                Util.read_file_to_dict("inputs/update_urls_of_url_category_custom_add.json.inp"),
                Util.read_file_to_dict("expected/update_urls_of_url_category_custom_add.json.exp"),
            ],
            [
                "predefined_add",
                Util.read_file_to_dict("inputs/update_urls_of_url_category_predefined_add.json.inp"),
                Util.read_file_to_dict("expected/update_urls_of_url_category_predefined_add.json.exp"),
            ],
            [
                "custom_remove",
                Util.read_file_to_dict("inputs/update_urls_of_url_category_custom_remove.json.inp"),
                Util.read_file_to_dict("expected/update_urls_of_url_category_custom_remove.json.exp"),
            ],
        ]
    )
    def test_update_urls_of_url_category(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "category_not_found",
                Util.read_file_to_dict("inputs/update_urls_of_url_category_not_found.json.inp"),
                Cause.CATEGORY_NOT_FOUND,
                Assistance.VERIFY_INPUT,
            ],
            [
                "invalid_url_list",
                Util.read_file_to_dict("inputs/update_urls_of_url_category_invalid_url_list.json.inp"),
                Cause.INVALID_DETAILS,
                Assistance.VERIFY_INPUT,
            ],
            [
                "empty_url_list_1",
                Util.read_file_to_dict("inputs/update_urls_of_url_category_empty_url_list_1.json.inp"),
                Cause.URL_LIST_NOT_PROVIDED,
                Assistance.VERIFY_INPUT,
            ],
            [
                "empty_url_list_2",
                Util.read_file_to_dict("inputs/update_urls_of_url_category_empty_url_list_2.json.inp"),
                Cause.URL_LIST_NOT_PROVIDED,
                Assistance.VERIFY_INPUT,
            ],
        ]
    )
    def test_update_urls_of_url_category_raise_exception(
        self, mock_request, test_name, input_parameters, cause, assistance
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
