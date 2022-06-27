import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_urlscan.actions.search import Search
from komand_urlscan.actions.search.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.get", side_effect=Util.mocked_requests_post)
class TestSearch(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(Search())

    @parameterized.expand(Util.load_json("payloads/search_parameters.json.resp").get("parameters"))
    def test_search(self, mock_get, name, input_type, query, sort, expected):
        actual = self.action.run({Input.INPUT_TYPE: input_type, Input.Q: query, Input.SORT: sort})
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_json("payloads/search_parameters_bad.json.resp").get("parameters"))
    def test_search_bad(self, mock_get, name, input_type, query, sort, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.INPUT_TYPE: input_type, Input.Q: query, Input.SORT: sort})
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
