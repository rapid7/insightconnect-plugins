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


class TestGetRemediationAction(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetRemediationAction())

    @patch("requests.get", side_effect=Util.mocked_requests)
    def test_get_remediation_action(self, mock_post):
        actual = self.action.run(
                {
                    Input.INCIDENT_ID: "63431",
                }
            )
        expected = {'remediation_details': 'WILL_AUTO_REMEDIATE'}
        self.assertEqual(actual, expected)
        