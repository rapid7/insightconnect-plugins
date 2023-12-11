import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_rapid7_insightidr.actions.get_alert_actors import GetAlertActors
from komand_rapid7_insightidr.actions.get_alert_actors.schema import (
    Input,
    GetAlertActorsInput,
    GetAlertActorsOutput,
)
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate


@patch("requests.Session.request", side_effect=Util.mocked_requests)
class TestGetAlertActors(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAlertActors())

    @parameterized.expand(Util.load_parameters("get_alert_actors_minimum").get("parameters"))
    def test_get_alert_actors_minimum(self, mock_request, alert_rrn, expected):
        test_input = {Input.ALERT_RRN: alert_rrn}
        validate(test_input, GetAlertActorsInput.schema)
        actual = self.action.run(test_input)
        self.assertEqual(actual, expected)
        validate(actual, GetAlertActorsOutput.schema)

    @parameterized.expand(Util.load_parameters("get_alert_actors").get("parameters"))
    def ttest_get_alert_actors(self, mock_request, alert_rrn, size, index, expected):
        test_input = {Input.ALERT_RRN: alert_rrn, Input.SIZE: size, Input.INDEX: index}
        validate(test_input, GetAlertActorsInput.schema)
        actual = self.action.run(test_input)
        self.assertEqual(actual, expected)
        validate(actual, GetAlertActorsOutput.schema)

    @parameterized.expand(Util.load_parameters("get_alert_actors_not_found").get("parameters"))
    def test_get_alert_actors_bad(self, mock_request, alert_rrn, cause, assistance):
        test_input = {Input.ALERT_RRN: alert_rrn}
        validate(test_input, GetAlertActorsInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(test_input)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
