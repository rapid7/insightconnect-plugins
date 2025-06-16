import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_matrix42.actions.create_ticket import CreateTicket
from icon_matrix42.actions.create_ticket.schema import Input
from util import Util
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.post", side_effect=Util.mocked_requests)
class TestCreateTicket(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connection(CreateTicket())

    @parameterized.expand(Util.load_parameters("create_service_request_ticket").get("parameters"))
    def test_create_service_request_ticket_success(
        self, mock_request, activity_type, subject, description_html, additional_fields
    ):

        result = self.action.run(
            {
                Input.ACTIVITY_TYPE: activity_type,
                Input.SUBJECT: subject,
                Input.DESCRIPTION_HTML: description_html,
                Input.ADDITIONAL_FIELDS: additional_fields,
            }
        )

        self.assertEqual(result["id"], "3db8e0a1-1d53-f011-1887-000d3aed261c2")

        args, kwargs = mock_request.call_args

        # Check the URL called
        self.assertEqual(kwargs["url"], "https://fake-url/ticket/create?activityType=6")

        # Check the headers sent in the request
        expected_headers = {
            "Authorization": f"Bearer {self.action.connection.access_token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        self.assertEqual(kwargs["headers"], expected_headers)

        # Check the JSON body sent in the request
        expected_body = {
            "User": "00000000-0000-1337-0000-000000000000",
            "Category": "00000000-0000-1337-0000-000000000000",
            "Subject": "Unit Test Ticket",
            "DescriptionHTML": "<h1>Unit Test</h1>",
        }
        self.assertEqual(kwargs["json"], expected_body)

    @parameterized.expand(Util.load_parameters("create_service_request_ticket_bad").get("parameters"))
    def test_create_service_request_ticket_bad(
        self, mock_request, activity_type, subject, description_html, additional_fields, cause, assistance, data
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(
                {
                    Input.ACTIVITY_TYPE: activity_type,
                    Input.SUBJECT: subject,
                    Input.DESCRIPTION_HTML: description_html,
                    Input.ADDITIONAL_FIELDS: additional_fields,
                }
            )

        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)
