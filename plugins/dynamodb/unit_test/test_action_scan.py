import os
import sys
from unittest import TestCase
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))
from komand_dynamodb.actions import Scan
from komand_dynamodb.actions.scan.schema import Input
from unit_test.util import Util


@patch("botocore.client.BaseClient._make_api_call", side_effect=Util.mocked_request)
class TestActionScan(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connection(Scan())

    def test_scan(self, mock_request):
        actual = self.action.run(
            {
                Input.TABLE_NAME: "test_table_for_scan",
                Input.CONSISTENT_READ: False,
                Input.EXCLUSIVE_START_KEY: {},
                Input.EXPRESSION_ATTRIBUTE_NAMES: {},
                Input.EXPRESSION_ATTRIBUTE_VALUES: {},
                Input.FILTER_EXPRESSION: "",
                Input.INDEX_NAME: "",
                Input.LIMIT: 100,
                Input.PROJECTION_EXPRESSION: "",
                Input.RETURN_CONSUMED_CAPACITY: "INDEXES",
                Input.SEGMENT: 100,
                Input.SELECT: "ALL_ATTRIBUTES",
                Input.TOTAL_SEGMENTS: 100,
            }
        )
        expected = Util.load_json("payloads/action_scan.json.exp")
        self.assertEqual(expected, actual)
