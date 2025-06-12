import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock
from icon_matrix42.actions.create_ticket import CreateTicket
from icon_matrix42.connection.connection import Connection


class TestCreateTicket(TestCase):
    @patch("requests.post")
    def test_create_ticket_success(self, mock_post):
        # Mock the access token retrieval
        connection = Connection()
        connection.api_url = "https://fake-url/"
        connection.api_key = "fake-key"
        connection.access_token = "mocked-access-token"
        connection.logger = MagicMock()

        # Mock the response from the ticket creation endpoint
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        # Mock response.text.strip() to return the ticket ID
        mock_response.text = '"3db8e0a1-1d53-f011-1887-000d3aed261c"'
        mock_response.json.return_value = {
            "body": {
                "log": "",
                "status": "ok",
                "meta": {},
                "output": {"id": "3db8e0a1-1d53-f011-1887-000d3aed261c"},
            },
            "version": "v1",
            "type": "action_event",
        }
        mock_post.return_value = mock_response

        # Prepare action and params
        action = CreateTicket()
        action.connection = connection
        params = {
            "activity_type": "Service Request",
            "subject": "Unit Test Ticket",
            "description_html": "<h1>Unit Test</h1>",
            "additional_fields": {
                "User": "00000000-0000-1337-0000-000000000000",
                "Category": "00000000-0000-1337-0000-000000000000",
            },
        }

        result = action.run(params)

        self.assertEqual(result["id"], "3db8e0a1-1d53-f011-1887-000d3aed261c")
        args, kwargs = mock_post.call_args

        # Check the URL called
        self.assertEqual(args[0], "https://fake-url/ticket/create?activityType=6")

        # Check the headers sent in the request
        self.assertEqual(
            kwargs["headers"],
            {
                "Authorization": f"Bearer {connection.access_token}",
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
