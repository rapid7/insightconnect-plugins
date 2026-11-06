import os
import sys
from unittest import TestCase
from unittest.mock import Mock, patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

sys.path.append(os.path.abspath("../"))

from komand_mimecast.actions import FindGroups
from komand_mimecast.util.constants import API

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
        self.assertEqual(
            exception.exception.cause, ConnectionTestException.causes.get(PluginException.Preset.UNAUTHORIZED)
        )
        self.assertEqual(
            exception.exception.assistance, ConnectionTestException.assistances.get(PluginException.Preset.UNAUTHORIZED)
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

    def test_token_expired_twice(self, mocked_request):
        token_expired = Mock(
            status_code=200, **{"json.return_value": Util.load_json("responses/token_expired.json.resp")}
        )

        # Expired token, re-authenticate, and the retried call is expired again
        mocked_request.side_effect = [
            token_expired,
            Util.mocked_request(url=f"{API}/oauth/token"),
            token_expired,
        ]

        # This should fail with a PluginException
        with self.assertRaises(PluginException) as exception:
            self.action.run(Util.load_json("inputs/find_groups.json.exp"))

        # Verify the exception data and that the plugin retried only once
        self.assertEqual(exception.exception.cause, PluginException.causes[PluginException.Preset.API_KEY])
        self.assertEqual(mocked_request.call_count, 3)

    def test_token_expired_on_login(self, mocked_request):
        # Return the same expired response for each call, including the login call
        mocked_request.side_effect = None
        mocked_request.return_value = Mock(
            status_code=200, **{"json.return_value": Util.load_json("responses/token_expired.json.resp")}
        )

        # This should fail with a PluginException
        with self.assertRaises(PluginException) as exception:
            Util.default_connector(FindGroups())

        # Verify the exception data and that the login was not retried
        self.assertEqual(exception.exception.cause, PluginException.causes[PluginException.Preset.API_KEY])
        self.assertEqual(mocked_request.call_count, 1)
