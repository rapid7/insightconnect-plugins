import os
import sys
from unittest import TestCase

sys.path.append(os.path.abspath("../"))
from komand_dynamodb.actions import GetItem
from komand_dynamodb.actions.get_item.schema import Input
from unit_test.util import Util


class TestActionGetItem(TestCase):
    """TestActionGetItem."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connection(GetItem())

    def test_get_item(self):
        actual = self.action.run(
            {
                Input.TABLE_NAME: "test_table_for_scan",
                Input.CONSISTENT_READ: False,
                Input.KEY: {},
                Input.EXPRESSION_ATTRIBUTE_NAMES: {},
                Input.PROJECTION_EXPRESSION: "",
                Input.RETURN_CONSUMED_CAPACITY: "INDEXES",
            }
        )
        expected = Util.load_json("payloads/action_get_item.json.exp.resp")
        self.assertEqual(expected, actual)
