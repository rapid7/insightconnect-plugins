import os
import sys

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from unittest.mock import patch, MagicMock

from jsonschema import validate
from komand_palo_alto_pan_os.actions.set_security_policy_rule import SetSecurityPolicyRule
from komand_palo_alto_pan_os.actions.set_security_policy_rule.schema import (
    Input,
    SetSecurityPolicyRuleInput,
    SetSecurityPolicyRuleOutput,
)
from parameterized import parameterized

from util import Util


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
        mock_get: MagicMock,
        mock_post: MagicMock,
        name: str,
        rule_name: str,
        source: str,
        destination: str,
        service: str,
        application: str,
        policy_action: str,
        source_user: str,
        disable_server_response_inspection: bool,
        negate_source: bool,
        negate_destination: bool,
        disabled: bool,
        log_start: bool,
        log_end: bool,
        description: str,
        src_zone: str,
        dst_zone: str,
        expected: dict,
    ) -> None:
        action = Util.default_connector(SetSecurityPolicyRule())
        input_data = {
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
        validate(input_data, SetSecurityPolicyRuleInput.schema)
        actual = action.run(input_data)
        self.assertEqual(actual, expected)
        validate(actual, SetSecurityPolicyRuleOutput.schema)
