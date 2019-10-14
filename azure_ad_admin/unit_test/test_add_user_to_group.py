import logging
from unittest import TestCase

from icon_azure_ad_admin.actions import AddUserToGroup
from icon_azure_ad_admin.connection import Connection

import json


class TestAddUserToGroup(TestCase):
    def test_get_add_user_to_group(self):
        log = logging.getLogger("TestLogger")

        test_connection = Connection()
        test_add_user_to_group = AddUserToGroup()

        test_connection.logger = log
        test_add_user_to_group.logger = log

        with open("../tests/get_user_info.json") as file:
            data = json.load(file)
            connection_params = data.get("body").get("connection")

        action_params = {
            "user_id": "jmcadams@komanddev.onmicrosoft.com",
            "group_name": "Azure AD Test Security Group"
        }

        test_connection.connect(connection_params)
        test_add_user_to_group.connection = test_connection

        result = test_add_user_to_group.run(action_params)
        expected = {'success': True}
        self.assertEqual(result, expected)
