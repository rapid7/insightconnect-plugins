import sys
import os
from unittest import TestCase
from komand_palo_alto_pan_os.actions.add_external_dynamic_list import AddExternalDynamicList
from komand_palo_alto_pan_os.actions.add_external_dynamic_list.schema import Input, Output
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))


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
        self, mock_get, mock_post, name, list_name, list_type, description, source, repeat, time, day, expected
    ):
        action = Util.default_connector(AddExternalDynamicList())
        actual = action.run(
            {
                Input.NAME: list_name,
                Input.LIST_TYPE: list_type,
                Input.DESCRIPTION: description,
                Input.SOURCE: source,
                Input.REPEAT: repeat,
                Input.TIME: time,
                Input.DAY: day,
            }
        )
        self.assertEqual(actual, expected)
