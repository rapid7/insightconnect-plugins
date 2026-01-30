import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from insightconnect_plugin_runtime.exceptions import PluginException
from util import Util
from parameterized import parameterized
from icon_connectwise.actions.get_ticket_notes import GetTicketNotes


@patch("requests.request", side_effect=Util.mock_request)
class TestGetTicketNotes(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetTicketNotes())

    @parameterized.expand(
        [
            [
                "many_parameters",
                Util.read_file_to_dict("inputs/get_ticket_notes_many_parameters.json.inp"),
                Util.read_file_to_dict("expected/get_ticket_notes_many_parameters.json.exp"),
            ],
            [
                "few_parameters",
                Util.read_file_to_dict("inputs/get_ticket_notes_few_parameters.json.inp"),
                Util.read_file_to_dict("expected/get_ticket_notes_few_parameters.json.exp"),
            ],
        ]
    )
    def test_get_ticket_notes(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "ticket_not_found",
                Util.read_file_to_dict("inputs/get_ticket_notes_ticket_not_found.json.inp"),
                "Resource not found.",
                "Please verify inputs and if the issue persists, contact support.",
                Util.read_file_to_string("expected/ticket_not_found.json.exp"),
            ],
            [
                "invalid_conditions",
                Util.read_file_to_dict("inputs/get_ticket_notes_invalid_conditions.json.inp"),
                PluginException.causes[PluginException.Preset.BAD_REQUEST],
                PluginException.assistances[PluginException.Preset.BAD_REQUEST],
                Util.read_file_to_string("expected/get_ticket_notes_invalid_conditions.json.exp"),
            ],
        ]
    )
    def test_get_ticket_notes_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance, data):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)
