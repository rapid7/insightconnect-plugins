import sys
import os
from unittest import TestCase
from komand_palo_alto_pan_os.actions.show import Show
from komand_palo_alto_pan_os.actions.show.schema import Input, Output
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))


@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
class TestShow(TestCase):
    @parameterized.expand(
        [
            [
                "address_group",
                "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address-group/entry[@name='Test Group']",
                {
                    "response": {
                        "@status": "success",
                        "result": {
                            "entry": {"@name": "Test Group", "static": {"member": ["example.com", "1.1.1.1", "IPv6"]}}
                        },
                    }
                },
            ],
            [
                "policy",
                "/config/devices/entry/vsys/entry/rulebase/security/rules/entry[@name='Test Policy']",
                {
                    "response": {
                        "@status": "success",
                        "result": {
                            "entry": {
                                "@name": "Test Policy",
                                "@uuid": "290ba776-4bd0-49b2-8c20-a35467b22c11",
                                "to": {"member": "any"},
                                "from": {"member": "any"},
                                "source": {"member": "any"},
                                "destination": {"member": "any"},
                                "service": {"member": ["application-default", "any"]},
                                "application": {"member": "any"},
                                "category": {"member": ["adult", "abused-drugs"]},
                                "hip-profiles": {"member": "any"},
                                "source-user": {"member": "Joe Smith"},
                                "action": "drop",
                            }
                        },
                    }
                },
            ],
        ]
    )
    def test_show(self, mock_get, name, xpath, expected):
        action = Util.default_connector(Show())
        actual = action.run({Input.XPATH: xpath})
        self.assertEqual(actual, expected)
