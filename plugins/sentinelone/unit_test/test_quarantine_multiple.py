import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import Mock, patch

from komand_sentinelone.actions.quarantine_multiple import QuarantineMultiple
from komand_sentinelone.actions.quarantine_multiple.schema import Input, Output

from util import Util


class TestQuarantineMultiple(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request: Mock) -> None:
        cls.action = Util.default_connector(QuarantineMultiple())

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    @patch("requests.get", side_effect=Util.mocked_requests_get)
    def test_should_succeed(self, mock_request: Mock, mock_get: Mock) -> None:
        expected = {
            Output.COMPLETED: ["hostname123", "hostname456", "hostname789"],
            Output.FAILED: [],
        }
        actual = self.action.run(
            {Input.AGENTS: ["hostname123", "hostname456", "hostname789"], Input.QUARANTINE_STATE: True}
        )
        self.assertEqual(expected, actual)
