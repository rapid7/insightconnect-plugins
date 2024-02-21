import json
import logging
import os
from typing import Callable
from unittest import mock
from unittest.mock import MagicMock
from komand_domaintools.connection.connection import Connection
from insightconnect_plugin_runtime.action import Action

import requests
from domaintools.exceptions import (
    NotAuthorizedException,
    ServiceUnavailableException,
    BadRequestException,
    NotFoundException,
    InternalServerErrorException,
)


class Util:
    @staticmethod
    def default_connector(action: Action) -> Action:
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        default_connection.connect({"username": "test", "api_key": {"secretKey": "test"}})
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def load_expected(filename: str) -> dict:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), f"expected/{filename}.json.resp")) as file:
            return json.load(file)


class MockResponse:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.text = json.dumps(self.json())
        self.request = MagicMock()
        self.headers = MagicMock()

    def json(self):
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp")
        ) as file:
            return json.load(file)

    def data(self):
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp")
        ) as file:
            return json.load(file)


def mock_responder(*args, **kwargs) -> MockResponse:
    if args == ("hosting_history.com",):
        return MockResponse("test_hosting_history")
    if kwargs == {"page": 1, "days_back": 1, "query": "ip_monitor.com"}:
        return MockResponse("test_ip_monitor")
    if args == ("example.com",):
        return MockResponse("test_domain_profile")
    if kwargs == {"query": "name_server_monitor.com", "page": 1, "days_back": 0}:
        return MockResponse("test_name_server_monitor")
    if args == ("parsed_whois.com",):
        return MockResponse("test_parsed_whois")
    if kwargs == {"query": "registrant_monitor.com", "days_back": 1, "exclude": "test.com"}:
        return MockResponse("test_registrant_monitor")
    if args == ("reputation.com", True):
        return MockResponse("test_reputation")
    if kwargs == {"domain": "reverse_ip.com", "limit": 1}:
        return MockResponse("test_reverse_ip")
    if kwargs == {"query": "reverse_name_server.com", "limit": 1}:
        return MockResponse("test_reverse_name_server")
    if kwargs == {
        "page": 1,
        "ip": "10.10.10.10",
        "server": "whois.arin.net",
        "country": "CA",
        "include_total_count": True,
    }:
        return MockResponse("test_reverse_ip_whois")
    if args == ("whois.com",):
        return MockResponse("test_whois")
    if args == ("whois_history.com",):
        return MockResponse("test_whois_history")
    if kwargs == {} and args == ():
        return MockResponse("account_information")
    if kwargs == {
        "query": "example.com",
        "exclude_query": "test.com",
        "max_length": 25,
        "min_length": 1,
        "has_hyphen": False,
        "has_number": False,
        "active_only": False,
        "deleted_only": False,
        "anchor_left": False,
        "anchor_right": False,
        "page": 1,
    }:
        return MockResponse("test_domain_search")
    if kwargs == {"query": "test.com", "exclude": "example.com", "domain_status": "new", "days_back": 1}:
        return MockResponse("test_brand_monitor")
    if kwargs.get("query", "") == "test.com":
        return MockResponse("test_reverse_whois")
    if kwargs.get("query", "") == "404.com":
        raise NotFoundException(code=404, reason="Bad Request")
    if kwargs.get("query", "") == "401.com":
        raise NotAuthorizedException(code=401, reason="Not Authorized")
    if kwargs.get("query", "") == "503.com":
        raise ServiceUnavailableException(code=500, reason="Service Unavailable")
    if kwargs.get("query", "") == "400.com":
        raise BadRequestException(code=400, reason="Bad Request")
    if kwargs.get("query", "") == "500.com":
        raise InternalServerErrorException(code=500, reason="Internal Server Error")
    raise Exception("Unrecognized endpoint")
