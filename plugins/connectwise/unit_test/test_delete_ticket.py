import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from insightconnect_plugin_runtime.exceptions import PluginException
from util import Util
from parameterized import parameterized
from icon_connectwise.actions.delete_ticket import DeleteTicket


@patch("requests.request", side_effect=Util.mock_request)
class TestDeleteTicket(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DeleteTicket())

    @parameterized.expand(
        [
            [
                "valid_id",
                Util.read_file_to_dict("inputs/delete_ticket.json.inp"),
                Util.read_file_to_dict("expected/delete_ticket.json.exp"),
            ]
        ]
    )
    def test_delete_ticket(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "ticket_not_found",
                Util.read_file_to_dict("inputs/create_ticket_note_ticket_not_found.json.inp"),
                "Resource not found.",
                "Please verify inputs and if the issue persists, contact support.",
                Util.read_file_to_string("expected/ticket_not_found.json.exp"),
            ]
        ]
    )
    def test_delete_ticket_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance, data):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)
