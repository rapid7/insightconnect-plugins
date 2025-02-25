import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_servicenow.connection.connection import Connection
from icon_servicenow.actions.search_incident_attachment import SearchIncidentAttachment
import json
import logging


class TestSearchIncidentAttachment(TestCase):
    def test_search_incident_attachment(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        pass
