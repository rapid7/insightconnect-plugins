import json
import logging
import os
import sys
from typing import Callable

import requests

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import mock

from insightconnect_plugin_runtime.action import Action
from komand_cisco_umbrella_investigate.connection.connection import Connection
from komand_cisco_umbrella_investigate.connection.schema import Input
from komand_cisco_umbrella_investigate.investigate.investigate import Investigate

STUB_CONNECTION = {
    Input.API_KEY: {"secretKey": "11111111-1111-1111-1111-111111111111"},
}

BASE_URL = Investigate.BASE_URL


class Util:
    @staticmethod
    def default_connector(action: Action) -> Action:
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        default_connection.connect(STUB_CONNECTION)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename: str) -> str:
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), filename), "r", encoding="utf-8"
        ) as file_reader:
            return file_reader.read()

    @staticmethod
    def read_file_to_dict(filename: str) -> Dict[str, Any]:
        return json.loads(Util.read_file_to_string(filename))


class MockResponse:
    def __init__(self, filename: str, status_code: int, text: str = "Example Text") -> None:
        self.filename = filename
        self.status_code = status_code
        self.text = text

    def json(self):
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp")
        ) as file:
            return json.load(file)


def mocked_request(side_effect: Callable) -> None:
    mock_function = requests
    mock_function.get = mock.Mock(side_effect=side_effect)


def mock_conditions(url: str, status_code: int, **kwargs: Dict[str, Any]) -> MockResponse:
    if url == f"{BASE_URL}domains/score/example.com":
        return MockResponse("test_connection", status_code)
    elif url == f"{BASE_URL}domains/categorization/example.com":
        return MockResponse("test_categorization", status_code)
    elif url == f"{BASE_URL}recommendations/name/example.com.json":
        return MockResponse("test_cooccurrences_found", status_code)
    elif url == f"{BASE_URL}recommendations/name/example.json":
        return MockResponse("test_cooccurrences_not_found", status_code)
    elif url == f"{BASE_URL}domains/example.com/latest_tags":
        return MockResponse("test_domain_tags", status_code)
    elif url == f"{BASE_URL}domains/example/latest_tags":
        return MockResponse("test_domain_tags_not_found", status_code)
    elif url == f"{BASE_URL}whois/example.com":
        return MockResponse("test_domain_whois", status_code)
    elif f"{BASE_URL}whois/emails/" in url:
        return MockResponse("test_email_whois", status_code)
    elif url == f"{BASE_URL}ips/192.168.0.1/latest_domains":
        return MockResponse("test_latest_domains", status_code)
    elif url == f"{BASE_URL}whois/nameservers/":
        return MockResponse("test_ns_whois", status_code)
    elif url in (
        f"{BASE_URL}pdns/domain/example",
        f"{BASE_URL}pdns/name/example",
        f"{BASE_URL}pdns/ip/example",
        f'{BASE_URL}pdns/raw/"example"',
    ):
        return MockResponse("test_passive_dns_domain", status_code)
    elif url == f"{BASE_URL}pdns/timeline/example":
        return MockResponse("test_passive_dns_timeline", status_code)
    elif url == f"{BASE_URL}links/name/example.com.json":
        return MockResponse("test_related", status_code)
    elif url == f"{BASE_URL}links/name/example2.com.json":
        return MockResponse("test_related_not_found", status_code)
    elif url == f"{BASE_URL}dnsdb/name/A/example.com.json":
        return MockResponse("test_rr_history", status_code)
    elif url == f"{BASE_URL}dnsdb/ip/A/192.168.0.1.json":
        return MockResponse("test_rr_history_ip", status_code)
    elif url == f"{BASE_URL}sample/ExampleHash":
        return MockResponse("test_sample", status_code)
    elif url == f"{BASE_URL}sample/ExampleHash/artifacts":
        return MockResponse("test_sample_artifacts", status_code)
    elif url in (f"{BASE_URL}sample/ExampleHashError/artifacts", f"{BASE_URL}sample/ExampleHashError/samples"):
        return MockResponse("test_sample_artifacts_error", status_code)
    elif url == f"{BASE_URL}sample/ExampleHash/connections":
        return MockResponse("test_sample_connections", status_code)
    elif url == f"{BASE_URL}sample/ExampleHash/samples":
        return MockResponse("test_sample_samples", status_code)
    elif url == f"{BASE_URL}samples/example.com":
        return MockResponse("test_samples", status_code)
    elif url == f"{BASE_URL}search/example.com":
        return MockResponse("test_search", status_code)
    elif url == f"{BASE_URL}security/name/example.com.json":
        return MockResponse("test_security", status_code)
    elif url == f"{BASE_URL}security/name/example_error_1.com.json":
        return MockResponse("test_domain_tags_not_found", status_code)
    elif url == f"{BASE_URL}security/name/example_error_2.com.json":
        return MockResponse("test_related_not_found", status_code)
    elif url == f"{BASE_URL}timeline/ExampleName":
        return MockResponse("test_timeline", status_code)
    raise Exception("Response has been not implemented")


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], 200, **kwargs)


def mock_request_201_invalid_json(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], 201, **kwargs)


def mock_request_403(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], 403, **kwargs)


def mock_request_404(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], 404, **kwargs)


def mock_request_429(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], 429, **kwargs)


def mock_request_500(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], 500, **kwargs)


def mock_request_501(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], 501, **kwargs)


def mock_request_503(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], 503, **kwargs)
