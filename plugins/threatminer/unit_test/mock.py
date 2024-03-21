import json
import os
from typing import Any, Callable, Dict
from unittest import mock

import requests

from icon_threatminer.util.api import BASE_API_URL


class MockResponse:
    def __init__(self, filename: str, status_code: int, text: str = "") -> None:
        self.filename = filename
        self.status_code = status_code
        self.text = text
        self.reason = text

    def json(self):
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp")
        ) as file:
            return json.load(file)


def mocked_request(side_effect: Callable, method: str) -> None:
    mock_function = requests
    setattr(mock_function, method, mock.Mock(side_effect=side_effect))


def mock_conditions(url: str, parameters: Dict[str, Any], status_code: int) -> MockResponse:
    if url == f"{BASE_API_URL}/av.php":
        if parameters.get("rt") == 1:
            return MockResponse("av_sample", status_code)
        elif parameters.get("rt") == 2:
            return MockResponse("av_report", status_code)
    elif url == f"{BASE_API_URL}/domain.php":
        if parameters.get("rt") in (1, 2, 3, 6):
            return MockResponse("domain_lookup", status_code)
        elif parameters.get("rt") in (4, 5):
            return MockResponse("domain_ext", status_code)
    elif url == f"{BASE_API_URL}/email.php":
        if parameters.get("rt") in (1, 2):
            return MockResponse("email_domain", status_code)
    elif url == f"{BASE_API_URL}/imphash.php":
        if parameters.get("rt") == 1:
            return MockResponse("import_hash_samples", status_code)
        elif parameters.get("rt") == 2:
            return MockResponse("import_hash_report", status_code)
    elif url == f"{BASE_API_URL}/host.php":
        if parameters.get("rt") in (1, 2, 3, 6):
            return MockResponse("ip", status_code)
        elif parameters.get("rt") in (4, 5):
            return MockResponse("ip_ext", status_code)
    elif url == f"{BASE_API_URL}/report.php":
        return MockResponse("report", status_code)
    elif url == f"{BASE_API_URL}/sample.php":
        return MockResponse("samples", status_code)
    elif url == f"{BASE_API_URL}/ssdeep.php":
        if parameters.get("rt") == 1:
            return MockResponse("ssdeep_sample", status_code)
        elif parameters.get("rt") == 2:
            return MockResponse("ssdeep_report", status_code)
    elif url == f"{BASE_API_URL}/ssl.php":
        if parameters.get("rt") == 1:
            return MockResponse("ssl_hosts", status_code)
        elif parameters.get("rt") == 2:
            return MockResponse("ssl_report", status_code)
    elif url == f"{BASE_API_URL}/reports.php":
        return MockResponse("search", status_code)
    raise Exception("Response has been not implemented")


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], kwargs.get("params", {}), 200)


def mock_request_500(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], kwargs.get("params", {}), 500)


def mock_request_503(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], kwargs.get("params", {}), 503)
