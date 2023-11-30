import sys
import os
import json

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_abnormal_security.connection.connection import Connection
from icon_abnormal_security.actions.get_threat_details import GetThreatDetails
from icon_abnormal_security.actions.get_threat_details.schema import Input, Output
from util import Util
from unittest.mock import patch


class TestGetThreatDetails(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetThreatDetails())

    @patch("requests.request", side_effect=Util.mocked_requests)
    def test_get_threat_details(self, mock_post):
        actual = self.action.run({Input.THREAT_ID: "184712ab-6d8b-47b3-89d3-a314efef79e2"})
        expected = json.loads(
            Util.read_file_to_string(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), "payloads/get_threat_details.json.exp")
            )
        )
        self.assertEqual(actual, expected)
