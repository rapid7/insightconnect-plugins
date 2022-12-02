import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_rapid7_insightcloudsec.actions.remove_exemption import RemoveExemption
from icon_rapid7_insightcloudsec.actions.remove_exemption.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests)
class TestRemoveExemption(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(RemoveExemption())

    @parameterized.expand(Util.load_parameters("remove_exemption").get("parameters"))
    def test_remove_exemption(self, mock_request, name, exemption_ids, expected):
        actual = self.action.run({Input.EXEMPTIONIDS: exemption_ids})
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("remove_exemption_bad").get("parameters"))
    def test_remove_exemption_bad(self, mock_request, name, exemption_ids, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.EXEMPTIONIDS: exemption_ids})
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
