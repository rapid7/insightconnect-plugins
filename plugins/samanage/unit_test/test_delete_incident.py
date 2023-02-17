import sys
import os
import json
import logging

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_samanage.connection.connection import Connection
from komand_samanage.actions.delete_incident import DeleteIncident
from unit_test.util import Util, mock_request_200
from unittest.mock import patch
from parameterized import parameterized


@patch("komand_samanage.util.api.request", side_effect=mock_request_200)
class TestDeleteIncident(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(DeleteIncident())

    @parameterized.expand(Util.load_parameters("delete_incident").get("parameters"))
    def test_delete_incident(self, mock_request, incident_id, expected):
        actual = self.action.run({"incident_id": incident_id})
        self.assertEqual(actual, expected)
