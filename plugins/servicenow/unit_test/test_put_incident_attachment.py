import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_servicenow.connection.connection import Connection
from icon_servicenow.actions.put_incident_attachment import PutIncidentAttachment
import json
import logging


class TestPutIncidentAttachment(TestCase):
    def test_put_incident_attachment(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        pass
