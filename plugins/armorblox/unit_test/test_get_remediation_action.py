import os
import sys

from util import Util

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_armorblox.actions.get_remediation_action import GetRemediationAction
from icon_armorblox.actions.get_remediation_action.schema import Input
from unittest.mock import patch, Mock
from parameterized import parameterized


@patch("requests.get", side_effect=Util.mocked_requests)
class TestGetIndicatorDetails(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(GetRemediationAction())

    @parameterized.expand([("10597"), ("11081"), ("11063")])
    def test_get_remediation_action(self, mock_post: Mock, incident_id: str) -> None:
        actual = self.action.run({Input.INCIDENT_ID: incident_id})
        expected = {"remediation_details": "WILL_AUTO_REMEDIATE"}
        self.assertEqual(actual, expected)
