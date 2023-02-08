import sys
import os
from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized

from insightconnect_plugin_runtime.exceptions import PluginException

from unit_test.util import Util
from icon_bitwarden.actions.listAllCollections import ListAllCollections

sys.path.append(os.path.abspath("../"))


@patch("requests.request", side_effect=Util.mock_request)
class TestListCollections(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListAllCollections())

    @parameterized.expand(
        [
            [
                "list_collections",
                Util.read_file_to_dict("expected/list_collections.json.exp"),
            ]
        ]
    )
    def test_list_collections(self, mock_request, test_name, expected):
        actual = self.action.run()
        self.assertEqual(actual, expected)
