import os
import sys

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from unittest.mock import patch, MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_palo_alto_pan_os.actions.remove_from_policy import RemoveFromPolicy
from komand_palo_alto_pan_os.actions.remove_from_policy.schema import (
    Input,
    RemoveFromPolicyInput,
    RemoveFromPolicyOutput,
)
from parameterized import parameterized

from util import Util


@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
@patch("requests.sessions.Session.post", side_effect=Util.mocked_requests)
class TestRemoveFromPolicy(TestCase):
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
    def test_remove_from_policy(
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
        action = Util.default_connector(RemoveFromPolicy())
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
        validate(input_data, RemoveFromPolicyInput.schema)
        actual = action.run(input_data)
        self.assertEqual(actual, expected)
        validate(actual, RemoveFromPolicyOutput.schema)

    @parameterized.expand(
        [
            [
                "removes_a_value_from_every_key_that_holds_it",
                {
                    Input.SERVICE: "any",
                    Input.URL_CATEGORY: "adult",
                    Input.SOURCE_USER: "Example User",
                    Input.ACTION: "allow",
                },
                '<entry name="Test Policy">'
                "<to><member>any</member></to>"
                "<from><member>any</member></from>"
                "<source><member>any</member></source>"
                "<destination><member>any</member></destination>"
                "<service><member>application-default</member></service>"
                "<application><member>any</member></application>"
                "<category><member>abused-drugs</member></category>"
                "<hip-profiles><member>any</member></hip-profiles>"
                "<source-user><member>Joe Smith</member></source-user>"
                "<action>drop</action>"
                "</entry>",
            ],
            [
                "leaves_every_key_alone_when_nothing_is_given",
                {},
                '<entry name="Test Policy">'
                "<to><member>any</member></to>"
                "<from><member>any</member></from>"
                "<source><member>any</member></source>"
                "<destination><member>any</member></destination>"
                "<service><member>application-default</member><member>any</member></service>"
                "<application><member>any</member></application>"
                "<category><member>adult</member><member>abused-drugs</member></category>"
                "<hip-profiles><member>any</member></hip-profiles>"
                "<source-user><member>Joe Smith</member></source-user>"
                "<action>drop</action>"
                "</entry>",
            ],
            # Removing the 'any' keyword from a key that already holds it narrows nothing, so the rule
            # is left as it is rather than the removal being refused
            [
                "leaves_a_wildcard_key_alone",
                {Input.SOURCE: "any", Input.SRC_ZONE: "any"},
                '<entry name="Test Policy">'
                "<to><member>any</member></to>"
                "<from><member>any</member></from>"
                "<source><member>any</member></source>"
                "<destination><member>any</member></destination>"
                "<service><member>application-default</member><member>any</member></service>"
                "<application><member>any</member></application>"
                "<category><member>adult</member><member>abused-drugs</member></category>"
                "<hip-profiles><member>any</member></hip-profiles>"
                "<source-user><member>Joe Smith</member></source-user>"
                "<action>drop</action>"
                "</entry>",
            ],
        ]
    )
    def test_remove_from_policy_element(
        self,
        mock_get: MagicMock,
        mock_post: MagicMock,
        name: str,
        removals: dict,
        expected_element: str,
    ) -> None:
        action = Util.default_connector(RemoveFromPolicy())
        input_data = {
            Input.RULE_NAME: "Test Policy",
            Input.UPDATE_ACTIVE_OR_CANDIDATE_CONFIGURATION: "candidate",
            **removals,
        }
        validate(input_data, RemoveFromPolicyInput.schema)
        action.run(input_data)

        writes = [call for call in Util.calls if call.get("action") == "edit"]
        self.assertEqual(len(writes), 1)
        # The action is never removed: a security rule always has exactly one, so the rule keeps it
        self.assertEqual(writes[0].get("element"), expected_element)

    def test_remove_from_policy_omits_hip_profiles_when_the_rule_has_none(
        self, mock_get: MagicMock, mock_post: MagicMock
    ) -> None:
        # PAN-OS 10.0 removed <hip-profiles> from the security rule, so writing one back to a rule that
        # does not carry it is rejected. The HIP Profiles input is ignored for such a rule.
        action = Util.default_connector(RemoveFromPolicy())
        input_data = {
            Input.RULE_NAME: "PAN-OS 10 Policy",
            Input.UPDATE_ACTIVE_OR_CANDIDATE_CONFIGURATION: "candidate",
            Input.DESTINATION: "any",
            Input.HIP_PROFILES: "Corporate Laptops",
        }
        validate(input_data, RemoveFromPolicyInput.schema)
        action.run(input_data)

        writes = [call for call in Util.calls if call.get("action") == "edit"]
        self.assertEqual(len(writes), 1)
        # <source-hip> and <destination-hip> are dropped too, because the write replaces the whole
        # <entry>. That is tracked separately and is not what this test covers.
        self.assertEqual(
            writes[0].get("element"),
            '<entry name="PAN-OS 10 Policy">'
            "<to><member>any</member></to>"
            "<from><member>any</member></from>"
            "<source><member>1.1.1.1</member></source>"
            "<destination><member>any</member></destination>"
            "<service><member>application-default</member></service>"
            "<application><member>any</member></application>"
            "<category><member>any</member></category>"
            "<source-user><member>any</member></source-user>"
            "<action>allow</action>"
            "</entry>",
        )

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
    def test_remove_from_policy_bad(
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
        action = Util.default_connector(RemoveFromPolicy())
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
        validate(input_data, RemoveFromPolicyInput.schema)
        with self.assertRaises(PluginException) as e:
            action.run(input_data)
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
        self.assertEqual(e.exception.data, data)
