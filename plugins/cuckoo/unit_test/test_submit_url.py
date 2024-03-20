import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_cuckoo.actions.submit_url import SubmitUrl
from komand_cuckoo.actions.submit_url.schema import SubmitUrlOutput
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from jsonschema import validate


class TestSubmitUrl(TestCase):
  @classmethod
  def setUpClass(cls) -> None:
    cls.action = Util.default_connector(SubmitUrl())

  @parameterized.expand(
    [
      [
        "Success",
        Util.read_file_to_dict("input/submit_url_success.json.inp"),
        Util.read_file_to_dict("expected/submit_url_success.json.exp"),
      ],
    ]
  )
  @patch("requests.request", side_effect=Util.mock_request)
  def test_submit_url(self, test_name, input, expected, mock_request):
    actual = self.action.run(input)
    self.assertEqual(expected, actual)
    validate(actual, SubmitUrlOutput.schema)
