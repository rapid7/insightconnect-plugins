import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_rapid7_insightvm.actions.tag_assets import TagAssets

from util import Util


@patch("requests.sessions.Session.put", side_effect=Util.mocked_requests)
class TestTagAssets(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(TagAssets())

    def setUp(self) -> None:
        self.params = {
            "tag_id": 1,
            "asset_ids": [1, 2, 3],
            "tag_source": "CUSTOM",
            "tag_type": "Custom",
            "tag_name": "Example Tag",
        }

    def test_tag_asset(self, mock_put) -> None:
        expected = {"success": True}
        actual = self.action.run(self.params)
        self.assertEqual(actual, expected)

    def test_tag_asset_bad_id(self, mock_put) -> None:
        self.params["tag_id"] = 2
        cause = "Malformed JSON received along with a status code of Not Found"
        assistance = (
            "Verify your connection is pointing to your local console and not "
            "`exposure-analytics.insight.rapid7.com` Ensure that the requested resource exists."
        )
        data = "The ID 2 is not available. Enter a different ID for this tag."
        with self.assertRaises(PluginException) as error:
            self.action.run(self.params)
        self.assertEqual(cause, error.exception.cause)
        self.assertEqual(assistance, error.exception.assistance)
        self.assertEqual(data, error.exception.data)

    def test_tag_asset_bad_asset_ids(self, mock_put) -> None:
        self.params["asset_ids"] = [4, 5, 6]
        cause = "Malformed JSON received along with a status code of Internal Server Error"
        assistance = (
            "Verify your connection is pointing to your local console and not "
            "`exposure-analytics.insight.rapid7.com` If this issue persists contact support for assistance."
        )
        data = "An unexpected error occurred. See the nsc.log file for more information."
        with self.assertRaises(PluginException) as error:
            self.action.run(self.params)
        self.assertEqual(cause, error.exception.cause)
        self.assertEqual(assistance, error.exception.assistance)
        self.assertEqual(data, error.exception.data)

    def test_tag_asset_bad_tag_source(self, mock_put) -> None:
        self.params["tag_source"] = "VM"
        cause = "Malformed JSON received along with a status code of Conflict"
        assistance = (
            "Verify your connection is pointing to your local console and not "
            "`exposure-analytics.insight.rapid7.com` Ensure that the requested action does not cause a "
            "conflict with the current state of the target resource."
        )
        data = "You cannot change the source of a tag."
        with self.assertRaises(PluginException) as error:
            self.action.run(self.params)
        self.assertEqual(cause, error.exception.cause)
        self.assertEqual(assistance, error.exception.assistance)
        self.assertEqual(data, error.exception.data)

    def test_tag_asset_bad_tag_type(self, mock_put) -> None:
        self.params["tag_type"] = "Criticality"
        cause = "Malformed JSON received along with a status code of Method Not Allowed"
        assistance = (
            "Verify your connection is pointing to your local console and not "
            "`exposure-analytics.insight.rapid7.com` Ensure that the requested action is permitted."
        )
        data = "You cannot create, edit or remove the tag 4 because it is a built-in tag."
        with self.assertRaises(PluginException) as error:
            self.action.run(self.params)
        self.assertEqual(cause, error.exception.cause)
        self.assertEqual(assistance, error.exception.assistance)
        self.assertEqual(data, error.exception.data)
