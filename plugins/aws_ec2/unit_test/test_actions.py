import logging
import sys
import os
import unittest
from unittest import TestCase, mock

from icon_aws_ec2.actions import AuthorizeSecurityGroupEgress
from icon_aws_ec2.connection import Connection

sys.path.append(os.path.abspath("../"))


class TestAuthorizeSecurityGroupEgress(TestCase):
    def setUp(self) -> None:
        self.action = AuthorizeSecurityGroupEgress()
        self.connection = Connection()
        self.connection.region = "us-east"
        self.connection.auth_params = {
            "aws_access_key_id": "123",
            "aws_secret_access_key": "321",
        }
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")
        self.params = {}

    @unittest.mock.patch(
        "insightconnect_plugin_runtime.clients.aws_client.AWSAction.run", return_value=unittest.mock.Mock()
    )
    def test_authorize_security_group_egress(self, mock):
        self.action.run(self.params)
        mock.assert_called_once()
