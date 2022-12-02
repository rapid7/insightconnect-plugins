import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_rapid7_insightcloudsec.actions.list_resource_tags import ListResourceTags
from icon_rapid7_insightcloudsec.actions.list_resource_tags.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests)
class TestListResourceTags(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListResourceTags())

    @parameterized.expand(Util.load_parameters("list_resource_tags").get("parameters"))
    def test_list_resource_tags(self, mock_request, name, resource_id, expected):
        actual = self.action.run({Input.RESOURCEID: resource_id})
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("list_resource_tags_bad").get("parameters"))
    def test_list_resource_tags_bad(self, mock_request, name, resource_id, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.RESOURCEID: resource_id})
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
