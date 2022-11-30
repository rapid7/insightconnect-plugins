from typing import Any, Dict, List
from unittest import mock

import nmap


class MockedPortScanner:
    """Mocked PortScanner class from nmap dependency."""

    def __init__(self, hosts: List[str], scanned_hosts: Dict[str, str]) -> None:
        self._scanned_hosts = scanned_hosts
        self.hosts = hosts

    def __getitem__(self, item: str) -> Any:
        return self._scanned_hosts.get(item, "")

    def scan(self, *args, **kwargs) -> None:
        return None

    def all_hosts(self) -> List[str]:
        return self.hosts


def mocked_port_scanner(*args, **kwargs):
    mocked_object = nmap
    mocked_object.nmap.PortScanner.__new__ = mock.Mock(return_value=MockedPortScanner(*args, **kwargs))
