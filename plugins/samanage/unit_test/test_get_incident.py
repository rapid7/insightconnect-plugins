import sys
import os
import json
import logging
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_samanage.connection.connection import Connection
from komand_samanage.actions.get_incident import GetIncident
from unit_test.util import Util, mock_request_200
from unittest.mock import patch
from parameterized import parameterized



@patch('komand_samanage.util.api.request', side_effect=mock_request_200)
class TestGetIncident(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(GetIncident())

    @parameterized.expand(Util.load_parameters("get_incident").get("parameters"))
    def test_get_incident(self, mock_request, incident_id, expected):

        actual = self.action.run({"incident_id": incident_id})
        self.assertEqual(actual, expected)
