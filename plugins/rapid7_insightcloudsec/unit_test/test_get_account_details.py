import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_rapid7_insightcloudsec.actions.get_account_details import GetAccountDetails
from icon_rapid7_insightcloudsec.actions.get_account_details.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests)
class TestGetAccountDetails(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAccountDetails())

    @parameterized.expand(Util.load_parameters("get_account_details").get("parameters"))
    def test_get_account_details(self, mock_request, name, account_id, expected):
        actual = self.action.run({Input.ACCOUNTID: account_id})
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("get_account_details_bad").get("parameters"))
    def test_get_account_details_bad(self, mock_request, name, account_id, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.ACCOUNTID: account_id})
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
