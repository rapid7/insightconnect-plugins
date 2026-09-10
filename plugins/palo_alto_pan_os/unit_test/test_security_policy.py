import logging
import os
import sys

sys.path.append(os.path.abspath("../"))
from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_palo_alto_pan_os.util.util import SecurityPolicy, extract_member_names
from parameterized import parameterized


class TestExtractMemberNames(TestCase):
    @parameterized.expand(
        [
            # PAN-OS returns a different shape for every member count and configuration state
            ["several_members", ["1.1.1.1", "test.com"], ["1.1.1.1", "test.com"]],
            ["one_member", "test.com", ["test.com"]],
            [
                "one_uncommitted_member",
                {"@admin": "admin", "@dirtyId": "144", "@time": "2021/12/14 09:43:15", "#text": "test.com"},
                ["test.com"],
            ],
            [
                "several_uncommitted_members",
                [
                    {"@dirtyId": "144", "#text": "1.1.1.1"},
                    {"@dirtyId": "144", "#text": "test.com"},
                ],
                ["1.1.1.1", "test.com"],
            ],
            ["no_members", None, []],
            ["empty_member", {"@dirtyId": "144"}, []],
        ]
    )
    def test_extract_member_names(self, name: str, member, expected: list) -> None:
        self.assertEqual(extract_member_names(member), expected)


class TestSecurityPolicyKeys(TestCase):
    def setUp(self) -> None:
        self.policy = SecurityPolicy(logger=logging.getLogger("test logger"))

    @parameterized.expand(
        [
            ["adds_to_a_list", ["1.1.1.1", "test.com"], "2.2.2.2", ["1.1.1.1", "test.com", "2.2.2.2"]],
            ["adds_to_a_lone_value", "1.1.1.1", "2.2.2.2", ["1.1.1.1", "2.2.2.2"]],
            ["replaces_any", "any", "1.1.1.1", "1.1.1.1"],
            ["skips_a_value_already_in_a_list", ["1.1.1.1", "test.com"], "test.com", ["1.1.1.1", "test.com"]],
            ["skips_a_lone_value_already_there", "test.com", "test.com", "test.com"],
            # 'trust' is a substring of 'trust-zone', but it is not a value of the key
            ["adds_a_value_that_is_a_substring", "trust-zone", "trust", ["trust-zone", "trust"]],
            ["adds_a_value_that_is_a_substring_of_a_list_item", ["trust-zone"], "trust", ["trust-zone", "trust"]],
        ]
    )
    def test_add_to_key(self, name: str, key, add: str, expected) -> None:
        self.assertEqual(self.policy.add_to_key(key, add), expected)

    @parameterized.expand(
        [
            ["removes_from_a_pair", ["1.1.1.1", "test.com"], "test.com", ["1.1.1.1"]],
            ["removes_from_three", ["1.1.1.1", "test.com", "IPv6"], "test.com", ["1.1.1.1", "IPv6"]],
            [
                "removes_from_four",
                ["1.1.1.1", "test.com", "IPv6", "2.2.2.2"],
                "test.com",
                ["1.1.1.1", "IPv6", "2.2.2.2"],
            ],
            ["removes_every_copy", ["test.com", "1.1.1.1", "test.com"], "test.com", ["1.1.1.1"]],
            # A key set to the 'any' keyword already matches everything, so removing it narrows nothing
            ["leaves_a_wildcard_key_alone", "any", "any", "any"],
            ["leaves_a_list_alone_when_the_value_is_absent", ["1.1.1.1"], "test.com", ["1.1.1.1"]],
            ["leaves_a_lone_value_alone_when_it_does_not_match", "1.1.1.1", "test.com", "1.1.1.1"],
            # 'trust' is a substring of 'trust-zone', but it is not a value of the key
            ["leaves_a_value_that_only_contains_the_removal", "trust-zone", "trust", "trust-zone"],
            ["leaves_a_list_item_that_only_contains_the_removal", ["trust-zone"], "trust", ["trust-zone"]],
        ]
    )
    def test_remove_from_key(self, name: str, key, remove: str, expected) -> None:
        self.assertEqual(self.policy.remove_from_key(key, remove, "source"), expected)

    @parameterized.expand(
        [
            # A policy key cannot be empty and the only value PAN-OS takes in place of the last one is
            # the 'any' keyword, which widens the rule instead of narrowing it, so removal is refused
            ["a_lone_value", "test.com"],
            ["a_single_item_list", ["test.com"]],
            ["every_copy_of_the_only_value", ["test.com", "test.com"]],
        ]
    )
    def test_remove_from_key_refuses_to_empty_a_key(self, name: str, key) -> None:
        with self.assertRaises(PluginException) as error:
            self.policy.remove_from_key(key, "test.com", "source")

        self.assertEqual(
            error.exception.cause, "'test.com' is the only value of the 'source' key of this security rule."
        )
        self.assertIn("cannot be removed", error.exception.assistance)

    @parameterized.expand(
        [
            # Uncommitted values carry read-only attributes that cannot be written back out
            [
                "strips_attributes_from_a_lone_value",
                {"@dirtyId": "145", "#text": "1.1.1.1"},
                "1.1.1.1",
            ],
            [
                "strips_attributes_from_a_list",
                [{"@dirtyId": "145", "#text": "1.1.1.1"}, "test.com"],
                ["1.1.1.1", "test.com"],
            ],
        ]
    )
    def test_extract_from_security_policy_strips_attributes(self, name: str, member, expected) -> None:
        policy = {
            "response": {
                "result": {
                    "entry": {
                        "source": {"member": member},
                        "action": "drop",
                    }
                }
            }
        }
        self.assertEqual(self.policy.extract_from_security_policy(policy)["source"], expected)
