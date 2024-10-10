import sys
import os
from unittest import TestCase
from unittest.mock import patch, MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from util import Util
from jsonschema import validate
from parameterized import parameterized
from icon_rapid7_insightcloudsec.actions.get_resource_id import GetResourceId
from icon_rapid7_insightcloudsec.actions.get_resource_id.schema import Input


@patch("requests.request", side_effect=Util.mocked_requests)
class TestGetResourceId(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetResourceId())

    @parameterized.expand(Util.load_parameters("get_resource_id").get("parameters"))
    def test_get_resource_id(
        self,
        mock_request: MagicMock,
        name: str,
        limit: int,
        offset: int,
        search_string: str,
        expected: dict,
    ):
        actual = self.action.run({Input.LIMIT: limit, Input.OFFSET: offset, Input.SEARCH_STRING: search_string})
        validate(actual, self.action.output.schema)
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("get_resource_id_bad").get("parameters"))
    def test_get_resource_id_bad(
        self,
        mock_request: MagicMock,
        name: str,
        limit: int,
        offset: int,
        search_string: str,
        cause: str,
        assistance: str,
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.LIMIT: limit, Input.OFFSET: offset, Input.SEARCH_STRING: search_string})
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
