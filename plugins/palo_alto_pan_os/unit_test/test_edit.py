import sys
import os

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from komand_palo_alto_pan_os.actions.edit import Edit
from komand_palo_alto_pan_os.actions.edit.schema import Input, EditInput, EditOutput
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from jsonschema import validate


@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
@patch("requests.sessions.Session.post", side_effect=Util.mocked_requests)
class TestEdit(TestCase):
    @parameterized.expand(
        [
            [
                "policy",
                "/config/devices/entry/vsys/entry/rulebase/security/rules/entry[@name='Test Rule']/action",
                "<action>drop</action>",
                {"response": {"response": {"@status": "success", "@code": "20", "msg": "command succeeded"}}},
            ],
            [
                "address_object",
                "/config/devices/entry/vsys/entry/address/entry[@name='example.com']/tag",
                "<tag><member>test</member></tag>",
                {"response": {"response": {"@status": "success", "@code": "20", "msg": "command succeeded"}}},
            ],
            [
                "address_group",
                "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address-group/entry[@name='Test Group']",
                "<entry name='Test Group'><static><member>example.com</member><member>IPv6</member></static></entry>",
                {"response": {"response": {"@status": "success", "@code": "20", "msg": "command succeeded"}}},
            ],
        ]
    )
    def test_edit(self, mock_get, mock_post, name, xpath, element, expected):
        action = Util.default_connector(Edit())
        input_data = {Input.XPATH: xpath, Input.ELEMENT: element}
        validate(input_data, EditInput.schema)
        actual = action.run(input_data)
        self.assertEqual(actual, expected)
        validate(actual, EditOutput.schema)
