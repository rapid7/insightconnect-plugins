import os
import sys
from jsonschema import validate
from unittest import TestCase
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_mimecast.actions import DeleteManagedUrl
from komand_mimecast.actions.delete_managed_url.schema import DeleteManagedUrlOutput, DeleteManagedUrlInput
from komand_mimecast.util.constants import BASIC_ASSISTANCE_MESSAGE, ERROR_CASES, MANAGED_URL_NOT_FOUND_ERROR

from util import EXPIRED_ACCESS_TOKEN, Util


@patch("requests.request", side_effect=Util.mocked_request)
class TestDeleteManagedURl(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DeleteManagedUrl())

    def test_delete_managed_url(self, _mocked_request):
        input_data = Util.load_json("inputs/delete_managed_url.json.exp")
        validate(input_data, DeleteManagedUrlInput.schema)
        actual = self.action.run(input_data)
        expect = Util.load_json("expected/delete_managed_url.json.exp")
        self.assertEqual(expect, actual)
        validate(actual, DeleteManagedUrlOutput.schema)

    def test_bad_delete_managed_url(self, _mocked_request):
        with self.assertRaises(PluginException) as exception:
            self.action.run(Util.load_json("inputs/delete_managed_url_bad.json.exp"))
        self.assertEqual(exception.exception.cause, ERROR_CASES.get(MANAGED_URL_NOT_FOUND_ERROR))
        self.assertEqual(exception.exception.assistance, BASIC_ASSISTANCE_MESSAGE)

    def test_delete_managed_url_token_expired(self, mocked_request):
        # The stored token is expired so the action re-authenticates and retries the call
        self.action.connection.client.access_token = EXPIRED_ACCESS_TOKEN
        actual = self.action.run(Util.load_json("inputs/delete_managed_url.json.exp"))
        self.assertEqual(Util.load_json("expected/delete_managed_url.json.exp"), actual)
        self.assertEqual(mocked_request.call_count, 3)
        validate(actual, DeleteManagedUrlOutput.schema)
