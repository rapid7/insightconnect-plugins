import sys
import os
from parameterized import parameterized
from unittest import TestCase, mock

sys.path.append(os.path.abspath("../"))

from komand_snortlabslist.actions.lookup import Lookup


class TestLookup(TestCase):
    def setUp(self):
        self.action = Lookup()
        self.mock_get_patcher = mock.patch("requests.get")
        self.mock_get = self.mock_get_patcher.start()
        self.addCleanup(self.mock_get_patcher.stop)

    def mock_response(self, addresses):
        mock_response = self.mock_get.return_value
        mock_response.text = "\n".join(addresses) + "\n"

    @parameterized.expand(
        [("found", ["1.2.3.4", "5.6.7.8"], "1.2.3.4", True), ("not_found", ["1.2.3.4", "5.6.7.8"], "9.10.11.12", False)]
    )
    def test_run(self, name, response_addresses, test_address, expected_found):
        self.mock_response(response_addresses)
        params = {"address": test_address}

        result = self.action.run(params)

        self.assertEqual(result["found"], expected_found)
        self.assertEqual(result["address"], test_address)
        self.assertEqual(result["status"], "No Error")
