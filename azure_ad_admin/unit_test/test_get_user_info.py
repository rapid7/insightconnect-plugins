import logging
from unittest import TestCase

from icon_azure_ad_admin.actions import GetUserInfo
from icon_azure_ad_admin.connection import Connection

import json


class TestGetUserInfo(TestCase):
    def test_get_user_info(self):
        log = logging.getLogger("TestLogger")

        test_connection = Connection()
        test_get_user_info = GetUserInfo()

        test_connection.logger = log
        test_get_user_info.logger = log

        with open("../tests/get_user_info.json") as file:
            data = json.load(file)
            connection_params = data.get("body").get("connection")

        action_params = {
            "user_id": "user@example.com"
        }

        test_connection.connect(connection_params)
        test_get_user_info.connection = test_connection

        result = test_get_user_info.run(action_params)
        expected = {'user_information': {'@odata.context': 'https://graph.microsoft.com/v1.0/$metadata#users/$entity',
                                         'businessPhones': [], 'displayName': 'Joey McAdams', 'givenName': 'Joey',
                                         'jobTitle': 'Sr. Software Engineer', 'mail': '', 'mobilePhone': '',
                                         'officeLocation': '', 'preferredLanguage': '', 'surname': 'McAdams',
                                         'userPrincipalName': 'user@example.com',
                                         'id': '08290005-23ba-46b4-a377-b381d651a2fb', 'accountEnabled': True}}
        self.assertEqual(result, expected)
