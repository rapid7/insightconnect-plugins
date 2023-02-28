import sys
import os
import json

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_ivanti_service_manager.actions.create_service_request import CreateServiceRequest
from icon_ivanti_service_manager.actions.create_service_request.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util
from unit_test.mock import mock_request


class TestCreateServiceRequest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.params = {
            "customer": "identifier",
            "description": "description",
            "service_request_template": "identifier",
            "service_request_template_not_unique": "identifier_not_unique",
            "service_request_template_none": "no_identifier",
            "status": "status",
            "urgency": "urgency",
        }

    def setUp(self) -> None:
        self.action = Util.default_connector(CreateServiceRequest())
        self.connection = self.action.connection

    @patch("requests.Session.request", side_effect=mock_request)
    def test_create_service_request_success(self, _mock_req):
        actual = self.action.run(
            {
                Input.CUSTOMER: self.params.get("customer"),
                Input.DESCRIPTION: self.params.get("description"),
                Input.SERVICE_REQUEST_TEMPLATE: self.params.get("service_request_template"),
                Input.STATUS: self.params.get("status"),
                Input.URGENCY: self.params.get("urgency"),
            }
        )
        expected = json.loads(
            Util.read_file_to_string(
                os.path.join(
                    os.path.dirname(os.path.realpath(__file__)), f"payloads/expected_create_service_request.json.resp"
                )
            )
        )
        self.assertEqual(actual, expected)

    @patch("requests.Session.request", side_effect=mock_request)
    def test_create_service_request_multiple_templates(self, _mock_req):
        with self.assertRaises(PluginException) as exception:
            self.action.run(
                {
                    Input.CUSTOMER: self.params.get("customer"),
                    Input.DESCRIPTION: self.params.get("description"),
                    Input.SERVICE_REQUEST_TEMPLATE: self.params.get("service_request_template_not_unique"),
                    Input.STATUS: self.params.get("status"),
                    Input.URGENCY: self.params.get("urgency"),
                }
            )
            cause = "Multiple service request templates found."
            self.assertEqual(exception.exception.cause, cause)

    @patch("requests.Session.request", side_effect=mock_request)
    def test_create_service_request_no_templates(self, _mock_req):
        with self.assertRaises(PluginException) as exception:
            self.action.run(
                {
                    Input.CUSTOMER: self.params.get("customer"),
                    Input.DESCRIPTION: self.params.get("description"),
                    Input.SERVICE_REQUEST_TEMPLATE: self.params.get("service_request_template_none"),
                    Input.STATUS: self.params.get("status"),
                    Input.URGENCY: self.params.get("urgency"),
                }
            )
            cause = "No service request templates found."
            self.assertEqual(exception.exception.cause, cause)
