import os
import sys
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))
from komand_dynamodb.actions import Scan
from komand_dynamodb.actions.scan.schema import Input
from unit_test.util import Util


@patch("botocore.client.BaseClient._make_api_call", side_effect=Util.mock_request_exception_handling)
class TestExceptionsHandling(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connection(Scan())

    def test_wrong_table_name(self, mock_request):
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.TABLE_NAME: "wrong_table_name"})
        self.assertEqual("Requested resource not found.", context.exception.cause)
        self.assertEqual(
            "Check the input parameters they could be missing or incorrect and try again. Especially table name and region.",
            context.exception.assistance,
        )

    def test_wrong_credentials(self, mock_request):
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.TABLE_NAME: "wrong_credentials"})
        self.assertEqual("Error occurred when invoking the aws-cli.", context.exception.cause)
        self.assertEqual(
            "Check client connection keys and input arguments and try again.", context.exception.assistance
        )

    def test_endpoint_connection_error(self, mock_request):
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.TABLE_NAME: "endpoint_connection_error"})
        self.assertEqual(
            "Error occurred when invoking the aws-cli: Unable to reach the url endpoint.", context.exception.cause
        )
        self.assertEqual("Check the connection region is correct.", context.exception.assistance)

    def test_param_validation_error(self, mock_request):
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.TABLE_NAME: "param_validation_error"})
        self.assertEqual("Error occurred when invoking the aws-cli.", context.exception.cause)
        self.assertEqual(
            "Check the input parameters they could be missing or incorrect and try again.", context.exception.assistance
        )

    def test_unexpected_error(self, mock_request):
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.TABLE_NAME: "unexpected_error"})
        self.assertEqual("Error occurred when invoking the aws-cli.", context.exception.cause)
        self.assertEqual("Please contact with developers because some unexpected appear.", context.exception.assistance)
