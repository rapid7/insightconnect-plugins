from komand.exceptions import PluginException

import json
from typing import Dict, Iterable
import requests


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
            cause="Received an unexpected response from Threatminer",
            assistance="(non-JSON or no response was received).",
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
    try:
        api_status_code = api_resp["status_code"]
    except KeyError:
        raise PluginException(
            cause="No status received from Threatminer",
            assistance="Please contact support",
            data=json.dumps(api_resp)
        )
    try:
        code = int(api_status_code)
    except ValueError:
        raise PluginException(
            cause="Unexpected status code received from Threatminer",
            assistance="Please contact support",
            data=api_status_code,
        )
    check_status_code(
        code, expected_range,
        cause="Unexpected status code received from Threatminer",
        assistance="Please contact support", data=api_status_code)
