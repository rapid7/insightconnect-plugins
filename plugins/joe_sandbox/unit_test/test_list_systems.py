import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_joe_sandbox.actions.list_systems import ListSystems
from icon_joe_sandbox.actions.list_systems.schema import Input, Output
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request


class TestListSystems(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(ListSystems())
        self.params = {}

    def test_list_systems(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
