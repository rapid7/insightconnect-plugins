import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from jsonschema import validate
from komand_rapid7_intelhub.actions.search_threat_actors import SearchThreatActors
from komand_rapid7_intelhub.actions.search_threat_actors.schema import Input

from util import Util


class TestSearchThreatActors(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(SearchThreatActors())

    @patch("requests.request", side_effect=Util.mock_request)
    def test_search_threat_actors(self, mock_request: MagicMock) -> None:
        input_params = {Input.SEARCH: "APT28", Input.PAGE: 1, Input.PAGE_SIZE: 2}
        validate(input_params, self.action.input.schema)
        response = self.action.run(input_params)
        validate(response, self.action.output.schema)
        self.assertEqual(Util.read_file_to_dict("expected/search_threat_actors.json.exp"), response)
        self.assertEqual({"page": 1, "page-size": 2, "search": "APT28"}, mock_request.call_args.kwargs["params"])
