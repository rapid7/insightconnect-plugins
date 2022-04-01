import sys
import os

sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from unittest.mock import patch
from unit_test.mock import mock_search_func
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_google_search.connection.connection import Connection
from komand_google_search.actions.search import Search
from komand_google_search.actions.search.schema import Input
import logging


class TestSearch(TestCase):

    connection = None
    action = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.connection = Connection()
        cls.connection.connect(None)
        cls.connection.logger = logging.getLogger("Connection Logger")
        cls.action = Search()
        cls.action.connection = cls.connection
        cls.action.logger = logging.getLogger("Action Logger")

    def setUp(cls) -> None:
        cls.params = {
            Input.QUERY: "Example Organization",
            Input.STOP: 20,
            Input.NUM: 10,
            Input.LANG: "en",
            Input.PAUSE: 2.0,
        }

    @patch("googlesearch.search", side_effect=mock_search_func)
    def test_search(self, _mock_req):
        actual = self.action.run(self.params)
        expected = {
            "urls": [
                "https://www.example.com/",
                "http://www.example1.com/",
                "http://www.example2.com/",
                "http://www.example3.com/",
                "http://www.example4.com/",
                "http://www.example5.com/",
                "http://www.example6.com/",
                "http://www.example7.com/",
                "http://www.example8.com/",
                "http://www.example9.com/",
                "http://www.example10.com/",
                "http://www.example11.com/",
                "http://www.example12.com/",
            ]
        }
        self.assertEqual(actual, expected)

    def test_search_bad_num(self):
        self.params[Input.NUM] = 0
        with self.assertRaises(PluginException) as exception:
            actual = self.action.run(self.params)
            cause = "One or more inputs were of an invalid value"
            self.assertEqual(exception.exception.cause, cause)

    def test_search_bad_stop(self):
        self.params[Input.STOP] = 0
        with self.assertRaises(PluginException) as exception:
            actual = self.action.run(self.params)
            cause = "One or more inputs were of an invalid value"
            self.assertEqual(exception.exception.cause, cause)

    def test_search_bad_pause(self):
        self.params[Input.PAUSE] = 0
        with self.assertRaises(PluginException) as exception:
            actual = self.action.run(self.params)
            cause = "One or more inputs were of an invalid value"
            self.assertEqual(exception.exception.cause, cause)