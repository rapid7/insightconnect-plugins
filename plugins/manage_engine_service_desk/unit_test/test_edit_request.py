import json
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema.validators import validate

from util import Util
from parameterized import parameterized
from icon_manage_engine_service_desk.actions.edit_request import EditRequest


@patch("requests.request", side_effect=Util.mock_request)
class TestEditRequest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(EditRequest())

    @parameterized.expand(
        [
            [
                "valid_parameters",
                Util.read_file_to_dict("inputs/edit_request.json.inp"),
                Util.read_file_to_dict("expected/edit_request.json.exp"),
            ],
        ]
    )
    def test_edit_request(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            # Typed inputs win over additional fields and a false custom field value is not stripped
            [
                "template_and_additional_fields",
                Util.read_file_to_dict("inputs/edit_request_extra_fields.json.inp"),
                {
                    "subject": "Edit request",
                    "template": {"name": "Default Template"},
                    "impact_details": "Details of the impact",
                    "sla": {"name": "High"},
                    "udf_fields": {"udf_char1": "test", "udf_boolean1": False},
                },
            ],
            # Additional fields alone count as input and are sent at the top level of the request
            [
                "only_additional_fields",
                Util.read_file_to_dict("inputs/edit_request_only_additional_fields.json.inp"),
                {"subject": "Edit request", "impact_details": "Details of the impact"},
            ],
        ]
    )
    def test_edit_request_extra_fields(
        self, mock_request: MagicMock, test_name: str, input_params: dict, expected_request: dict
    ) -> None:
        result = self.action.run(input_params)
        validate(result, self.action.output.schema)

        sent_request = json.loads(mock_request.call_args.kwargs["data"]["input_data"])["request"]
        self.assertEqual(sent_request, expected_request)

    @parameterized.expand(
        [
            [
                "request_not_found",
                Util.read_file_to_dict("inputs/edit_request_request_not_found.json.inp"),
                "Resource not found.",
                "Please verify inputs and if the issue persists, contact support.",
                Util.read_file_to_dict("expected/request_not_found.json.exp"),
            ],
            [
                "not_enough_parameters",
                Util.read_file_to_dict("inputs/edit_request_not_enough_parameters.json.inp"),
                "Not enough input parameters were provided.",
                "Please provide at least one input parameter except request id and try again. If the issue persists, please contact support.",
                "",
            ],
            [
                "empty_additional_fields",
                Util.read_file_to_dict("inputs/edit_request_empty_additional_fields.json.inp"),
                "Not enough input parameters were provided.",
                "Please provide at least one input parameter except request id and try again. If the issue persists, please contact support.",
                "",
            ],
        ]
    )
    def test_edit_request_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance, data):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, str(data))
