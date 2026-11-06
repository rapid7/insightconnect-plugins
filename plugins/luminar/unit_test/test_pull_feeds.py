import json
import os
import sys
import unittest
from unittest import mock

sys.path.append(os.path.abspath("../"))

from icon_luminar.util.utils import pull_feeds


class ReadJSONFile:
    @staticmethod
    def load_response(file_name: str):
        file_path = os.path.join(os.path.dirname(__file__), f"responses/{file_name}")
        with open(file_path, "r") as f:
            return json.load(f)


class TestPullFeeds(unittest.TestCase):
    def setUp(self):
        self.mock_logger = mock.Mock()
        self.mock_client = mock.Mock()

        # mock TAXII collections
        self.mock_client.get_taxi_collections.return_value = {
            "cyberfeeds": "collection-123",
            "leakedrecords": "collection-456",
            "iocs": "collection-789",
        }

    def test_pull_feeds_returns_associations(self):

        for file_name, feed_name in [
            ("cyberfeeds.json.resp", "cyberfeeds"),
            ("iocs.json.resp", "iocs"),
            ("leakedrecords.json.resp", "leakedrecords"),
        ]:
            data = ReadJSONFile.load_response(file_name)
            self.assertIsInstance(data, list)

            # patch the API call for collection objects
            self.mock_client.get_collection_objects.return_value = data
            from_date = "2025-09-10T00:00:00.000000Z"
            result = pull_feeds(
                self.mock_client, feed_name, from_date, self.mock_logger
            )

            # Now `result` should be whatever `create_associations` produces.
            # Typically it's a list of enriched records with "associations" key.
            self.assertIsInstance(result, list)

            # Each record should now have associations
            for record in result:
                if record["type"] == "report":
                    if record.get("object_refs"):
                        self.assertIn("ref_objects", record)
                else:
                    self.assertIn("related_obj", record)
