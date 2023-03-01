import sys
import os
import json
import logging

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_samanage.connection.connection import Connection
from komand_samanage.actions.change_incident_state import ChangeIncidentState
from unit_test.util import Util, mock_request_200
from unittest.mock import patch
from parameterized import parameterized


@patch("komand_samanage.util.api.request", side_effect=mock_request_200)
class TestChangeIncidentState(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(ChangeIncidentState())

    @parameterized.expand(Util.load_parameters("change_incident_state").get("parameters"))
    def test_change_incident_state(self, mock_request, incident_id, state, expected):
        actual = self.action.run({"incident_id": incident_id, "state": state})
        self.assertEqual(actual, expected)
