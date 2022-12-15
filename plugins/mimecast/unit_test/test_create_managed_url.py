import json
import os
import sys
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))
from komand_mimecast.actions import CreateManagedUrl
from komand_mimecast.util.constants import BASIC_ASSISTANCE_MESSAGE, ERROR_CASES, MANAGED_URL_EXISTS_ERROR

from unit_test.util import Util


@patch("requests.request", side_effect=Util.mocked_request)
class TestCreateManagedURl(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateManagedUrl())

    def test_create_managed_url(self, mocked_request):
        actual = self.action.run(Util.load_json("inputs/create_managed_url.json.exp"))
        expect = Util.load_json("expected/create_managed_url.json.exp")
        self.assertEqual(expect, actual)

    def test_bad_create_managed_url(self, mocked_request):
        with self.assertRaises(PluginException) as exception:
            self.action.run(Util.load_json("inputs/create_managed_url_bad.json.exp"))
        self.assertEqual(exception.exception.cause, ERROR_CASES.get(MANAGED_URL_EXISTS_ERROR))
        self.assertEqual(exception.exception.assistance, BASIC_ASSISTANCE_MESSAGE)
