import os
import sys

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from unittest.mock import patch, MagicMock

from jsonschema import validate
from komand_palo_alto_pan_os.actions.show import Show
from komand_palo_alto_pan_os.actions.show.schema import Input, ShowInput, ShowOutput
from parameterized import parameterized

from util import Util


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
    def test_show(
        self,
        mock_get: MagicMock,
        name: str,
        xpath: str,
        expected: dict,
    ) -> None:
        action = Util.default_connector(Show())
        input_data = {Input.XPATH: xpath}
        validate(input_data, ShowInput.schema)
        actual = action.run(input_data)
        self.assertEqual(actual, expected)
        validate(actual, ShowOutput.schema)
