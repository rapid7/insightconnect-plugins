import sys
import os
from unittest import TestCase
from komand_palo_alto_pan_os.actions.delete import Delete
from komand_palo_alto_pan_os.actions.delete.schema import Input, Output
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))


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
    def test_delete(self, mock_get, name, xpath, expected):
        action = Util.default_connector(Delete())
        actual = action.run({Input.XPATH: xpath})
        self.assertEqual(actual, expected)
