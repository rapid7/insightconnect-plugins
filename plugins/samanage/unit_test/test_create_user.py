import json
import logging
import re
import string
import sys
import os

sys.path.append(os.path.abspath('../'))

import unittest
from unittest import TestCase, mock
#from unittest import TestCase, mock
#from unittest.mock import MagicMock
from komand_samanage.connection.connection import Connection
from komand_samanage.actions.create_user import CreateUser
from komand_samanage.util.api import SamanageAPI
from unit_test.mock import MockRequest

expected_response = {"user":
            {
                "id": 4245316,
                "name": "Test user",
                "disabled": False,
                "email": "user@example.com",
                "created_at": "2018-11-22T15:18:53.337-05:00",
                "phone": "123456",
                "mobile_phone": "0012345",
                "department": {"id": 133365, "name": "Marketing"},
                "role": {
                    "id": 461182,
                    "name": "Read Only",
                    "portal": False,
                    "show_my_tasks": False,
                },
                "salt": "fc136bca03c6361bf1e564e18d70cc421b1fc582",
                "group_ids": [4492546],
                "custom_fields_values": [],
                "avatar": {"type": "initials", "color": "#fa7911", "initials": "JS"},
                "mfa_enabled": False,
            }
        }

class TestCreateUser(TestCase):
    def setUp(self) -> None:
        print('In setup function')
        self.action = CreateUser()
        print('self.action is {} of type {}'.format(self.action, type(self.action)))
        self.connection = Connection()
        #self.connection.api = mock.create_autospec(SamanageAPI)
        #print('self.connection.api is {} of type {}'.format(self.connection.api, type(self.connection.api)))
        self.connection.region = "us-east"
        self.connection.auth_params = {
            "aws_access_key_id": "123",
            "aws_secret_access_key": "321",
        }
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")
        #self.params = {}
        self.params = {
            "phone": "12345",
            "mobile_phone": "1234567",
            "name": "ExampleUser",
            "token": {"secretKey": "Examplesecretkey"},
            "email": "example@user.com",
            "role": "Example role",
            "department": "Example department",

        }


        # # mock_komand_samanage_actions_create_user.return_value = MagicMock(status_code=200,response=json.dumps({'user': 'expected_response'}))
        # self.connection = mock.create_autospec(Connection())
        # self.connection.logger = logging.getLogger("connection logger")
        # self.connection.tenant = "tenant_id"
        #
        # self.action = CreateUser()
        # # self.action.connection = self.connection
        # self.action.connection = self.connection
        # self.action.logger = logging.getLogger("action loger")
        # self.action.connection.api = mock.create_autospec(SamanageAPI)
        #
        # # self.password = _pw_gen()
        # self.app_id = "application_id"
        # # self.app_secret = {"application_secret": {"secretKey": "secret_key"}}
        # self.params = {
        #     "phone": "12345",
        #     "mobile_phone": "1234567",
        #     "name": "ExampleUser",
        #     "token": {"secretKey": "Examplesecretkey"},
        #     "email": "example@user.com",
        #     "role": "Example role",
        #     "department": "Example department",
        #
        # }

    #@unittest.mock.patch("requests.request", return_value=unittest.mock.Mock())
    @unittest.mock.patch("komand_samanage.actions.create_user", return_value=unittest.mock.Mock())
    def test_create_user(self, mock):

        print("DLDEBUG before create user:")
        create_user = self.action.run(self.params)
        print("DLDEBUG create user:")
        print(create_user)
        #self.assertEqual(create_user, expected_response)
        mock.assert_called_once()
        # TODO CHECK Azure for other creation types e.g incident and see what way the assert is done


# @unittest.mock.patch(
#     "insightconnect_plugin_runtime.clients.aws_client.AWSAction.run", return_value=unittest.mock.Mock()
# )
# def test_authorize_security_group_egress(self, mock):
#     self.action.run(self.params)
#     mock.assert_called_once()


# import logging
# import sys
# import os
# import unittest
# from unittest import TestCase, mock
#
# from icon_aws_ec2.actions import AuthorizeSecurityGroupEgress
# from icon_aws_ec2.connection import Connection
#
# sys.path.append(os.path.abspath("../"))


# class TestAuthorizeSecurityGroupEgress(TestCase):
#     def setUp(self) -> None:
#         self.action = AuthorizeSecurityGroupEgress()
#         self.connection = Connection()
#         self.connection.region = "us-east"
#         self.connection.auth_params = {
#             "aws_access_key_id": "123",
#             "aws_secret_access_key": "321",
#         }
#         self.action.connection = self.connection
#         self.action.logger = logging.getLogger("action logger")
#         self.params = {}

    # @unittest.mock.patch(
    #     "insightconnect_plugin_runtime.clients.aws_client.AWSAction.run", return_value=unittest.mock.Mock()
    # )
    # def test_authorize_security_group_egress(self, mock):
    #     self.action.run(self.params)
    #     mock.assert_called_once()
