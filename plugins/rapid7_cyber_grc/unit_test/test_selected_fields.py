import importlib
import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from parameterized import parameterized

# Every typed read action that offers Fields ($select), with its output key. A step's
# output is validated against the record type, so a record narrowed to a few fields has
# to pass that validation: the record types declare no required fields.
ACTIONS = [
    ("get_assessment", "assessment", False),
    ("get_assessments", "assessments", True),
    ("get_risk", "risk", False),
    ("get_risks", "risks", True),
    ("get_tasks", "tasks", True),
    ("get_vendors", "vendors", True),
]


class TestSelectedFieldsPassOutputValidation(TestCase):
    @parameterized.expand(ACTIONS)
    def test_a_record_holding_only_the_selected_fields_validates(self, action, key, is_list):
        schema = importlib.import_module(f"icon_rapid7_cyber_grc.actions.{action}.schema")
        output_class = next(
            getattr(schema, name) for name in dir(schema) if name.endswith("Output") and name != "Output"
        )
        record = {"id": 7, "name": "Only two fields"}
        output = {key: [record] if is_list else record}
        if is_list:
            output["count"] = 1

        output_class().validate(output)

    @parameterized.expand(ACTIONS)
    def test_the_input_is_titled_fields(self, action, _key, _is_list):
        schema = importlib.import_module(f"icon_rapid7_cyber_grc.actions.{action}.schema")
        input_class = next(getattr(schema, name) for name in dir(schema) if name.endswith("Input") and name != "Input")

        self.assertEqual(input_class.schema["properties"]["select"]["title"], "Fields")
