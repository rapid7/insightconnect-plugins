import sys
import os

from unittest import TestCase
from unittest.mock import patch
from unit_test.util import Util
from icon_servicenow.actions.get_incident_attachment import GetIncidentAttachment
from icon_servicenow.actions.get_incident_attachment.schema import Input

sys.path.append(os.path.abspath("../"))


class TestGetIncidentAttachment(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetIncidentAttachment())

    @patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
    def test_manage_threat_remediate(self, mock_post):
        actual = self.action.run({Input.ATTACHMENT_ID: "b259f4062d9f78f9ffdd6efd05c492c7"})

        expected = {"attachment_contents": "ImNtRndhV1EzWVhSMFlXTm9iV1Z1ZEhSbGN6ZzNOalF6TWpKMCI="}
        self.assertEqual(actual, expected)
