import sys
import os

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from komand_palo_alto_pan_os.actions.add_to_policy import AddToPolicy
from komand_palo_alto_pan_os.actions.add_to_policy.schema import Input, AddToPolicyInput, AddToPolicyOutput
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate


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
        mock_get,
        mock_post,
        name,
        rule_name,
        update_active_or_candidate_configuration,
        source,
        destination,
        service,
        application,
        source_user,
        src_zone,
        dst_zone,
        url_category,
        hip_profiles,
        new_action,
        expected,
    ):
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
        mock_get,
        mock_post,
        name,
        rule_name,
        update_active_or_candidate_configuration,
        source,
        destination,
        service,
        application,
        source_user,
        src_zone,
        dst_zone,
        url_category,
        hip_profiles,
        new_action,
        cause,
        assistance,
        data,
    ):
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
