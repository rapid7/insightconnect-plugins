import os
import sys
from unittest.mock import patch

from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_ibm_qradar.triggers.get_new_offense import GetNewOffense
from unit_test.helpers.offense import OffensesHelper

sys.path.append(os.path.abspath("../"))


class TestGetNewOffense(TestCase):
    """Test case class for trigger : get new offense."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up an action for test."""
        cls.action = OffensesHelper.default_connector(GetNewOffense())

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_get_offenses_with_invalid_range(self, make_request):
        """To get offenses with given invalid range.

        :return: None
        """
        action_params = {"range": "-1-2"}
        with self.assertRaises(PluginException):
            self.action.run(action_params)

    @patch("requests.get", side_effect=OffensesHelper.mock_request)
    def test_with_internal_server_error(self, make_request):
        """To test the get offense with internalServerError."""
        action_params = {"filter": "internalServerError"}
        with self.assertRaises(PluginException):
            self.action.run(action_params)
