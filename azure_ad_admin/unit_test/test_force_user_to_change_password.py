import logging
from unittest import TestCase

from icon_azure_ad_admin.actions import ForceUserToChangePassword
from icon_azure_ad_admin.connection import Connection

import json


class TestForceUserToChangePassword(TestCase):
    def test_force_user_to_change_password(self):
        log = logging.getLogger("TestLogger")

        test_connection = Connection()
        test_force_user = ForceUserToChangePassword()

        test_connection.logger = log
        test_force_user.logger = log

        # Read in tests file and get connection params
        with open("../tests/get_user_info.json") as file:
            data = json.load(file)
            connection_params = data.get("body").get("connection")

        action_params = {
            "user_id": "user@example.com"
        }

        test_connection.connect(connection_params)
        test_force_user.connection = test_connection

        result = test_force_user.run(action_params)
        expected = {'success': True}
        self.assertEqual(result, expected)
