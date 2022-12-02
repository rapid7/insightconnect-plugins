import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_rapid7_insightcloudsec.actions.get_resource_details import GetResourceDetails
from icon_rapid7_insightcloudsec.actions.get_resource_details.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests)
class TestGetResourceDetails(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetResourceDetails())

    @parameterized.expand(Util.load_parameters("get_resource_details").get("parameters"))
    def test_get_resource_details(self, mock_request, name, resource_id, expected):
        actual = self.action.run({Input.RESOURCEID: resource_id})
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("get_resource_details_bad").get("parameters"))
    def test_get_resource_details_bad(self, mock_request, name, resource_id, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.RESOURCEID: resource_id})
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
