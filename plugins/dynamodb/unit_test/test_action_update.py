import os
import sys
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))
from komand_dynamodb.actions import Update
from komand_dynamodb.actions.update.schema import Input
from unit_test.util import Util


@patch("botocore.client.BaseClient._make_api_call", side_effect=Util.mocked_request)
class TestActionUpdate(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connection(Update())

    def test_update(self, mock_request):
        actual = self.action.run(
            {
                Input.CONDITION_EXPRESSION: "",
                Input.EXPRESSION_ATTRIBUTE_NAMES: {"#AT": "AlbumTitle"},
                Input.EXPRESSION_ATTRIBUTE_VALUES: {":t": {"S": "Louder Than Everrrrrr"}},
                Input.KEY: {"partitional_key": {"S": "test3"}},
                Input.RETURN_VALUES: "ALL_NEW",
                Input.TABLE_NAME: "test_table_for_update",
                Input.UPDATE_EXPRESSION: "SET #AT = :t",
                Input.RETURN_CONSUMED_CAPACITY: "INDEXES",
                Input.RETURN_ITEM_COLLECTION_METRICS: False,
            }
        )
        expect = {"success": True}
        self.assertEqual(expect, actual)

    def test_bad_update_not_valid_key(self, mock_request):
        with self.assertRaises(PluginException) as context:
            self.action.run(
                {
                    Input.CONDITION_EXPRESSION: "",
                    Input.EXPRESSION_ATTRIBUTE_NAMES: {"#AT": "AlbumTitle"},
                    Input.EXPRESSION_ATTRIBUTE_VALUES: {":t": {"S": "Louder Than Everrrrrr"}},
                    Input.KEY: {"wrong_key": {"S": "test3"}},
                    Input.RETURN_VALUES: "ALL_NEW",
                    Input.TABLE_NAME: "test_table_for_update",
                    Input.UPDATE_EXPRESSION: "SET #AT = :t",
                    Input.RETURN_CONSUMED_CAPACITY: "INDEXES",
                    Input.RETURN_ITEM_COLLECTION_METRICS: False,
                }
            )
        self.assertEqual("Error occurred when invoking the aws-cli.", context.exception.cause)
        self.assertEqual(
            "Check client connection keys and input arguments and try again.", context.exception.assistance
        )
        self.assertEqual(Util.load_json("payloads/action_bad_update_validation_exception.exp"), context.exception.data)
