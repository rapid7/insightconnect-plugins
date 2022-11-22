import sys
import os
import json
import logging
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_nmap.connection.connection import Connection
from komand_nmap.actions.scan import Scan


class TestScan(TestCase):
    def test_scan(self):
        log = logging.getLogger("Test")
        test_action = Scan()
        test_action.logger = log

        working_params = {"input": {"arguments": "-A", "hosts": "socutil01", "ports": "", "sudo": True}}
        results = test_action.run(working_params)
        expected = {'body': {'log': 'rapid7/Nmap:1.0.3. Step name: scan\n', 'status': 'ok', 'meta': {}, 'output': {'result': []}}, 'version': 'v1', 'type': 'action_event'}
        self.assertNotEqual({}, results, "returns non - empty results")
        self.assertEqual(expected, results)

        """
        https://docs.google.com/document/d/1PifePDG1-mBcmNYE8dULwGxJimiRBrax5BIDG_0TFQI/edit?usp=sharing
        """

        self.fail("Unimplemented Test Case")