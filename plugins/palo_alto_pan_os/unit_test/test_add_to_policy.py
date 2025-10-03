import os
import sys

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from unittest.mock import patch, MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_palo_alto_pan_os.actions.add_to_policy import AddToPolicy
from komand_palo_alto_pan_os.actions.add_to_policy.schema import AddToPolicyInput, AddToPolicyOutput, Input
from parameterized import parameterized

from util import Util


@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
@patch("requests.sessions.Session.post", side_effect=Util.mocked_requests)
class TestAddToPolicy(TestCase):
    @parameterized.expand(
        [
            [
                "update_active_configuration",
                "Test Policy",
                "active",
                "any",
                "any",
                "any",
                "any",
                "Example User",
                "any",
                "any",
                "adult",
                "any",
                "drop",
                {"message": "command succeeded", "status": "success", "code": "20"},
            ],
            [
                "update_candidate_configuration",
                "Test Policy",
                "candidate",
                "any",
                "any",
                "any",
                "any",
                "Example User",
                "any",
                "any",
                "adult",
                "any",
                "drop",
                {"message": "command succeeded", "status": "success", "code": "20"},
            ],
        ]
    )
    def test_add_to_policy(
        self,
        mock_get: MagicMock,
        mock_post: MagicMock,
        name: str,
        rule_name: str,
        update_active_or_candidate_configuration: str,
        source: str,
        destination: str,
        service: str,
        application: str,
        source_user: str,
        src_zone: str,
        dst_zone: str,
        url_category: str,
        hip_profiles: str,
        new_action: str,
        expected: dict,
    ) -> None:
        action = Util.default_connector(AddToPolicy())
        input_data = {
            Input.RULE_NAME: rule_name,
            Input.UPDATE_ACTIVE_OR_CANDIDATE_CONFIGURATION: update_active_or_candidate_configuration,
            Input.SOURCE: source,
            Input.DESTINATION: destination,
            Input.SERVICE: service,
            Input.APPLICATION: application,
            Input.SOURCE_USER: source_user,
            Input.SRC_ZONE: src_zone,
            Input.DST_ZONE: dst_zone,
            Input.URL_CATEGORY: url_category,
            Input.HIP_PROFILES: hip_profiles,
            Input.ACTION: new_action,
        }
        validate(input_data, AddToPolicyInput.schema)
        actual = action.run(input_data)
        self.assertEqual(actual, expected)
        validate(actual, AddToPolicyOutput.schema)

    @parameterized.expand(
        [
            [
                "invalid_rule_name",
                "Invalid Rule Name",
                "active",
                "any",
                "any",
                "any",
                "any",
                "Example User",
                "any",
                "any",
                "adult",
                "any",
                "drop",
                "PAN-OS returned an error in response to the request.",
                "Double-check that inputs are valid. Contact support if this issue persists.",
                '{"line": "No such node"}',
            ]
        ]
    )
    def test_add_to_policy_bad(
        self,
        mock_get: MagicMock,
        mock_post: MagicMock,
        name: str,
        rule_name: str,
        update_active_or_candidate_configuration: str,
        source: str,
        destination: str,
        service: str,
        application: str,
        source_user: str,
        src_zone: str,
        dst_zone: str,
        url_category: str,
        hip_profiles: str,
        new_action: str,
        cause: str,
        assistance: str,
        data: str,
    ) -> None:
        action = Util.default_connector(AddToPolicy())
        input_data = {
            Input.RULE_NAME: rule_name,
            Input.UPDATE_ACTIVE_OR_CANDIDATE_CONFIGURATION: update_active_or_candidate_configuration,
            Input.SOURCE: source,
            Input.DESTINATION: destination,
            Input.SERVICE: service,
            Input.APPLICATION: application,
            Input.SOURCE_USER: source_user,
            Input.SRC_ZONE: src_zone,
            Input.DST_ZONE: dst_zone,
            Input.URL_CATEGORY: url_category,
            Input.HIP_PROFILES: hip_profiles,
            Input.ACTION: new_action,
        }
        validate(input_data, AddToPolicyInput.schema)
        with self.assertRaises(PluginException) as e:
            action.run(input_data)

        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
        self.assertEqual(e.exception.data, str(data))
