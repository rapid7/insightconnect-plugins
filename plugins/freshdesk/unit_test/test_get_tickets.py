import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unit_test.util import Util
from parameterized import parameterized
from icon_freshdesk.actions.getTickets import GetTickets


@patch("requests.request", side_effect=Util.mock_request)
class TestGetTickets(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetTickets())

    @parameterized.expand(
        [
            [
                "many_parameters",
                Util.read_file_to_dict("inputs/get_tickets_many_parameters.json.inp"),
                Util.read_file_to_dict("expected/get_tickets_many_parameters.json.exp"),
            ],
            [
                "no_parameters",
                Util.read_file_to_dict("inputs/get_tickets_no_parameters.json.inp"),
                Util.read_file_to_dict("expected/get_tickets_no_parameters.json.exp"),
            ],
        ]
    )
    def test_get_tickets(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_requester",
                Util.read_file_to_dict("inputs/get_tickets_invalid_company_id.json.inp"),
                PluginException.causes[PluginException.Preset.BAD_REQUEST],
                PluginException.assistances[PluginException.Preset.BAD_REQUEST],
                Util.read_file_to_string("expected/get_tickets_invalid_company_id.json.exp"),
            ]
        ]
    )
    def test_get_tickets_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance, data):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)
