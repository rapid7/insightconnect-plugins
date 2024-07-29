import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch
from komand_netmiko.actions.configuration_commands import ConfigurationCommands
from komand_netmiko.actions.configuration_commands.schema import Input, Output


class TestConfigurationCommands(TestCase):
    def setUp(self):
        self.action = ConfigurationCommands()
        self.action.connection = MagicMock()
        self.action.logger = MagicMock()
        self.mock_client = MagicMock()
        self.action.connection.client = self.mock_client

        self.params = {Input.COMMAND: "dadada", Input.HOST: "dadada"}

    @patch("komand_netmiko.connection.connection.Connection")
    def test_configuration_commands_success(self, mock_connection):
        mock_connection.client = self.mock_client
        self.mock_client().send_config_set.return_value = {
            "results": "sudo -s\nroot@buster:/home/vagrant# ls -la\ntotal 125088\ndrwxr-xr-x  9 vagrant vagrant      4096 Mar 31 19:24 .\ndrwxr-xr-x  3 root    root         4096 May 10  2020 ..\n-rw-------  1 vagrant vagrant     74883 Mar 31 19:24 .bash_history\n-rw-r--r--  1 vagrant vagrant       220 May 10  2020 .bash_logout\n-rw-r--r--  1 vagrant vagrant      3685 Sep 20  2020 .bashrc\ndrwxr-xr-x  6 vagrant vagrant      4096 Sep 20  2020 .cache\ndrwxr-xr-x  4 vagrant vagrant      4096 Sep 16  2020 .gem\n-rw-r--r--  1 vagrant vagrant        24 Sep 20  2020 .gitconfig\ndrwx------  3 vagrant vagrant      4096 Sep 16  2020 .gnupg\ndrwxr-xr-x 10 root    root         4096 May  6  2019 go\n-rw-r--r--  1 root    root    127938445 Sep 16  2020 go1.12.5.linux-amd64.tar.gz\ndrwxr-xr-x  4 vagrant vagrant      4096 Sep 20  2020 go_work\ndrwx------  4 vagrant vagrant      4096 Nov 25 00:51 .local\n-rw-r--r--  1 vagrant vagrant       807 May 10  2020 .profile\ndrwx------  2 vagrant vagrant      4096 Nov  2 16:16 .ssh\n-rw-------  1 vagrant vagrant     19449 Mar 23 20:33 .viminfo\nroot@buster:/home/vagrant# "
        }
        result = self.action.run(self.params)
        expected_response = {
            "results": {
                "results": "sudo -s\nroot@buster:/home/vagrant# ls -la\ntotal 125088\ndrwxr-xr-x  9 vagrant vagrant      4096 Mar 31 19:24 .\ndrwxr-xr-x  3 root    root         4096 May 10  2020 ..\n-rw-------  1 vagrant vagrant     74883 Mar 31 19:24 .bash_history\n-rw-r--r--  1 vagrant vagrant       220 May 10  2020 .bash_logout\n-rw-r--r--  1 vagrant vagrant      3685 Sep 20  2020 .bashrc\ndrwxr-xr-x  6 vagrant vagrant      4096 Sep 20  2020 .cache\ndrwxr-xr-x  4 vagrant vagrant      4096 Sep 16  2020 .gem\n-rw-r--r--  1 vagrant vagrant        24 Sep 20  2020 .gitconfig\ndrwx------  3 vagrant vagrant      4096 Sep 16  2020 .gnupg\ndrwxr-xr-x 10 root    root         4096 May  6  2019 go\n-rw-r--r--  1 root    root    127938445 Sep 16  2020 go1.12.5.linux-amd64.tar.gz\ndrwxr-xr-x  4 vagrant vagrant      4096 Sep 20  2020 go_work\ndrwx------  4 vagrant vagrant      4096 Nov 25 00:51 .local\n-rw-r--r--  1 vagrant vagrant       807 May 10  2020 .profile\ndrwx------  2 vagrant vagrant      4096 Nov  2 16:16 .ssh\n-rw-------  1 vagrant vagrant     19449 Mar 23 20:33 .viminfo\nroot@buster:/home/vagrant# "
            }
        }

        self.assertEqual(result, expected_response)
