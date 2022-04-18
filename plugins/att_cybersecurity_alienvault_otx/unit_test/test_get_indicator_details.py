import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_att_cybersecurity_alienvault_otx.actions.get_indicator_details import GetIndicatorDetails
from komand_att_cybersecurity_alienvault_otx.actions.get_indicator_details.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
class TestGetIndicatorDetails(TestCase):
    @parameterized.expand(Util.load_parameters("get_indicator_details").get("parameters"))
    def test_get_indicator_details(self, mock_request, name, indicator_type, indicator, section, expected):
        action = Util.default_connector(GetIndicatorDetails())
        actual = action.run({Input.INDICATOR_TYPE: indicator_type, Input.INDICATOR: indicator, Input.SECTION: section})
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("get_indicator_details_bad").get("parameters"))
    def test_get_indicator_details_bad(self, mock_request, name, indicator_type, indicator, section, cause, assistance):
        with self.assertRaises(PluginException) as error:
            action = Util.default_connector(GetIndicatorDetails())
            action.run({Input.INDICATOR_TYPE: indicator_type, Input.INDICATOR: indicator, Input.SECTION: section})
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
