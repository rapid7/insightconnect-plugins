import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_rapid7_insightcloudsec.actions.detach_policy import DetachPolicy
from icon_rapid7_insightcloudsec.actions.detach_policy.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests)
class TestDetachPolicy(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DetachPolicy())

    @parameterized.expand(Util.load_parameters("detach_policy").get("parameters"))
    def test_detach_policy(self, mock_request, name, resource_id, policy_resource_id, expected):
        actual = self.action.run({Input.RESOURCEID: resource_id, Input.POLICYRESOURCEID: policy_resource_id})
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("detach_policy_bad").get("parameters"))
    def test_detach_policy_bad(self, mock_request, name, resource_id, policy_resource_id, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.RESOURCEID: resource_id, Input.POLICYRESOURCEID: policy_resource_id})
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
