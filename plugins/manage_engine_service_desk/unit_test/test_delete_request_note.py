import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unit_test.util import Util
from parameterized import parameterized
from icon_manage_engine_service_desk.actions.delete_request_note import DeleteRequestNote


@patch("requests.request", side_effect=Util.mock_request)
class TestDeleteRequestNote(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DeleteRequestNote())

    @parameterized.expand(
        [
            [
                "valid_parameters",
                Util.read_file_to_dict("inputs/delete_request_note.json.inp"),
                Util.read_file_to_dict("expected/delete_request_note.json.exp"),
            ]
        ]
    )
    def test_delete_request_note(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "request_not_found",
                Util.read_file_to_dict("inputs/delete_request_note_request_not_found.json.inp"),
                "Resource not found.",
                "Please verify inputs and if the issue persists, contact support.",
                Util.read_file_to_dict("expected/request_not_found.json.exp"),
            ],
            [
                "note_not_found",
                Util.read_file_to_dict("inputs/delete_request_note_note_not_found.json.inp"),
                "Resource not found.",
                "Please verify inputs and if the issue persists, contact support.",
                Util.read_file_to_dict("expected/note_not_found.json.exp"),
            ],
        ]
    )
    def test_delete_request_note_raise_exception(
        self, mock_request, test_name, input_parameters, cause, assistance, data
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, str(data))
