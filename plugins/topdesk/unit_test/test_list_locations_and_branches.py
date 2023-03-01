import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unit_test.util import Util
from parameterized import parameterized
from icon_topdesk.actions.listLocationsAndBranches import ListLocationsAndBranches
from icon_topdesk.util.constants import Cause, Assistance


@patch("requests.request", side_effect=Util.mock_request)
class TestListLocationsAndBranches(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListLocationsAndBranches())

    @parameterized.expand(
        [
            [
                "found",
                Util.read_file_to_dict("inputs/list_locations_and_branches_found.json.inp"),
                Util.read_file_to_dict("expected/list_locations_and_branches_found.json.exp"),
            ],
            [
                "not_found",
                Util.read_file_to_dict("inputs/list_locations_and_branches_not_found.json.inp"),
                Util.read_file_to_dict("expected/list_locations_and_branches_not_found.json.exp"),
            ],
        ]
    )
    def test_list_locations_and_branches(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_query",
                Util.read_file_to_dict("inputs/list_locations_and_branches_invalid_query.json.inp"),
                Cause.INVALID_REQUEST,
                Assistance.VERIFY_INPUT,
            ]
        ]
    )
    def test_list_locations_and_branches_raise_exception(
        self, mock_request, test_name, input_parameters, cause, assistance
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
