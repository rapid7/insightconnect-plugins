from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_typo_squatter.actions.check_for_squatters import CheckForSquatters
from komand_typo_squatter.actions.check_for_squatters.schema import Input, Output
from parameterized import parameterized

from unit_test.util import Util


@patch("subprocess.run", side_effect=Util.mocked_run)
class TestCheckForSquatters(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = CheckForSquatters()

    @parameterized.expand(Util.load_parameters("check_for_squatters_parameters").get("parameters"))
    def test_check_for_squatters(
        self, mock_run: MagicMock, name: str, domain: str, flag: str, expected: Dict[str, Any]
    ) -> None:
        actual = self.action.run({Input.DOMAIN: domain, Input.FLAG: flag})
        expected = {Output.POTENTIAL_SQUATTERS: expected}
        self.assertEqual(actual, expected)

    def test_check_for_squatters_invalid_domain(self, mock_run: MagicMock) -> None:
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.DOMAIN: "rapid7"})
        self.assertEqual(error.exception.cause, "Invalid domain provided.")
        self.assertEqual(error.exception.assistance, "Please provide a valid domain and try again.")

    def test_check_for_squatters_invalid_flag(self, mock_run: MagicMock) -> None:
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.DOMAIN: "rapid7.com", Input.FLAG: "--invalid_flag"})
        self.assertEqual(error.exception.cause, "Invalid flag provided.")
        self.assertEqual(error.exception.assistance, "Please provide a valid flag and try again.")
        self.assertEqual(
            error.exception.data,
            "usage: /usr/local/bin/dnstwist [OPTION]... DOMAIN\ndnstwist: error: unrecognized arguments: --invalid_flag"
            "\n",
        )
