import json
from logging import Logger
from typing import Any, Dict, Union

import requests
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_threatminer.util.constants import (
    DOMAIN_LOOKUP_FLAG_DEFAULT,
    DOMAIN_LOOKUP_FLAG_MAP,
    IP_LOOKUP_FLAG_DEFAULT,
    IP_LOOKUP_FLAG_MAP,
    REPORT_FLAG_DEFAULT,
    REPORT_FLAG_MAP,
    SAMPLES_FLAG_DEFAULT,
    SAMPLES_LOOKUP_FLAG_MAP,
    SEARCH_LOOKUP_FLAG_DEFAULT,
    SEARCH_LOOKUP_FLAG_MAP,
)
from icon_threatminer.util.utils import normalize_response_data, prune_domain


BASE_API_URL = "https://api.threatminer.org/v2"
DEFAULT_PARAMETERS = {"api": True}


class ThreatminerAPI:
    def __init__(self, logger: Logger = None) -> None:
        self.logger = logger

    def test(self) -> None:
        self._call_api("GET", "domain.php", parameters={"q": "example.com", "rt": 1})

    def ssl_hosts(self, query: str, report: bool = False) -> Dict[str, Any]:
        return self._call_api("GET", "ssl.php", parameters={"q": query, "rt": 1 if not report else 2})

    def ssdeep(self, query: str, report: bool = False) -> Dict[str, Any]:
        return self._call_api("GET", "ssdeep.php", parameters={"q": query, "rt": 1 if not report else 2})

    def import_hash(self, query: str, report: bool = False) -> Dict[str, Any]:
        return self._call_api("GET", "imphash.php", parameters={"q": query, "rt": 1 if not report else 2})

    def email(self, email: str, report: bool = False) -> Dict[str, Any]:
        return self._call_api("GET", "email.php", parameters={"q": email, "rt": 1 if not report else 2})

    def av_detection(self, query: str, report: bool = False) -> Dict[str, Any]:
        return self._call_api("GET", "av.php", parameters={"q": query, "rt": 1 if not report else 2})

    def search(self, query: str, query_type: str) -> Dict[str, Any]:
        return self._call_api(
            "GET",
            "reports.php",
            parameters={
                "q": query,
                "rt": SAMPLES_LOOKUP_FLAG_MAP.get(query_type, SAMPLES_FLAG_DEFAULT),
            },
        )

    def samples(self, query: str, query_type: str) -> Dict[str, Any]:
        return self._call_api(
            "GET",
            "sample.php",
            parameters={
                "q": query,
                "rt": SEARCH_LOOKUP_FLAG_MAP.get(query_type, SEARCH_LOOKUP_FLAG_DEFAULT),
            },
        )

    def report(self, filename: str, year: str, query_type: str) -> Dict[str, Any]:
        return self._call_api(
            "GET",
            "report.php",
            parameters={
                "q": filename,
                "y": year,
                "rt": REPORT_FLAG_MAP.get(query_type, REPORT_FLAG_DEFAULT),
            },
        )

    def ip_lookup(self, address: str, query_type: str) -> Dict[str, Any]:
        return self._call_api(
            "GET",
            "host.php",
            parameters={
                "q": address,
                "rt": IP_LOOKUP_FLAG_MAP.get(query_type, IP_LOOKUP_FLAG_DEFAULT),
            },
        )

    def domain_lookup(self, domain: str, query_type: str) -> Dict[str, Any]:
        return self._call_api(
            "GET",
            "domain.php",
            parameters={
                **DEFAULT_PARAMETERS,
                "q": prune_domain(domain),
                "rt": DOMAIN_LOOKUP_FLAG_MAP.get(query_type, DOMAIN_LOOKUP_FLAG_DEFAULT),
            },
        )

    @normalize_response_data
    def _call_api(
        self, method: str, url: str, json_data: Dict[str, Any] = None, parameters: Dict[str, Any] = None, **kwargs
    ) -> Dict[str, Any]:
        try:
            response = requests.request(
                method,
                f"{BASE_API_URL}/{url}",
                json=json_data,
                params={**parameters, **DEFAULT_PARAMETERS},
                **kwargs,
            )
            if response.status_code in range(200, 299):
                return response.json()
            elif response.status_code == 500:
                raise PluginException(
                    preset=PluginException.Preset.SERVER_ERROR, data=self._extract_status_message(response)
                )
            elif response.status_code == 503:
                raise PluginException(
                    preset=PluginException.Preset.SERVICE_UNAVAILABLE, data=self._extract_status_message(response)
                )
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=self._extract_status_message(response))
        except json.decoder.JSONDecodeError as error:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)

    @staticmethod
    def _extract_status_message(response: requests.Response) -> Union[str, None]:
        return response.json().get("status_message")
