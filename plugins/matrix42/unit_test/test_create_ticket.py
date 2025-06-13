import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_matrix42.actions.create_ticket import CreateTicket
from util import Util


@patch("requests.post", side_effect=Util.mocked_requests)
class TestCreateTicket(TestCase):
    def test_create_ticket_success(self, mock_post):
        action = Util.default_connection(CreateTicket())
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
