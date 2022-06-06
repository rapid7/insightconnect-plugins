import logging
import sys
import os
from unittest import TestCase, mock

sys.path.append(os.path.abspath("../"))

from icon_azure_ad_admin.connection.connection import Connection
from icon_azure_ad_admin.actions.get_user_info import GetUserInfo


class MockRequest:
    def __init__(self):
        self.status_code = 200

    def json(self):
        return {
            "accountEnabled": True,
            "mobilePhone": None,
            "manager": {
                "@odata.type": "#microsoft.graph.user",
                "city": None,
                "companyName": None,
            },
        }


class TestGetUserInfo(TestCase):
    @mock.patch("icon_azure_ad_admin.util.get_user_info", return_value={"some": "some"})
    def setUp(self, mock_connection) -> None:
        self.connection = mock.create_autospec(Connection())
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.tenant = "tenant_id"

        self.action = GetUserInfo()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action loger")

        self.app_id = "application_id"
        self.app_secret = {"application_secret": {"secretKey": "secret_key"}}
        self.params = {"user_id": "user@example.com"}

    @mock.patch("requests.get", return_value=MockRequest())
    def test_get_user_info(self, mocked):
        response = self.action.run(self.params)
        expected_response = {
            "user_information": {
                "accountEnabled": True,
                "manager": {
                    "@odata.type": "#microsoft.graph.user",
                },
            }
        }

        self.assertEqual(response, expected_response)
