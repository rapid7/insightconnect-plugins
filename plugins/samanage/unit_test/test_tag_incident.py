import sys
import os
import json
import logging

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_samanage.connection.connection import Connection
from komand_samanage.actions.tag_incident import TagIncident
from unit_test.util import Util, mock_request_200
from unittest.mock import patch
from parameterized import parameterized


@patch("komand_samanage.util.api.request", side_effect=mock_request_200)
class TestTagIncident(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(TagIncident())

    @parameterized.expand(Util.load_parameters("tag_incident").get("parameters"))
    def test_assign_incident(self, mock_request, incident_id, tag, expected):
        actual = self.action.run({"incident_id": incident_id, "tags": tag})
        self.assertEqual(actual, expected)
