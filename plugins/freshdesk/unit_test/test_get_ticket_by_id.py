import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unit_test.util import Util
from parameterized import parameterized
from icon_freshdesk.actions.getTicketById import GetTicketById


@patch("requests.request", side_effect=Util.mock_request)
class TestGetTicketById(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetTicketById())

    @parameterized.expand(
        [
            [
                "valid_id",
                Util.read_file_to_dict("inputs/get_ticket_by_id.json.inp"),
                Util.read_file_to_dict("expected/get_ticket_by_id.json.exp"),
            ]
        ]
    )
    def test_get_ticket_by_id(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "ticket_not_found",
                Util.read_file_to_dict("inputs/get_ticket_by_id_ticket_not_found.json.inp"),
                "Resource not found.",
                "Please verify inputs and if the issue persists, contact support.",
            ]
        ]
    )
    def test_get_ticket_by_id_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
