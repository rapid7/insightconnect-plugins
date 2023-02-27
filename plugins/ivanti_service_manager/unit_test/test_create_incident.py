import sys
import os
import json

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from unit_test.util import Util
from unit_test.mock import mock_request
from icon_ivanti_service_manager.actions.create_incident.schema import Input
from icon_ivanti_service_manager.actions.create_incident import CreateIncident
from insightconnect_plugin_runtime.exceptions import PluginException


class TestCreateIncident(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.params = {
            "assignee": "identifier",
            "category": "category",
            "customer": "identifier",
            "customer_not_unique": "identifier_not_unique",
            "no_customer": "no_identifier",
            "description": "description",
            "impact": "impact",
            "source": "source",
            "status": "status",
            "summary": "summary",
            "type": "type",
            "urgency": "urgency",
        }

    def setUp(self) -> None:
        self.action = Util.default_connector(CreateIncident())
        self.connection = self.action.connection

    @patch("requests.Session.request", side_effect=mock_request)
    def test_create_incident_success(self, _mock_req):
        actual = self.action.run(
            {
                Input.ASSIGNEE: self.params.get("assignee"),
                Input.CATEGORY: self.params.get("category"),
                Input.CUSTOMER: self.params.get("customer"),
                Input.DESCRIPTION: self.params.get("description"),
                Input.IMPACT: self.params.get("impact"),
                Input.SOURCE: self.params.get("source"),
                Input.STATUS: self.params.get("status"),
                Input.SUMMARY: self.params.get("summary"),
                Input.TYPE: self.params.get("type"),
                Input.URGENCY: self.params.get("urgency"),
            }
        )
        expected = json.loads(
            Util.read_file_to_string(
                os.path.join(
                    os.path.dirname(os.path.realpath(__file__)), f"payloads/expected_create_incident_good.json.resp"
                )
            )
        )
        self.assertEqual(actual, expected)

    @patch("requests.Session.request", side_effect=mock_request)
    def test_create_incident_not_unique_customer(self, _mock_req):
        with self.assertRaises(PluginException) as exception:
            self.action.run(
                {
                    Input.ASSIGNEE: self.params.get("assignee"),
                    Input.CATEGORY: self.params.get("category"),
                    Input.CUSTOMER: self.params.get("customer_not_unique"),
                    Input.DESCRIPTION: self.params.get("description"),
                    Input.IMPACT: self.params.get("impact"),
                    Input.SOURCE: self.params.get("source"),
                    Input.STATUS: self.params.get("status"),
                    Input.SUMMARY: self.params.get("summary"),
                    Input.TYPE: self.params.get("type"),
                    Input.URGENCY: self.params.get("urgency"),
                }
            )
        cause = "Multiple employees found."
        self.assertEqual(exception.exception.cause, cause)

    @patch("requests.Session.request", side_effect=mock_request)
    def test_create_incident_no_customer(self, _mock_req):
        with self.assertRaises(PluginException) as exception:
            self.action.run(
                {
                    Input.ASSIGNEE: self.params.get("assignee"),
                    Input.CATEGORY: self.params.get("category"),
                    Input.CUSTOMER: self.params.get("no_customer"),
                    Input.DESCRIPTION: self.params.get("description"),
                    Input.IMPACT: self.params.get("impact"),
                    Input.SOURCE: self.params.get("source"),
                    Input.STATUS: self.params.get("status"),
                    Input.SUMMARY: self.params.get("summary"),
                    Input.TYPE: self.params.get("type"),
                    Input.URGENCY: self.params.get("urgency"),
                }
            )
        cause = "No employees found."
        self.assertEqual(exception.exception.cause, cause)
