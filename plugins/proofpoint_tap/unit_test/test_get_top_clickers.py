import sys
import os

from unittest.mock import patch
from komand_proofpoint_tap.actions.get_top_clickers import GetTopClickers
from komand_proofpoint_tap.actions.get_top_clickers.schema import Input
from unit_test.test_util import Util
from unittest import TestCase

sys.path.append(os.path.abspath("../"))


class TestGetTopClickers(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetTopClickers())

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_get_top_clickers(self, mock_request):
        actual = self.action.run({Input.WINDOW: 14})
        expected = {
            "results": {
                "interval": "2021-01-23T15:45:00Z/2021-04-23T15:45:00Z",
                "totalTopClickers": 5,
                "users": [
                    {
                        "clickStatistics": {"families": [{"clicks": 28, "name": "Malware"}], "clickCount": 28},
                        "identity": {
                            "emails": ["user@example.com"],
                            "guid": "9ec73de-5100-26ef-4935-579c6b872d35",
                            "vip": False,
                        },
                    }
                ],
            }
        }
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_get_top_clickers2(self, mock_request):
        actual = self.action.run({Input.WINDOW: 30})
        expected = {
            "results": {
                "interval": "2021-01-23T15:45:00Z/2021-04-23T15:45:00Z",
                "totalTopClickers": 5,
                "users": [
                    {
                        "clickStatistics": {"families": [{"clicks": 28, "name": "Malware"}], "clickCount": 28},
                        "identity": {
                            "emails": ["user@example.com"],
                            "guid": "9ec73de-5100-26ef-4935-579c6b872d35",
                            "vip": False,
                        },
                    }
                ],
            }
        }
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_get_top_clickers3(self, mock_request):
        actual = self.action.run({Input.WINDOW: 90})
        expected = {
            "results": {
                "interval": "2021-01-23T15:45:00Z/2021-04-23T15:45:00Z",
                "totalTopClickers": 5,
                "users": [
                    {
                        "clickStatistics": {"families": [{"clicks": 28, "name": "Malware"}], "clickCount": 28},
                        "identity": {
                            "emails": ["user@example.com"],
                            "guid": "9ec73de-5100-26ef-4935-579c6b872d35",
                            "vip": False,
                        },
                    }
                ],
            }
        }
        self.assertEqual(actual, expected)
