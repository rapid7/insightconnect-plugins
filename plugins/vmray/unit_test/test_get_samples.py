import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_vmray.actions.get_samples import GetSamples
from util import Util
from parameterized import parameterized
from unittest import mock
import logging


class TestGetSamples(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetSamples())

    @parameterized.expand(Util.load_data("get_samples", "expected").get("parameters"))
    @mock.patch("requests.Session.send", side_effect=Util.mocked_requests)
    def test_get_samples_unit(self, name, _input, expected, mock_request):
        logging.basicConfig(level=logging.INFO)
        result = self.action.run(_input)
        self.assertEqual(expected, result)
