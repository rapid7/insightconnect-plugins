import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from jsonschema import validate
from komand_rapid7_insightidr.actions.close_investigations_in_bulk import CloseInvestigationsInBulk
from komand_rapid7_insightidr.actions.close_investigations_in_bulk.schema import (
    CloseInvestigationsInBulkInput,
    CloseInvestigationsInBulkOutput,
    Input,
)
from komand_rapid7_insightidr.connection.schema import Input as ConnectionInput

from util import Util


@patch("requests.Session.send", side_effect=Util.mocked_requests)
class TestCloseInvestigationsInBulk(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.params = {
            Input.ALERT_TYPE: "Account Created",
            Input.DATETIME_FROM: "2018-07-01 00:00:00 00:00",
            Input.DATETIME_FROM: "2018-07-01 00:00:00 00:00",
            Input.MAX_INVESTIGATIONS_TO_CLOSE: 10,
            Input.SOURCE: "MANUAL",
        }
        cls.connection_params = {
            ConnectionInput.REGION: "United States 1",
            ConnectionInput.API_KEY: {"secretKey": "api_key"},
        }

    def setUp(self) -> None:
        self.action = Util.default_connector(CloseInvestigationsInBulk())
        self.connection = self.action.connection

    def test_close_investigations_in_bulk(self, _mock_req) -> None:
        validate(self.params, CloseInvestigationsInBulkInput.schema)
        actual = self.action.run(self.params)
        expected = {"ids": ["6c7db8d1-abc5-b9da-dd71-1a3ffffe8a16"], "num_closed": 10}
        self.assertEqual(actual, expected)
        validate(actual, CloseInvestigationsInBulkOutput.schema)
