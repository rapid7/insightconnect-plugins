from komand.exceptions import PluginException

import json
from typing import Dict, Iterable, Any
import requests
import copy


def get_query(url: str, query: str) -> requests.Response:
    try:
        response = requests.get(url, params={"q": query}, allow_redirects=False)
    except requests.exceptions.HTTPError as e:
        raise PluginException(
            cause="Unexpected http error",
            data=str(e),
            assistance="If the issue persists please contact support.",
        )
    check_status_code(
        response.status_code, range(200, 299),
        cause=f"Received HTTP {response.status_code} status code from Threatminer."
              "Please verify your Threatminer server status and try again.",
        assistance="If the issue persists please contact support.",
        data=f"{response.status_code}, {response.text[:100]}")

    return response


def extract_json_data(response: requests.Response) -> Dict:
    try:
        dct = response.json()
    except json.decoder.JSONDecodeError:
        raise PluginException(
            preset=PluginException.Preset.INVALID_JSON,
            data=response.text
        )
    return dct


def check_status_code(code: int, expected_range: Iterable, cause="",
                      assistance="", data=""):
    if code not in expected_range:
        raise PluginException(
            cause=cause,
            assistance=assistance,
            data=data,
        )


def check_api_status_code(api_resp: Dict, expected_range: Iterable):
    api_status_code = extract_response_field(api_resp, "status_code")
    normalized_status_code = normalize_status_code(api_status_code)
    check_status_code(normalized_status_code, expected_range,
                      cause="Unexpected status code received from Threatminer",
                      assistance="Please contact support",
                      data=normalized_status_code)


def normalize_status_code(api_status_code: int) -> int:
    try:
        normalized_code = int(api_status_code)
    except ValueError:
        raise PluginException(
            cause="Unexpected status code received from Threatminer",
            assistance="Please contact support",
            data=api_status_code,
        )
    return normalized_code


def normalize_data(api_resp: Dict) -> dict:
    # avoid side effects
    normalized_api_response = copy.deepcopy(api_resp)

    # normalize status code
    api_status_code = extract_response_field(api_resp, "status_code")
    normalized_status_code = normalize_status_code(api_status_code)
    normalized_api_response["status_code"] = normalized_status_code

    return normalized_api_response


def extract_response_field(api_resp: Dict, field_name: str) -> Any:
    try:
        field_value = api_resp[field_name]
    except KeyError:
        raise PluginException(
            cause=f"No {field_name} received from Threatminer",
            assistance="Please contact support",
            data=json.dumps(api_resp)
        )
    return field_value
