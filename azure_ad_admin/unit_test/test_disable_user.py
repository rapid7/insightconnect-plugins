import os
import sys
from unittest import TestCase

working_path = os.getcwd()
sys.path.insert(0, "../")

from icon_azure_ad_admin.actions import DisableUserAccount
from icon_azure_ad_admin.actions import EnableUserAccount
from icon_azure_ad_admin.connection import Connection
import logging
import json


class TestDisableUser(TestCase):

    def test_admin_actions(self):
        log = logging.getLogger("TestLogger")

        test_connection = Connection()
        test_disable = DisableUserAccount()
        test_enable = EnableUserAccount()

        test_connection.logger = log
        test_disable.logger = log
        test_enable.logger = log

        with open("../tests/get_user_info.json") as file:
            data = json.load(file)
            connection_params = data.get("body").get("connection")

        action_params = {
            "user_id": "jmcadams@komanddev.onmicrosoft.com"
        }

        test_connection.connect(connection_params)
        test_disable.connection = test_connection
        test_enable.connection = test_connection

        success = test_disable.run(action_params)
        self.assertTrue(success)

        success = test_enable.run(action_params)
        self.assertTrue(success)

        pass
