import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_rapid7_insightcloudsec.actions.run_bot_on_demand import RunBotOnDemand
from icon_rapid7_insightcloudsec.actions.run_bot_on_demand.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests)
class TestRunBotOnDemand(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(RunBotOnDemand())

    @parameterized.expand(Util.load_parameters("run_bot_on_demand").get("parameters"))
    def test_run_bot_on_demand(self, mock_request, name, bot_id, expected):
        actual = self.action.run({Input.BOTID: bot_id})
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("run_bot_on_demand_bad").get("parameters"))
    def test_run_bot_on_demand_bad(self, mock_request, name, bot_id, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.BOTID: bot_id})
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
