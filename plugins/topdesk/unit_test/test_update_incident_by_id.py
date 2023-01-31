import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_topdesk.actions.updateIncidentById import UpdateIncidentById
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mock_request)
class TestUpdateIncidentById(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(UpdateIncidentById())

    @parameterized.expand(
        [
            [
                "success1",
                Util.read_file_to_dict("inputs/update_incident_by_id1.json.inp"),
                Util.read_file_to_dict("expected/update_incident1.json.exp"),
            ],
            [
                "success2",
                Util.read_file_to_dict("inputs/update_incident_by_id2.json.inp"),
                Util.read_file_to_dict("expected/update_incident2.json.exp"),
            ],
            [
                "success3",
                Util.read_file_to_dict("inputs/update_incident_by_id3.json.inp"),
                Util.read_file_to_dict("expected/update_incident3.json.exp"),
            ],
        ]
    )
    def test_update_incident_by_id(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "not_found",
                Util.read_file_to_dict("inputs/update_incident_by_id_not_found.json.inp"),
                "Resource not found.",
                "Please verify inputs and if the issue persists, contact support.",
            ],
            [
                "invalid_input",
                Util.read_file_to_dict("inputs/update_incident_by_id_invalid_input.json.inp"),
                "The parameters of the request were malformed.",
                "Please verify inputs and if the issue persists, contact support.",
            ],
        ]
    )
    def test_update_incident_by_id_bad(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
