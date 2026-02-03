import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from insightconnect_plugin_runtime.exceptions import PluginException
from util import Util
from parameterized import parameterized
from icon_connectwise.actions.update_ticket_note import UpdateTicketNote


@patch("requests.request", side_effect=Util.mock_request)
class TestUpdateTicketNote(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(UpdateTicketNote())

    @parameterized.expand(
        [
            [
                "valid",
                Util.read_file_to_dict("inputs/update_ticket_note.json.inp"),
                Util.read_file_to_dict("expected/update_ticket_note.json.exp"),
            ]
        ]
    )
    def test_update_ticket_note(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "no_parameters",
                Util.read_file_to_dict("inputs/update_ticket_note_no_parameters.json.inp"),
                "Not enough input parameters were provided.",
                "Please provide at least one input parameter except Ticket ID and Note ID and try again. If the issue persists, please contact support.",
                "",
            ]
        ]
    )
    def test_update_ticket_note_raise_exception(
        self, mock_request, test_name, input_parameters, cause, assistance, data
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)
