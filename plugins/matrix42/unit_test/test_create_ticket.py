import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_matrix42.actions.create_ticket import CreateTicket
from icon_matrix42.actions.create_ticket.schema import Input
from util import Util
from parameterized import parameterized


@patch("requests.post", side_effect=Util.mocked_requests)
class TestCreateTicket(TestCase):

    @parameterized.expand(Util.load_parameters("create_service_request_ticket").get("parameters"))
    def test_create_service_request_ticket_success(
        self, mock_request, activity_type, subject, description_html, additional_fields
    ):
        action = Util.default_connection(CreateTicket())

        result = action.run(
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
        self.assertEqual(
            kwargs["headers"],
            {
                "Authorization": f"Bearer {action.connection.access_token}",
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
        )

        # Check the JSON body sent in the request
        expected_body = {
            "User": "00000000-0000-1337-0000-000000000000",
            "Category": "00000000-0000-1337-0000-000000000000",
            "Subject": "Unit Test Ticket",
            "DescriptionHTML": "<h1>Unit Test</h1>",
        }
        self.assertEqual(kwargs["json"], expected_body)
