import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized

from util import Util
from icon_powershell.actions.powershell_string import PowershellString


class TestPowershellString(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.params = {
            "address": "10.0.1.11",
            "host_name": "windows",
            "script": "Get-Date",
        }

    @parameterized.expand(
        [
            ("ntlm", "inputs/ntlm_connection.json.resp", "expecteds/ntlm_connection.json.resp"),
            ("cred_ssp", "inputs/credssp_connection.json.resp", "expecteds/credssp_connection.json.resp"),
        ]
    )
    @patch("icon_powershell.util.util.FixWinrmSession", side_effect=Util.mock_powershell)
    def test_powershell_string_ntlm_credssp(self, name: str, input_path: str, expected_path: str, mock_powershell):
        params = Util.read_file_to_dict(input_path)
        action = Util.default_connector(PowershellString(), params)
        actual = action.run(params=self.params)
        expected = Util.read_file_to_dict(expected_path)
        self.assertEqual(actual, expected)

    @patch("subprocess.Popen", side_effect=Util.mock_powershell)
    def test_powershell_string_local(self, mock_powershell):
        params = Util.read_file_to_dict("inputs/local_connection.json.resp")
        action = Util.default_connector(PowershellString(), params)
        actual = action.run(params=self.params)
        expected = Util.read_file_to_dict("expecteds/local_connection.json.resp")
        self.assertEqual(actual, expected)

    @patch("icon_powershell.util.util.FixWinrmSession", side_effect=Util.mock_powershell)
    @patch("icon_powershell.util.util.configure_machine_for_kerberos_connection")
    def test_powershell_string_kerberos(self, mock_configure_kerberos, mock_powershell):
        params = Util.read_file_to_dict("inputs/kerberos_connection.json.resp")
        action = Util.default_connector(PowershellString(), params)
        actual = action.run(params=self.params)
        expected = Util.read_file_to_dict("expecteds/kerberos_connection.json.resp")
        self.assertEqual(actual, expected)
