import os
import sys

sys.path.append(os.path.abspath("../"))
import logging
from typing import Dict, List
from unittest import TestCase
from komand_nmap.actions.scan import Scan
from komand_nmap.connection.connection import Connection
from parameterized import parameterized
from unit_test.mock import mocked_port_scanner


class TestScan(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect({})

        self.action = Scan()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")
        self.payload = {"arguments": "-A", "hosts": "socutil01", "ports": "", "sudo": True}

    @parameterized.expand([(["test"], {"test": "192.168.0.1"}, {"result": ["192.168.0.1"]})])
    def test_scan(self, hosts: List[str], scanned_hosts: Dict[str, str], result: str) -> None:
        mocked_port_scanner(hosts, scanned_hosts)
        response = self.action.run(self.payload)
        assert response == result
