import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_joe_sandbox.actions.get_account_info import GetAccountInfo
from icon_joe_sandbox.actions.get_account_info.schema import Input, Output
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request


class TestGetAccountInfo(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(GetAccountInfo())
        self.params = {}

    def test_get_account_info(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
