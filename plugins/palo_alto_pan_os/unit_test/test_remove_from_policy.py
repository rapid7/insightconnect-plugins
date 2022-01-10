import sys
import os
from unittest import TestCase
from komand_palo_alto_pan_os.actions.remove_from_policy import RemoveFromPolicy
from komand_palo_alto_pan_os.actions.remove_from_policy.schema import Input, Output
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from komand.exceptions import PluginException

sys.path.append(os.path.abspath("../"))


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
            [
                "update_candidate_configuration",
                "Test Policy",
                "active",
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                {"message": "command succeeded", "status": "success", "code": "20"},
            ],
        ]
    )
    def test_remove_from_policy(
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
        action = Util.default_connector(RemoveFromPolicy())
        actual = action.run(
            {
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
        )
        self.assertEqual(actual, expected)

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
        action = Util.default_connector(RemoveFromPolicy())
        with self.assertRaises(PluginException) as e:
            action.run(
                {
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
            )
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
        self.assertEqual(e.exception.data, data)
