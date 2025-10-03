import os
import sys

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from unittest.mock import patch, MagicMock

from jsonschema import validate
from komand_palo_alto_pan_os.actions.get import Get
from komand_palo_alto_pan_os.actions.get.schema import GetInput, GetOutput, Input
from parameterized import parameterized

from util import Util


@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
class TestGet(TestCase):
    @parameterized.expand(
        [
            [
                "address_object",
                "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address/entry[@name='1.1.1.1']",
                {
                    "response": {
                        "@status": "success",
                        "@code": "19",
                        "result": {
                            "@total-count": "1",
                            "@count": "1",
                            "entry": {
                                "@name": "1.1.1.1",
                                "ip-netmask": "1.1.1.1",
                                "description": "Example Description",
                            },
                        },
                    }
                },
            ],
            [
                "address_group",
                "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address-group/entry[@name='Test Group']",
                {
                    "response": {
                        "@status": "success",
                        "@code": "19",
                        "result": {
                            "@total-count": "1",
                            "@count": "1",
                            "entry": {
                                "@name": "Test Group",
                                "@admin": "admin",
                                "@dirtyId": "144",
                                "@time": "2021/12/14 09:43:15",
                                "static": {
                                    "@admin": "admin",
                                    "@dirtyId": "144",
                                    "@time": "2021/12/14 09:43:15",
                                    "member": [
                                        {
                                            "@admin": "admin",
                                            "@dirtyId": "144",
                                            "@time": "2021/12/14 09:43:15",
                                            "#text": "1.1.1.1",
                                        },
                                        {
                                            "@admin": "admin",
                                            "@dirtyId": "144",
                                            "@time": "2021/12/14 09:43:15",
                                            "#text": "test.com",
                                        },
                                        {
                                            "@admin": "admin",
                                            "@dirtyId": "144",
                                            "@time": "2021/12/14 09:43:15",
                                            "#text": "IPv6",
                                        },
                                    ],
                                },
                            },
                        },
                    }
                },
            ],
            [
                "policy",
                "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/rulebase/security/rules/entry[@name='Test Rule']",
                {
                    "response": {
                        "@status": "success",
                        "@code": "19",
                        "result": {
                            "@total-count": "1",
                            "@count": "1",
                            "entry": {
                                "@name": "Test Rule",
                                "@admin": "admin",
                                "@dirtyId": "145",
                                "@time": "2021/12/17 08:10:05",
                                "@uuid": "6783a432-c27a-4bc7-9535-7652ab5a4987",
                                "to": {
                                    "@admin": "admin",
                                    "@dirtyId": "145",
                                    "@time": "2021/12/17 08:10:05",
                                    "member": {
                                        "@admin": "admin",
                                        "@dirtyId": "145",
                                        "@time": "2021/12/17 08:10:05",
                                        "#text": "any",
                                    },
                                },
                                "from": {
                                    "@admin": "admin",
                                    "@dirtyId": "145",
                                    "@time": "2021/12/17 08:10:05",
                                    "member": {
                                        "@admin": "admin",
                                        "@dirtyId": "145",
                                        "@time": "2021/12/17 08:10:05",
                                        "#text": "any",
                                    },
                                },
                                "source": {
                                    "@admin": "admin",
                                    "@dirtyId": "145",
                                    "@time": "2021/12/17 08:10:05",
                                    "member": {
                                        "@admin": "admin",
                                        "@dirtyId": "145",
                                        "@time": "2021/12/17 08:10:05",
                                        "#text": "any",
                                    },
                                },
                                "destination": {
                                    "@admin": "admin",
                                    "@dirtyId": "145",
                                    "@time": "2021/12/17 08:10:05",
                                    "member": {
                                        "@admin": "admin",
                                        "@dirtyId": "145",
                                        "@time": "2021/12/17 08:10:05",
                                        "#text": "any",
                                    },
                                },
                                "source-user": {
                                    "@admin": "admin",
                                    "@dirtyId": "145",
                                    "@time": "2021/12/17 08:10:05",
                                    "member": {
                                        "@admin": "admin",
                                        "@dirtyId": "145",
                                        "@time": "2021/12/17 08:10:05",
                                        "#text": "any",
                                    },
                                },
                                "category": {
                                    "@admin": "admin",
                                    "@dirtyId": "145",
                                    "@time": "2021/12/17 08:10:05",
                                    "member": {
                                        "@admin": "admin",
                                        "@dirtyId": "145",
                                        "@time": "2021/12/17 08:10:05",
                                        "#text": "any",
                                    },
                                },
                                "application": {
                                    "@admin": "admin",
                                    "@dirtyId": "145",
                                    "@time": "2021/12/17 08:10:05",
                                    "member": {
                                        "@admin": "admin",
                                        "@dirtyId": "145",
                                        "@time": "2021/12/17 08:10:05",
                                        "#text": "any",
                                    },
                                },
                                "service": {
                                    "@admin": "admin",
                                    "@dirtyId": "145",
                                    "@time": "2021/12/17 08:10:05",
                                    "member": {
                                        "@admin": "admin",
                                        "@dirtyId": "145",
                                        "@time": "2021/12/17 08:10:05",
                                        "#text": "application-default",
                                    },
                                },
                                "hip-profiles": {
                                    "@admin": "admin",
                                    "@dirtyId": "145",
                                    "@time": "2021/12/17 08:10:05",
                                    "member": {
                                        "@admin": "admin",
                                        "@dirtyId": "145",
                                        "@time": "2021/12/17 08:10:05",
                                        "#text": "any",
                                    },
                                },
                                "action": {
                                    "@admin": "admin",
                                    "@dirtyId": "145",
                                    "@time": "2021/12/17 08:10:05",
                                    "#text": "drop",
                                },
                            },
                        },
                    }
                },
            ],
        ]
    )
    def test_get(self, mock_get: MagicMock, name: str, xpath: str, expected: dict) -> None:
        action = Util.default_connector(Get())
        input_data = {Input.XPATH: xpath}
        validate(input_data, GetInput.schema)
        actual = action.run(input_data)
        self.assertEqual(actual, expected)
        validate(actual, GetOutput.schema)
