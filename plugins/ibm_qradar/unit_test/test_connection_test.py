import os
import sys
from unittest import TestCase

from icon_ibm_qradar.connection import Connection

sys.path.append(os.path.abspath("../"))


class TestConnection(TestCase):
    """Test QRadar Connection."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up an action for test."""
        cls.default_connection = Connection()

    def test_integration_connection_test(self):
        """To test the integration connection with qradar."""
        params = {
            "host_url": "http://hostname",
            "credentials": {"username": "user1", "password": "password"},
        }
        self.default_connection.test(params)
