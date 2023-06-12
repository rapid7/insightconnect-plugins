import os
import sys
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

sys.path.append(os.path.abspath("../"))

from komand_mimecast.actions import FindGroups

from util import Util


@patch("requests.request", side_effect=Util.mocked_request)
class TestResponseStatusCodeHandling(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(FindGroups())

    def test_500_response(self, mocked_request):
        with self.assertRaises(PluginException) as exception:
            self.action.run(Util.load_json("inputs/find_groups_500.json.exp"))
        self.assertEqual(
            exception.exception.cause, ConnectionTestException.causes.get(PluginException.Preset.SERVER_ERROR)
        )
        self.assertEqual(
            exception.exception.assistance, ConnectionTestException.assistances.get(PluginException.Preset.SERVER_ERROR)
        )

    def test_403_response(self, mocked_request):
        with self.assertRaises(PluginException) as exception:
            self.action.run(Util.load_json("inputs/find_groups_403.json.exp"))
        self.assertEqual(exception.exception.cause, ConnectionTestException.causes.get(PluginException.Preset.API_KEY))
        self.assertEqual(
            exception.exception.assistance, ConnectionTestException.assistances.get(PluginException.Preset.API_KEY)
        )

    def test_404_response(self, mocked_request):
        with self.assertRaises(PluginException) as exception:
            self.action.run(Util.load_json("inputs/find_groups_404.json.exp"))
        self.assertEqual(
            exception.exception.cause, ConnectionTestException.causes.get(PluginException.Preset.NOT_FOUND)
        )
        self.assertEqual(
            exception.exception.assistance, ConnectionTestException.assistances.get(PluginException.Preset.NOT_FOUND)
        )
