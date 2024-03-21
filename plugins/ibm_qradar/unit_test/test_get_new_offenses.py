import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from unittest import TestCase
from jsonschema import validate

from insightconnect_plugin_runtime.exceptions import PluginException
from icon_ibm_qradar.triggers.get_new_offense.trigger import GetNewOffense
from icon_ibm_qradar.triggers.get_new_offense.schema import Input, GetNewOffenseInput
from helpers.offense import OffensesHelper


class TestGetNewOffense(TestCase):
    """Test case class for trigger : get new offense."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up an action for test."""
        cls.action = OffensesHelper.default_connector(GetNewOffense())

    @patch("requests.request", side_effect=OffensesHelper.mock_request)
    def test_get_offenses_with_invalid_range(self, make_request):
        """To get offenses with given invalid range.

        :return: None
        """
        action_params = {Input.RANGE: "-1-2", Input.INTERVAL: 30}
        validate(action_params, GetNewOffenseInput.schema)
        with self.assertRaises(PluginException):
            self.action.run(action_params)

    @patch("requests.request", side_effect=OffensesHelper.mock_request)
    def test_with_internal_server_error(self, make_request):
        """To test the get offense with internalServerError."""
        action_params = {Input.FILTER: "internalServerError", Input.INTERVAL: 30}
        validate(action_params, GetNewOffenseInput.schema)
        with self.assertRaises(PluginException):
            self.action.run(action_params)
