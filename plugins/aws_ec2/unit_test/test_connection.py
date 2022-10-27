import unittest.mock
import unittest
import botocore.exceptions as be

from icon_aws_ec2.util.common import AWSAction, ActionHelper
from icon_aws_ec2.connection import Connection

from insightconnect_plugin_runtime.exceptions import PluginException


@unittest.mock.patch("botocore.session.Session", return_value=unittest.mock.Mock())
class TestConnection(unittest.TestCase):
    def test_connect(self, get_mock):
        params = {
            "aws_access_key_id": {"secretKey": "123"},
            "aws_secret_access_key": {"secretKey": "456"},
            "region": "us-east",
        }
        test_connection = Connection()
        test_connection.logger = unittest.mock.Mock()
        test_connection.connect(params)
        test_connection.logger.info.assert_called_once()
        get_mock.assert_called()

    def test_assume_role(self, get_mock):
        params = {
            "aws_access_key_id": {"secretKey": "123"},
            "aws_secret_access_key": {"secretKey": "456"},
            "region": "us-east",
            "role_arn": "test_role",
            "external_id": "test_id",
        }
        test_connection = Connection()
        test_connection.region = "us-east"
        test_connection.sts_client = unittest.mock.Mock()
        test_connection.sts_client.assume_role.return_value = {
            "Credentials": {"AccessKeyId": "123", "SecretAccessKey": "456", "SessionToken": "token"}
        }
        test_connection.logger = unittest.mock.Mock()
        test_connection.try_to_assume_role(params=params)
        test_connection.sts_client.assume_role.assert_called_once()
