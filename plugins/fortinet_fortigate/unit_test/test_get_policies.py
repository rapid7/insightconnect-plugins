import sys
import os

from unittest import TestCase
from icon_fortinet_fortigate.actions.get_policies import GetPolicies
from icon_fortinet_fortigate.actions.get_policies.schema import Input, Output
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))


@patch("requests.Session.request", side_effect=Util.mocked_requests)
class TestGetPolicies(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetPolicies())

    @parameterized.expand(
        [
            [
                "get_policies",
                "Test Policy",
                {
                    "policies": [
                        {
                            "policyid": 1,
                            "q_origin_key": 1,
                            "name": "Test Policy",
                            "uuid": "6193559a-6862-51ea-44ce-e27594b8536a",
                            "srcintf": [{"name": "port1", "q_origin_key": "port1"}],
                            "dstintf": [{"name": "port1", "q_origin_key": "port1"}],
                            "srcaddr": [{"name": "Test Group", "q_origin_key": "Test Group"}],
                            "dstaddr": [{"name": "Test Group", "q_origin_key": "Test Group"}],
                            "action": "accept",
                            "service": [{"name": "ALL", "q_origin_key": "ALL"}],
                        }
                    ],
                },
            ],
            [
                "get_policies_invalid_name",
                "Invalid Policy",
                {
                    "policies": [],
                },
            ],
        ]
    )
    def test_get_policies(self, mock_request, name, name_filter, expected):
        actual = self.action.run({Input.NAME_FILTER: name_filter})
        self.assertEqual(actual, expected)
