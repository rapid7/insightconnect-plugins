import sys
import os
import time

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from util import Util
from icon_rapid7_intsights.actions.enrich_indicator import EnrichIndicator
from icon_rapid7_intsights.actions.enrich_indicator.schema import Input, EnrichIndicatorInput, EnrichIndicatorOutput
from jsonschema import validate


class TestEnrichIndicator(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mock_request)
    def setUpClass(cls, mock_request) -> None:
        Util.request_count = 0
        cls.action = Util.default_connector(EnrichIndicator())

    @patch("requests.request", side_effect=Util.mock_request)
    def test_enrich_indicator_should_success(self, make_request):
        input_params = {Input.INDICATOR_VALUE: "rapid7.com"}
        validate(input_params, EnrichIndicatorInput.schema)
        Util.request_count = 1
        actual = self.action.run(input_params)
        Util.request_count = 0
        expected = {"data": {}, "original_value": "rapid7.com", "status": "Done"}
        self.assertEqual(expected, actual)
        validate(actual, EnrichIndicatorOutput.schema)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_enrich_indicator_should_success_when_in_progress(self, make_request):
        input_params = {Input.INDICATOR_VALUE: "rapid7.com"}
        validate(input_params, EnrichIndicatorInput.schema)
        Util.request_count = 0
        time_start = time.time()
        actual = self.action.run(input_params)
        expected = 1
        expected_time_elapsed = time.time() - time_start
        self.assertEqual(expected, Util.request_count)
        self.assertTrue(expected_time_elapsed > 5)
        validate(actual, EnrichIndicatorOutput.schema)
