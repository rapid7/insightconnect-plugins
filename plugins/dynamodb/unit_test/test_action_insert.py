import os.path
import sys
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))
from komand_dynamodb.actions import Insert
from komand_dynamodb.actions.insert.schema import Input
from unit_test.util import Util


@patch("botocore.client.BaseClient._make_api_call", side_effect=Util.mocked_request)
class TestActionInsrt(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connection(Insert())

    def test_insert(self, mock_request):
        actual = self.action.run(
            {
                Input.TABLE_NAME: "test_table_for_insert",
                Input.CONDITION_EXPRESSION: "",
                Input.EXPRESSION_ATTRIBUTE_NAMES: {},
                Input.EXPRESSION_ATTRIBUTE_VALUES: {},
                Input.ITEM: {
                    "partitional_key": {"S": "test3"},
                    "AlbumTitle": {"S": "Somewhat Famous"},
                    "Artist": {"S": "No One You Know"},
                    "SongTitle": {"S": "Call Me Today"},
                },
                Input.RETURN_CONSUMED_CAPACITY: "TOTAL",
                Input.RETURN_ITEM_COLLECTION_METRICS: False,
                Input.RETURN_VALUES: False,
            }
        )
        expect = {"success": True}
        self.assertEqual(expect, actual)

    def test_bad_insert_wrong_key(self, mock_request):
        with self.assertRaises(PluginException) as context:
            self.action.run(
                {
                    Input.TABLE_NAME: "test_table_for_insert",
                    Input.CONDITION_EXPRESSION: "",
                    Input.EXPRESSION_ATTRIBUTE_NAMES: {},
                    Input.EXPRESSION_ATTRIBUTE_VALUES: {},
                    Input.ITEM: {
                        "wrong_key": {"S": "test3"},
                        "AlbumTitle": {"S": "Somewhat Famous"},
                        "Artist": {"S": "No One You Know"},
                        "SongTitle": {"S": "Call Me Today"},
                    },
                    Input.RETURN_CONSUMED_CAPACITY: "TOTAL",
                    Input.RETURN_ITEM_COLLECTION_METRICS: False,
                    Input.RETURN_VALUES: False,
                }
            )
        self.assertEqual("Error occurred when invoking the aws-cli.", context.exception.cause)
        self.assertEqual(
            "Check client connection keys and input arguments and try again.", context.exception.assistance
        )
        self.assertEqual(Util.load_json("payloads/action_bad_insert_resource_not_found.resp"), context.exception.data)
