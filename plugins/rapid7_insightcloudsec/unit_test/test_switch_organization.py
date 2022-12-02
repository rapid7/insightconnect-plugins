import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_rapid7_insightcloudsec.actions.switch_organization import SwitchOrganization
from icon_rapid7_insightcloudsec.actions.switch_organization.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests)
class TestSwitchOrganization(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(SwitchOrganization())

    @parameterized.expand(Util.load_parameters("switch_organization").get("parameters"))
    def test_switch_organization(self, mock_request, name, organization_name, expected):
        actual = self.action.run({Input.ORGANIZATIONNAME: organization_name})
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("switch_organization_bad").get("parameters"))
    def test_switch_organization_bad(self, mock_request, name, organization_name, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.ORGANIZATIONNAME: organization_name})
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
