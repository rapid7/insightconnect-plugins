import logging
from unittest import TestCase

from icon_azure_ad_admin.actions import GetGroupByName
from icon_azure_ad_admin.connection import Connection

import json


class TestGetGroupByName(TestCase):
    def test_get_group_by_name(self):
        log = logging.getLogger("TestLogger")

        test_connection = Connection()
        test_get_group_by_name = GetGroupByName()

        test_connection.logger = log
        test_get_group_by_name.logger = log

        with open("../tests/get_user_info.json") as file:
            data = json.load(file)
            connection_params = data.get("body").get("connection")

        action_params = {
            "name": "Dream Team"
        }

        test_connection.connect(connection_params)
        test_get_group_by_name.connection = test_connection

        result = test_get_group_by_name.run(action_params)
        expected = {'group': {'id': 'd2cc6aa2-8071-44d9-a97a-0a758da420a8', 'createdDateTime': '2018-07-13T17:46:51Z', 'creationOptions': ['Team', 'ExchangeProvisioningFlags:3552'], 'description': 'Komand test for plugin', 'displayName': 'Dream Team', 'groupTypes': ['Unified'], 'mail': 'DreamTeam@komanddev.onmicrosoft.com', 'mailEnabled': True, 'mailNickname': 'DreamTeam', 'proxyAddresses': ['SPO:SPO_5f0de1c4-0f19-4eab-9ede-00c06c2dab4b@SPO_5c824599-dc8c-4d31-96fb-3b886d4f8f10', 'SMTP:DreamTeam@komanddev.onmicrosoft.com'], 'renewedDateTime': '2018-07-13T17:46:51Z', 'resourceBehaviorOptions': ['HideGroupInOutlook', 'SubscribeMembersToCalendarEventsDisabled', 'WelcomeEmailDisabled'], 'resourceProvisioningOptions': ['Team'], 'securityEnabled': False, 'visibility': 'Public', 'onPremisesProvisioningErrors': []}}
        self.assertEqual(result, expected)
        self.assertEqual(result.get("group").get("displayName"), "Dream Team")
