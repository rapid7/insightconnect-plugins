import os
import sys

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from unittest.mock import patch, MagicMock

from jsonschema import validate
from komand_palo_alto_pan_os.actions.add_external_dynamic_list import AddExternalDynamicList
from komand_palo_alto_pan_os.actions.add_external_dynamic_list.schema import (
    AddExternalDynamicListInput,
    AddExternalDynamicListOutput,
    Input,
)
from parameterized import parameterized

from util import Util


@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
@patch("requests.sessions.Session.post", side_effect=Util.mocked_requests)
class TestAddExternalDynamicList(TestCase):
    @parameterized.expand(
        [
            [
                "ip_list",
                "IP List",
                "IP List",
                "List of IPs",
                "https://www.example.com/test.txt",
                "Five Minute",
                "00",
                "Monday",
                {"status": "success", "code": "20", "message": "command succeeded"},
            ],
            [
                "url_list",
                "URL List",
                "URL List",
                "List of URLs",
                "https://www.example.com/test.txt",
                "Hourly",
                "01",
                "Wednesday",
                {"status": "success", "code": "20", "message": "command succeeded"},
            ],
            [
                "domain_list",
                "Domain List",
                "Domain List",
                "List of domains",
                "https://www.example.com/test.txt",
                "Daily",
                "08",
                "Tuesday",
                {"status": "success", "code": "20", "message": "command succeeded"},
            ],
            [
                "url_list_weekly",
                "URL List",
                "URL List",
                "List of URLs",
                "https://www.example.com/test.txt",
                "Weekly",
                "12",
                "Thursday",
                {"status": "success", "code": "20", "message": "command succeeded"},
            ],
        ]
    )
    def test_add_external_dynamic_list(
        self,
        mock_get: MagicMock,
        mock_post: MagicMock,
        name: str,
        list_name: str,
        list_type: str,
        description: str,
        source: str,
        repeat: str,
        time: str,
        day: str,
        expected: dict,
    ) -> None:
        action = Util.default_connector(AddExternalDynamicList())
        input_data = {
            Input.NAME: list_name,
            Input.LIST_TYPE: list_type,
            Input.DESCRIPTION: description,
            Input.SOURCE: source,
            Input.REPEAT: repeat,
            Input.TIME: time,
            Input.DAY: day,
        }
        validate(input_data, AddExternalDynamicListInput.schema)
        actual = action.run(input_data)
        self.assertEqual(actual, expected)
        validate(actual, AddExternalDynamicListOutput.schema)
