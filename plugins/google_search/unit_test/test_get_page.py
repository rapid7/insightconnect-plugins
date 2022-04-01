import sys
import os

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from unittest.mock import patch
from unit_test.mock import mock_get_page_func
from komand_google_search.connection.connection import Connection
from komand_google_search.actions.get_page import GetPage
from komand_google_search.actions.get_page.schema import Input
import logging


class TestGetPage(TestCase):

    connection = None
    action = None
    params = {"url": "http://www.google.com"}

    @classmethod
    def setUpClass(cls) -> None:
        cls.connection = Connection()
        cls.connection.connect(None)
        cls.connection.logger = logging.getLogger("Connection Logger")
        cls.action = GetPage()
        cls.action.connection = cls.connection
        cls.action.logger = logging.getLogger("Action Logger")

    def setUp(cls) -> None:
        cls.params = {
            Input.URL: "http://www.example.com"
        }

    @patch("googlesearch.get_page", side_effect=mock_get_page_func)
    def test_get_page(self, _mock_req):
        actual = self.action.run(self.params)
        print(actual)
        expected = {
            "web_page": '<!doctype html>\\n<html>\\n<head>\\n    <title>Example Domain</title>\\n\\n    <meta charset="utf-8" />\\n    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />\\n    <meta name="viewport" content="width=device-width, initial-scale=1" />\\n    <style type="text/css">\\n    body {\\n        background-color: #f0f0f2;\\n        margin: 0;\\n        padding: 0;\\n        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;\\n        \\n    }\\n    div {\\n        width: 600px;\\n        margin: 5em auto;\\n        padding: 2em;\\n        background-color: #fdfdff;\\n        border-radius: 0.5em;\\n        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);\\n    }\\n    a:link, a:visited {\\n        color: #38488f;\\n        text-decoration: none;\\n    }\\n    @media (max-width: 700px) {\\n        div {\\n            margin: 0 auto;\\n            width: auto;\\n        }\\n    }\\n    </style>    \\n</head>\\n\\n<body>\\n<div>\\n    <h1>Example Domain</h1>\\n    <p>This domain is for use in illustrative examples in documents. You may use this\\n    domain in literature without prior coordination or asking for permission.</p>\\n    <p><a href="https://www.iana.org/domains/example">More information...</a></p>\\n</div>\\n</body>\\n</html>\\n'
        }
        self.assertEqual(actual, expected)

    def test_get_page_bad_url(self):
        self.params[Input.URL] = "example.com"
        with self.assertRaises(PluginException) as exception:
            actual = self.action.run(self.params)
            cause = "URL input must be a valid URL value"
            self.assertEqual(exception.exception.cause, cause)