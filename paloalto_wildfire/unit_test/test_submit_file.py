from unittest import TestCase
from komand_paloalto_wildfire.actions import SubmitFile
from komand_paloalto_wildfire.connection import Connection
import json
import logging

class TestSubmitFile(TestCase):
    def test_submit_file_unsupported_type(self):
        # Live test - uncomment and use icon-lab set to run
        log = logging.getLogger("Test")
        sf = SubmitFile()
        conn = Connection()

        sf.logger = log
        conn.logger = log

        with open("../tests/submit_file.json") as file:
            data = json.load(file)
            connection_params = data.get("body").get("connection")

        conn.connect(connection_params)
        sf.connection = conn

        action_params = {
            "filename": "EICAR.txt",
            "file": "WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy1URVNULUZJTEUhJEgrSCo="
        }

        actual = sf.run(action_params)

        expected = {'submission': {'supported_file_type': False, 'filename': 'Unknown', 'url': 'Unknown'}}
        self.assertEqual(actual, expected)
        pass

