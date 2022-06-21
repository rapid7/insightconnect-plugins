import unittest.mock
import unittest
import botocore.exceptions as be

from parameterized import parameterized

from icon_aws_ec2.util.common import AWSAction, ActionHelper
from icon_aws_ec2.connection import Connection
from icon_aws_ec2.actions.describe_instances.schema import DescribeInstancesInput, DescribeInstancesOutput

from insightconnect_plugin_runtime.exceptions import PluginException


def raise_attribiute_error(arg1, arg2):
    raise AttributeError()


class TestAwsAction(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_handle_rest_call(self):
        aws_action = AWSAction("NewAction", "Description", None, None, "ec2", "describe_instance")
        aws_action.connection = unittest.mock.create_autospec(Connection)
        aws_action.input = DescribeInstancesInput()
        aws_action.output = DescribeInstancesOutput()
        mock_call = unittest.mock.Mock()
        aws_action.handle_rest_call(mock_call, {})
        mock_call.assert_called_once()
        aws_action.connection.helper.format_input.assert_called_once()
        aws_action.connection.helper.format_output.assert_called_once()

    @staticmethod
    def mock_call_raise_endpoint_connection_error():
        raise be.EndpointConnectionError(**{"endpoint_url": "test_url"})

    def test_handle_rest_call_endpoint_connection_error(self):
        aws_action = AWSAction("NewAction", "Description", None, None, "ec2", "describe_instance")
        aws_action.connection = unittest.mock.create_autospec(Connection)
        aws_action.input = DescribeInstancesInput()
        aws_action.output = DescribeInstancesOutput()
        with self.assertRaises(PluginException):
            mock_call = TestAwsAction.mock_call_raise_endpoint_connection_error
            aws_action.handle_rest_call(mock_call, {})

    @staticmethod
    def mock_call_raise_param_validation_error():
        raise be.ParamValidationError(**{"endpoint_url": "test_url"})

    def test_handle_rest_call_param_validation_error(self):
        aws_action = AWSAction("NewAction", "Description", None, None, "ec2", "describe_instance")
        aws_action.connection = unittest.mock.create_autospec(Connection)
        aws_action.input = DescribeInstancesInput()
        aws_action.output = DescribeInstancesOutput()
        with self.assertRaises(PluginException):
            mock_call = TestAwsAction.mock_call_raise_param_validation_error
            aws_action.handle_rest_call(mock_call, {})

    @staticmethod
    def mock_call_raise_client_error():
        raise be.ClientError(**{"endpoint_url": "test_url"})

    def test_handle_rest_call_client_error(self):
        aws_action = AWSAction("NewAction", "Description", None, None, "ec2", "describe_instance")
        aws_action.connection = unittest.mock.create_autospec(Connection)
        aws_action.input = DescribeInstancesInput()
        aws_action.output = DescribeInstancesOutput()
        mock_call = TestAwsAction.mock_call_raise_client_error
        with self.assertRaises(PluginException):
            aws_action.handle_rest_call(mock_call, {})

    def mocked_requests_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code
                self.ok = True

        return MockResponse(None, 200)

    @unittest.mock.patch("requests.get", side_effect=mocked_requests_get)
    def test_test(self, mock_get):
        aws_action = AWSAction("NewAction", "Description", None, None, "ec2", "describe_instance")
        aws_action.connection = unittest.mock.create_autospec(Connection)
        aws_action.input = DescribeInstancesInput()
        aws_action.output = DescribeInstancesOutput()
        aws_action.connection.helper = unittest.mock.create_autospec(ActionHelper)
        aws_action.test()
        aws_action.connection.helper.format_output.assert_called_once()

    @unittest.mock.patch("icon_aws_ec2.util.common.getattr", side_effect=raise_attribiute_error)
    def test_run_attribute_error(self, arg1):
        aws_action = AWSAction("NewAction", "Description", None, None, "ec2", "describe_instance")
        aws_action.connection = unittest.mock.create_autospec(Connection)
        aws_action.input = DescribeInstancesInput()
        aws_action.output = DescribeInstancesOutput()
        with self.assertRaises(PluginException):
            aws_action.run()

    @unittest.mock.patch("icon_aws_ec2.util.common.getattr")
    def test_run_ok(self, arg1):
        aws_action = AWSAction("NewAction", "Description", None, None, "ec2", "describe_instance")
        aws_action.connection = unittest.mock.create_autospec(Connection)
        aws_action.input = DescribeInstancesInput()
        aws_action.output = DescribeInstancesOutput()
        aws_action.handle_rest_call = unittest.mock.Mock(return_value={})
        aws_action.run()
        aws_action.handle_rest_call.assert_called_once()
