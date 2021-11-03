import sys
import os

from unittest import TestCase
from icon_cisco_asa.actions.get_blocked_hosts import GetBlockedHosts
from icon_cisco_asa.actions.get_blocked_hosts.schema import Output
from unit_test.util import Util
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))


class TestGetBlockedHosts(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetBlockedHosts())

    @patch("requests.request", side_effect=Util.mocked_requests)
    def test_get_blocked_hosts(self, mock_post):
        actual = self.action.run()

        expected = {
            Output.HOSTS: [
                {
                    "source_ip": "1.1.1.1",
                    "dest_ip": "2.2.2.2",
                    "source_port": "444",
                    "dest_port": "555",
                    "protocol": "6",
                },
                {
                    "source_ip": "3.3.3.3",
                    "dest_ip": "4.4.4.4",
                    "source_port": "333",
                    "dest_port": "444",
                    "protocol": "6",
                },
            ]
        }

        self.assertEqual(actual, expected)

    class Response:
        def __init__(self, text, status_code):
            self.status_code = status_code
            self.text = text

        def json(self):
            return self.text

    @patch("requests.request")
    def test_get_blocked_hosts_single_host(self, mock_post):
        text = {"response": ["shun (management) 1.1.1.1 2.2.2.2 444 555 6\n"]}
        mock_post.return_value = TestGetBlockedHosts.Response(text, 200)
        actual = self.action.run()

        expected = {
            Output.HOSTS: [
                {
                    "source_ip": "1.1.1.1",
                    "dest_ip": "2.2.2.2",
                    "source_port": "444",
                    "dest_port": "555",
                    "protocol": "6",
                }
            ]
        }

        self.assertEqual(actual, expected)

    @patch("requests.request")
    def test_get_blocked_hosts_without_new_line(self, mock_post):
        text = {"response": ["shun (management) 1.1.1.1 2.2.2.2 444 555 6"]}
        mock_post.return_value = TestGetBlockedHosts.Response(text, 200)
        actual = self.action.run()

        expected = {
            Output.HOSTS: [
                {
                    "source_ip": "1.1.1.1",
                    "dest_ip": "2.2.2.2",
                    "source_port": "444",
                    "dest_port": "555",
                    "protocol": "6",
                }
            ]
        }

        self.assertEqual(actual, expected)

    @patch("requests.request")
    def test_get_blocked_hosts_incomplete_response(self, mock_post):
        text = {"response": ["shun (management) 1.1.1.1 2.2.2.2\n"]}
        mock_post.return_value = TestGetBlockedHosts.Response(text, 200)
        actual = self.action.run()

        expected = {Output.HOSTS: []}

        self.assertEqual(actual, expected)

    @patch("requests.request")
    def test_get_blocked_hosts_incomplete_response2(self, mock_post):
        text = {"response": ["shun (management) 1.1.1.1 2.2.2.2\nshun (management) 3.3.3.3 4.4.4.4 333 444 6\n"]}
        mock_post.return_value = TestGetBlockedHosts.Response(text, 200)
        actual = self.action.run()

        expected = {
            Output.HOSTS: [
                {
                    "source_ip": "3.3.3.3",
                    "dest_ip": "4.4.4.4",
                    "source_port": "333",
                    "dest_port": "444",
                    "protocol": "6",
                }
            ]
        }

        self.assertEqual(actual, expected)

    @patch("requests.request")
    def test_get_blocked_hosts_incomplete_response3(self, mock_post):
        text = {"response": ["shun (management) 1.1.1.1 2.2.2.2 444 555 6\nshun (management) 3.3.3.3 4.4.4.4\n"]}
        mock_post.return_value = TestGetBlockedHosts.Response(text, 200)
        actual = self.action.run()

        expected = {
            Output.HOSTS: [
                {
                    "source_ip": "1.1.1.1",
                    "dest_ip": "2.2.2.2",
                    "source_port": "444",
                    "dest_port": "555",
                    "protocol": "6",
                }
            ]
        }

        self.assertEqual(actual, expected)

    @patch("requests.request")
    def test_get_blocked_hosts_bad_response(self, mock_post):
        text = {
            "response": [
                "shun (management) 1.1.1.1 2.2.2.2 444 555 6\n\n  \n     \n\n       	\nshun (management) 3.3.3.3 "
                "4.4.4.4 333 444 6\n"
            ]
        }
        mock_post.return_value = TestGetBlockedHosts.Response(text, 200)
        actual = self.action.run()

        expected = {
            Output.HOSTS: [
                {
                    "source_ip": "1.1.1.1",
                    "dest_ip": "2.2.2.2",
                    "source_port": "444",
                    "dest_port": "555",
                    "protocol": "6",
                },
                {
                    "source_ip": "3.3.3.3",
                    "dest_ip": "4.4.4.4",
                    "source_port": "333",
                    "dest_port": "444",
                    "protocol": "6",
                },
            ]
        }

        self.assertEqual(actual, expected)

    @patch("requests.request")
    def test_get_blocked_hosts_no_blocked_hosts(self, mock_post):
        text = {"response": [""]}
        mock_post.return_value = TestGetBlockedHosts.Response(text, 200)
        actual = self.action.run()

        expected = {Output.HOSTS: []}

        self.assertEqual(actual, expected)

    @patch("requests.request")
    def test_get_blocked_hosts_empty_list(self, mock_post):
        text = {"response": []}
        mock_post.return_value = TestGetBlockedHosts.Response(text, 200)
        actual = self.action.run()

        expected = {Output.HOSTS: []}

        self.assertEqual(actual, expected)

    @patch("requests.request")
    def test_get_blocked_hosts_response_as_string(self, mock_post):
        text = {"response": "test"}
        mock_post.return_value = TestGetBlockedHosts.Response(text, 200)
        actual = self.action.run()

        expected = {Output.HOSTS: []}

        self.assertEqual(actual, expected)

    @patch("requests.request")
    def test_get_blocked_hosts_no_response(self, mock_post):
        text = {"response": None}
        mock_post.return_value = TestGetBlockedHosts.Response(text, 200)
        actual = self.action.run()

        expected = {Output.HOSTS: []}

        self.assertEqual(actual, expected)
