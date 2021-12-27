import sys
import os
from unittest import TestCase
from komand_palo_alto_pan_os.actions.set_security_policy_rule import SetSecurityPolicyRule
from komand_palo_alto_pan_os.actions.set_security_policy_rule.schema import Input, Output
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))


@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
@patch("requests.sessions.Session.post", side_effect=Util.mocked_requests)
class TestSetSecurityPolicyRule(TestCase):
    @parameterized.expand(
        [
            [
                "test_policy_1",
                "Test Policy 1",
                "any",
                "any",
                "any",
                "any",
                "drop",
                "Example User",
                False,
                False,
                False,
                False,
                False,
                False,
                "Test Rule",
                "any",
                "any",
                {"response": {"@status": "success", "@code": "20", "msg": "command succeeded"}},
            ],
            [
                "test_policy_2",
                "Test Policy 2",
                "198.51.100.1",
                "198.51.100.2",
                "any",
                "8x8",
                "deny",
                "Example User",
                True,
                True,
                True,
                True,
                True,
                True,
                "Test Rule",
                "any",
                "any",
                {"response": {"@status": "success", "@code": "20", "msg": "command succeeded"}},
            ],
        ]
    )
    def test_set_security_policy_rule(
        self,
        mock_get,
        mock_post,
        name,
        rule_name,
        source,
        destination,
        service,
        application,
        policy_action,
        source_user,
        disable_server_response_inspection,
        negate_source,
        negate_destination,
        disabled,
        log_start,
        log_end,
        description,
        src_zone,
        dst_zone,
        expected,
    ):
        action = Util.default_connector(SetSecurityPolicyRule())
        actual = action.run(
            {
                Input.RULE_NAME: rule_name,
                Input.SOURCE: source,
                Input.DESTINATION: destination,
                Input.SERVICE: service,
                Input.APPLICATION: application,
                Input.ACTION: policy_action,
                Input.SOURCE_USER: source_user,
                Input.DISABLE_SERVER_RESPONSE_INSPECTION: disable_server_response_inspection,
                Input.NEGATE_SOURCE: negate_source,
                Input.NEGATE_DESTINATION: negate_destination,
                Input.DISABLED: disabled,
                Input.LOG_START: log_start,
                Input.LOG_END: log_end,
                Input.DESCRIPTION: description,
                Input.SRC_ZONE: src_zone,
                Input.DST_ZONE: dst_zone,
            }
        )
        self.assertEqual(actual, expected)
