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

    def test_add_to_policy_writes_the_src_zone_to_the_destination_zone(
        self, mock_get: MagicMock, mock_post: MagicMock
    ) -> None:
        # PAN-OS names the source zone <from> and the destination zone <to>, so both policy actions
        # have the two the wrong way round. This pins the behaviour rather than changing it: swapping
        # them changes what a published workflow writes to a live security rule, which is a release of
        # its own. Tracked separately.
        action = Util.default_connector(AddToPolicy())
        input_data = {
            Input.RULE_NAME: "Test Policy",
            Input.UPDATE_ACTIVE_OR_CANDIDATE_CONFIGURATION: "candidate",
            Input.SRC_ZONE: "trust",
        }
        validate(input_data, AddToPolicyInput.schema)
        action.run(input_data)

        writes = [call for call in Util.calls if call.get("action") == "edit"]
        self.assertEqual(len(writes), 1)
        self.assertIn("<to><member>trust</member></to>", writes[0].get("element"))
        self.assertIn("<from><member>any</member></from>", writes[0].get("element"))

    def test_add_to_policy_omits_hip_profiles_when_the_rule_has_none(
        self, mock_get: MagicMock, mock_post: MagicMock
    ) -> None:
        # PAN-OS 10.0 removed <hip-profiles> from the security rule, so writing one back to a rule that
        # does not carry it is rejected. The HIP Profiles input is ignored for such a rule.
        action = Util.default_connector(AddToPolicy())
        input_data = {
            Input.RULE_NAME: "PAN-OS 10 Policy",
            Input.UPDATE_ACTIVE_OR_CANDIDATE_CONFIGURATION: "candidate",
            Input.SOURCE: "2.2.2.2",
            Input.HIP_PROFILES: "Corporate Laptops",
        }
        validate(input_data, AddToPolicyInput.schema)
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
            "<source><member>1.1.1.1</member><member>2.2.2.2</member></source>"
            "<destination><member>any</member></destination>"
            "<service><member>application-default</member></service>"
            "<application><member>any</member></application>"
            "<category><member>any</member></category>"
            "<source-user><member>any</member></source-user>"
            "<action>allow</action>"
            "</entry>",
        )

    def test_add_to_policy_reports_a_rejected_element(self, mock_get: MagicMock, mock_post: MagicMock) -> None:
        # PAN-OS reports a rejected element as a <msg> holding one <line> per problem
        element = (
            '<entry name="Test Policy">'
            "<to><member>any</member></to>"
            "<from><member>any</member></from>"
            "<source><member>any</member></source>"
            "<destination><member>any</member></destination>"
            "<service><member>application-default</member><member>any</member></service>"
            "<application><member>any</member></application>"
            "<category><member>adult</member><member>abused-drugs</member><member>test1</member></category>"
            "<hip-profiles><member>any</member></hip-profiles>"
            "<source-user><member>Joe Smith</member></source-user>"
            "<action>drop</action>"
            "</entry>"
        )
        action = Util.default_connector(AddToPolicy())
        input_data = {
            Input.RULE_NAME: "Test Policy",
            Input.UPDATE_ACTIVE_OR_CANDIDATE_CONFIGURATION: "candidate",
            Input.URL_CATEGORY: "test1",
            Input.SOURCE_USER: "Joe Smith",
            Input.ACTION: "drop",
        }
        validate(input_data, AddToPolicyInput.schema)
        with self.assertRaises(PluginException) as e:
            action.run(input_data)

        # A value that is already in a key is not added a second time
        writes = [call for call in Util.calls if call.get("action") == "edit"]
        self.assertEqual(len(writes), 1)
        self.assertEqual(writes[0].get("element"), element)

        self.assertEqual(e.exception.cause, "PAN-OS returned an error in response to the request.")
        self.assertEqual(
            e.exception.assistance,
            f"This is likely because the provided element {element} does not exist or the xpath is not correct. "
            "Please verify the element name and xpath and try again.",
        )
        self.assertEqual(
            e.exception.data,
            str(
                [
                    "ICON Block Rule -> category 'hacking1' is not an allowed keyword",
                    "ICON Block Rule -> category 'hacking1' is not a valid reference",
                    "ICON Block Rule -> category is invalid",
                ]
            ),
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
