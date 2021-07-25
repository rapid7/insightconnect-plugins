import sys
import os
from unittest import TestCase
from unittest.mock import patch
from unit_test.util import Util
from komand_elasticsearch.actions import ClusterHealth

sys.path.append(os.path.abspath("../"))


class TestClusterHealth(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(ClusterHealth())

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_get_messages_from_user(self, mock_request):
        actual = self.action.run()
        expected = {
            "cluster_health": {
                "cluster_name": "cluster_name",
                "status": "green",
                "timed_out": False,
                "number_of_nodes": 1,
                "number_of_data_nodes": 1,
                "active_primary_shards": 90,
                "active_shards": 1,
                "relocating_shards": 0,
                "initializing_shards": 0,
                "unassigned_shards": 0,
                "delayed_unassigned_shards": 0,
                "number_of_pending_tasks": 0,
                "number_of_in_flight_fetch": 0,
                "task_max_waiting_in_queue_millis": 0,
                "active_shards_percent_as_number": 100,
            }
        }
        self.assertEqual(actual, expected)
