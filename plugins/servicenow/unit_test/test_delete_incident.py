import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_servicenow.connection.connection import Connection
from icon_servicenow.actions.delete_incident import DeleteIncident
import json
import logging


class TestDeleteIncident(TestCase):
    def test_delete_incident(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        pass
