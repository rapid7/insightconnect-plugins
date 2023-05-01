import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_armorblox.connection.connection import Connection
from icon_armorblox.actions.get_remediation_action import GetRemediationAction
from icon_armorblox.actions.get_remediation_action.schema import Input, Output
import json
import logging
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized


@patch("requests.get", side_effect=Util.mocked_requests)
class TestGetIndicatorDetails(TestCase):
    @parameterized.expand([("10597"),("11081"),("11063")])
    def test_get_remediation_action(self, mock_post, incident_id):
        action = Util.default_connector(GetRemediationAction())
        actual = action.run({Input.INCIDENT_ID: incident_id})
        expected = {'remediation_details': 'WILL_AUTO_REMEDIATE'}
        self.assertEqual(actual, expected)
