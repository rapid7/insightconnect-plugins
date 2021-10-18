import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from unit_test.util import Util
from icon_servicenow.actions.get_attachments_for_an_incident import GetAttachmentsForAnIncident
from icon_servicenow.actions.get_attachments_for_an_incident.schema import Input


class TestGetAttachmentsForAnIncident(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAttachmentsForAnIncident())

    @patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
    def test_get_attachments_for_an_incident(self, mock_post):
        actual = self.action.run({Input.INCIDENT_ID: "3072d01d07a552f6d0ea83ef29c936be"})

        expected = {"incident_attachments": ["ImNtRndhV1EzWVhSMFlXTm9iV1Z1ZEhSbGN6ZzNOalF6TWpKMCI="]}
        self.assertEqual(actual, expected)

    @patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
    def test_get_attachments_for_an_incident_many(self, mock_post):
        actual = self.action.run({Input.INCIDENT_ID: "51e4a8abb1b66fc04ba11001955e7dcb"})

        expected = {
            "incident_attachments": [
                "ImNtRndhV1EzWVhSMFlXTm9iV1Z1ZEhSbGN6ZzNOalF6TWpKMCI=",
                "ImNtRndhV1EzWVhSMFlXTm9iV1Z1ZEhSbGN6ZzNOalF6TWpKMCI=",
            ]
        }
        self.assertEqual(actual, expected)

    @patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
    def test_get_attachments_for_an_incident_empty(self, mock_post):
        actual = self.action.run({Input.INCIDENT_ID: "c1565da4456c2df374793d471d6ae8dd"})

        expected = {"incident_attachments": []}
        self.assertEqual(actual, expected)
