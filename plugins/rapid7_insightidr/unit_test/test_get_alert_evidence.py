import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_rapid7_insightidr.actions.get_alert_evidence import GetAlertEvidence
from komand_rapid7_insightidr.actions.get_alert_evidence.schema import (
    Input,
    GetAlertEvidenceInput,
    GetAlertEvidenceOutput,
)
from util import Util
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate


@patch("requests.Session.send", side_effect=Util.mocked_requests)
class TestGetAlertEvidences(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAlertEvidence())

    @parameterized.expand(Util.load_parameters("get_alert_evidence_minimum").get("parameters"))
    def test_get_alert_evidence_minimum(self, mock_request: MagicMock, alert_rrn: str, expected: dict) -> None:
        test_input = {Input.ALERT_RRN: alert_rrn}
        validate(test_input, GetAlertEvidenceInput.schema)
        actual = self.action.run(test_input)
        self.assertEqual(actual, expected)
        validate(actual, GetAlertEvidenceOutput.schema)

    @parameterized.expand(Util.load_parameters("get_alert_evidence").get("parameters"))
    def test_get_alert_evidence(
        self, mock_request: MagicMock, alert_rrn: str, size: int, index: int, expected: dict
    ) -> None:
        test_input = {Input.ALERT_RRN: alert_rrn, Input.SIZE: size, Input.INDEX: index}
        validate(test_input, GetAlertEvidenceInput.schema)
        actual = self.action.run(test_input)
        self.assertEqual(actual, expected)
        validate(actual, GetAlertEvidenceOutput.schema)

    @parameterized.expand(Util.load_parameters("get_alert_evidence_not_found").get("parameters"))
    def test_get_alert_evidence_bad(self, mock_request: MagicMock, alert_rrn: str, cause: str, assistance: str) -> None:
        test_input = {Input.ALERT_RRN: alert_rrn}
        validate(test_input, GetAlertEvidenceInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(test_input)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
