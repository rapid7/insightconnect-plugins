import sys
import os
import json
import tempfile

sys.path.append(os.path.abspath("../komand_rapid7_metasploit/"))

from unittest import TestCase
from komand_rapid7_metasploit.triggers.new_modules import NewModules
from komand_rapid7_metasploit.connection import Connection
import logging
import insightconnect_plugin_runtime
from tempfile import TemporaryFile
from unittest.mock import MagicMock
from unittest.mock import mock_open, patch


class TestNewModules(TestCase):
    def test_integration_new_modules(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_trigger = NewModules()
        data = "linux/misc/saltstack_salt_unauth_rce"
        m_open = mock_open(read_data=data)
        try:
            with open("../tests/new_modules.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
        except Exception as e:
            message = "Missing json file"
            self.fail(message)

        # This is not a common test- but due to needing the cache file this is the workaround currently used
        with patch("insightconnect_plugin_runtime.helper.open_cachefile", m_open):
            test_conn.logger = log
            test_trigger.logger = log
            test_conn.connect(connection_params)
            test_trigger.connection = test_conn
            results = test_trigger.run()
            self.assertIsNotNone(results)
            test_conn.client.close()
        os.remove("tempFile")
