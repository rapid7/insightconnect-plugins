import unittest.mock
import unittest

from icon_aws_ec2.connection import Connection


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
