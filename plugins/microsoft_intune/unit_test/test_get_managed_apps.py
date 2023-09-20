import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_microsoft_intune.actions.get_managed_apps import GetManagedApps
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mocked_requests)
class TestGetManagedApps(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mocked_requests)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(GetManagedApps())

    @parameterized.expand(
        [
            [
                "all",
                Util.read_file_to_dict("inputs/get_managed_apps.json.inp"),
                Util.read_file_to_dict("expected/get_managed_apps.json.exp"),
            ],
            [
                "by_id",
                Util.read_file_to_dict("inputs/get_managed_apps_by_id.json.inp"),
                Util.read_file_to_dict("expected/get_managed_apps_by_id.json.exp"),
            ],
            [
                "by_name",
                Util.read_file_to_dict("inputs/get_managed_apps_by_name.json.inp"),
                Util.read_file_to_dict("expected/get_managed_apps.json.exp"),
            ],
            [
                "empty",
                Util.read_file_to_dict("inputs/get_managed_apps_empty.json.inp"),
                Util.read_file_to_dict("expected/get_managed_apps_empty.json.exp"),
            ],
        ]
    )
    def test_get_managed_apps(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "not_found",
                Util.read_file_to_dict("inputs/get_managed_apps_invalid_id.json.inp"),
                "Resource not found.",
                "Please provide valid inputs and try again.",
            ]
        ]
    )
    def test_get_managed_apps_raise_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
