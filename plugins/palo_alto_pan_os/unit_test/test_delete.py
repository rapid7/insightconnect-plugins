import os
import sys

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from unittest.mock import patch, MagicMock

from jsonschema import validate
from komand_palo_alto_pan_os.actions.delete import Delete
from komand_palo_alto_pan_os.actions.delete.schema import DeleteInput, DeleteOutput, Input
from parameterized import parameterized

from util import Util


@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
class TestDelete(TestCase):
    @parameterized.expand(
        [
            [
                "address_group",
                "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address-group/entry[@name='Test Group']",
                {"response": {"@status": "success", "@code": "20", "msg": "command succeeded"}},
            ],
            [
                "address_object",
                "/config/devices/entry/vsys/entry/address/entry[@name='example.com']",
                {"response": {"@status": "success", "@code": "20", "msg": "command succeeded"}},
            ],
            [
                "policy",
                "/config/devices/entry/vsys/entry/rulebase/security/rules/entry[@name='Test Rule']",
                {"response": {"@status": "success", "@code": "20", "msg": "command succeeded"}},
            ],
        ]
    )
    def test_delete(self, mock_get: MagicMock, name: str, xpath: str, expected: dict) -> None:
        action = Util.default_connector(Delete())
        input_data = {Input.XPATH: xpath}
        validate(input_data, DeleteInput.schema)
        actual = action.run(input_data)
        self.assertEqual(actual, expected)
        validate(actual, DeleteOutput.schema)
