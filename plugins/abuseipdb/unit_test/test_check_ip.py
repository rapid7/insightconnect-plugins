import json
import sys
import os

import requests

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from komand_abuseipdb.actions.check_ip import CheckIp
from komand_abuseipdb.connection.connection import Connection
import logging


def read_file_to_string(filename):
    with open(filename) as my_file:
        return my_file.read()

# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code
            self.text = "This is some error text"
        def json(self):
            return json.loads(self.json_data)

    # Since this is folder down from the base unit_test folder, the base path may change on us if we're
    # running the whole suite, or just these tests.
    actual_path = os.path.dirname(os.path.realpath(__file__))
    actual_joined_path = os.path.join(actual_path, "payloads/check_ip_data.json")
    get_messages_from_user_payload = read_file_to_string(actual_joined_path)
    if args[0] == "https://api.abuseipdb.com/api/v2/login":
        return MockResponse({"access_token": "test_api_token6"}, 200)
    if args[0] == "https://api.abuseipdb.com/api/v2/check":
        return MockResponse(get_messages_from_user_payload, 200)

    print(f"mocked_requests_get failed looking for: {args[0]}")
    return MockResponse(None, 404)


class MockConnection:
    def __init__(self):
        self.api_key = 100
        self.base = "https://api.abuseipdb.com/api/v2"
        self.headers = None

    def make_headers_and_refresh_token(self):
        return {"headers": "test_headers"}


class TestCheckIP(TestCase):
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_check_ip(self, mock_get):
        log = logging.getLogger("Test")
        test_action = CheckIp()
        test_action.connection = MockConnection()
        test_action.logger = log

        working_params = {
            "address": "198.51.100.102",
            "days": "30",
            "verbose": True
        }
        results = test_action.run(working_params)
        expected = {
          "ipAddress": "198.51.100.100",
          "isPublic": True,
          "ipVersion": 4,
          "isWhitelisted": False,
          "abuseConfidenceScore": 100,
          "countryCode": "CN",
          "countryName": "China",
          "usageType": "Data Center/Web Hosting/Transit",
          "isp": "Tencent Cloud Computing (Beijing) Co. Ltd",
          "domain": "tencent.com",
          "totalReports": 1,
          "numDistinctUsers": 1,
          "lastReportedAt": "2018-12-20T20:55:14+00:00",
          "reports": [
            {
              "reportedAt": "2018-12-20T20:55:14+00:00",
              "comment": "Dec 20 20:55:14 srv206 sshd[13937]: Invalid user oracle from 198.51.100.100",
              "categories": [
                18,
                22
              ],
              "reporterId": 1,
              "reporterCountryCode": "US",
              "reporterCountryName": "United States"
            }
          ],
          "found": True
        }

        self.assertNotEqual({}, results, "returns non - empty results")
        self.assertEqual(expected, results)
