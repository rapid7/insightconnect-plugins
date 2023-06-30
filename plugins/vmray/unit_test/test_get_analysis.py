import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_vmray.actions.get_analysis import GetAnalysis
from util import Util
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException
from unittest import mock
import logging


class TestGetAnalysis(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAnalysis())

    @parameterized.expand(Util.load_data("get_analysis", "expected").get("parameters"))
    @mock.patch("requests.Session.send", side_effect=Util.mocked_requests)
    def test_get_analysis_unit(self, name, _input, expected, mock_request):
        logging.basicConfig(level=logging.INFO)
        result = self.action.run(_input)
        self.assertEqual(expected, result)

    @parameterized.expand(Util.load_data("get_analysis_errors", "expected").get("parameters"))
    @mock.patch("requests.Session.send", side_effect=Util.mocked_requests)
    def test_get_analysis_unit_errors(self, name, _input, expected, mock_request):
        with self.assertRaises(PluginException) as error:
            logging.basicConfig(level=logging.INFO)
            self.action.run(_input)
        self.assertEqual(expected["cause"], error.exception.cause)
        self.assertEqual(expected["assistance"], error.exception.assistance)
        self.assertEqual(expected["data"], error.exception.data)
