import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock
from icon_gitlab.actions.get_user import GetUser
from icon_gitlab.actions.get_user.schema import Output, Input
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request


class TestGetUser(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(GetUser())
        self.params = {Input.ID: "123"}

    @patch("requests.request", side_effect=mock_request_200)
    def test_get_user(self, mock_get: MagicMock) -> None:
        mocked_request(mock_get)
        response = self.action.run(self.params)

        expected = {
            Output.USER: {
                "id": 20455089,
                "username": "baggelisp.keph",
                "name": "baggelisSP",
                "state": "active",
                "locked": False,
                "avatar_url": "https://secure.gravatar.com/avatar/ef525c89fc7ba9dc5f5cc287edb77d45763c427e14f9083e38a71fc048a3998e?s=80&d=identicon",
                "web_url": "https://gitlab.com/baggelisp.keph",
                "bio": "",
                "location": "",
                "public_email": None,
                "skype": "",
                "linkedin": "",
                "twitter": "",
                "discord": "",
                "website_url": "",
                "organization": "",
                "job_title": "",
                "pronouns": None,
                "bot": False,
                "work_information": None,
                "local_time": None,
            }
        }
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
