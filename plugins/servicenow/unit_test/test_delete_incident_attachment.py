import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_servicenow.connection.connection import Connection
from icon_servicenow.actions.delete_incident_attachment import DeleteIncidentAttachment
import json
import logging


class TestDeleteIncidentAttachment(TestCase):
    def test_delete_incident_attachment(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        pass
