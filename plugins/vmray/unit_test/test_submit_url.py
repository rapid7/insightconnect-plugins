import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_vmray.actions.submit_url import SubmitUrl
from util import Util
from parameterized import parameterized
from unittest import mock
import logging


class TestSubmitUrl(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(SubmitUrl())

    @parameterized.expand(Util.load_data("submit_url", "expected").get("parameters"))
    @mock.patch("requests.Session.send", side_effect=Util.mocked_requests)
    def test_submit_url_unit(self, name, _input, expected, mock_request):
        logging.basicConfig(level=logging.INFO)
        result = self.action.run(_input)
        self.assertEqual(expected, result)
