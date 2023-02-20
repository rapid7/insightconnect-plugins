import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_ivanti_service_manager.connection.connection import Connection
from icon_ivanti_service_manager.actions.delete_incident import DeleteIncident
import json
import logging


class TestDeleteIncident(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # Setting up things
        pass

    def test_delete_incident_success(self):
        actual = "Insert here"
        expected = "Insert here"
        self.assertEqual(actual, expected)

    def test_delete_incident_fail(self):
        actual = "Insert here"
        expected = "Insert here"
        self.assertEqual(actual, expected)
