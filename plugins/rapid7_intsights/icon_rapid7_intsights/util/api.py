import json
import time
from dataclasses import dataclass
from logging import Logger
import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean
from requests.auth import HTTPBasicAuth
from icon_rapid7_intsights.util.constants import Assistance, Cause


@dataclass
class AlertParams:
    alert_type: [str]
    severity: [str]
    source_type: [str]
    network_type: [str]
    matched_asset_value: str
    remediation_status: [str]
    source_date_from: str
    source_date_to: str
    found_date_from: str
    found_date_to: str
    assigned: str
    is_flagged: str
    is_closed: str
    has_ioc: bool

    def to_dict(self) -> dict:
        return clean(
            {
                "alertType": ",".join(self.alert_type) if self.alert_type else None,
                "severity": ",".join(self.severity) if self.severity else None,
                "sourceType": ",".join(self.source_type) if self.source_type else None,
                "networkType": ",".join(self.network_type) if self.network_type else None,
                "matchedAssetValue": ",".join(self.matched_asset_value) if self.matched_asset_value else None,
                "remediationStatus": ",".join(self.remediation_status) if self.remediation_status else None,
                "sourceDateFrom": int(self.source_date_from) if self.source_date_from else None,
                "sourceDateTo": int(self.source_date_to) if self.source_date_to else None,
                "foundDateFrom": int(self.found_date_from) if self.found_date_from else None,
                "foundDateTo": int(self.found_date_to) if self.found_date_to else None,
                "assigned": json.dumps(self.assigned == "Assigned" if self.assigned else None),
                "isFlagged": json.dumps(self.is_flagged == "Flagged" if self.is_flagged else None),
                "isClosed": json.dumps(self.is_closed == "Closed" if self.is_closed else None),
                "hasIoc": json.dumps(self.has_ioc if self.has_ioc else None),
            }
        )


@dataclass
class Image:
    type: str
    data: str


@dataclass
class ManualAlertParams:
    title: str
    found_date: str
    description: str
    type: str
    sub_type: str
    severity: str
    source_type: int
    source_network_type: int
    source_url: int
    source_date: int
    images: [Image]

    def to_dict(self) -> dict:
        images = []
        if self.images:
            for image in self.images:
                if not image:
                    continue
                try:
                    images.append({"Type": image["type"], "Data": image["data"]})
                except KeyError as e:
                    raise PluginException(cause="Wrong input parameter.", assistance=f"Wrong image: {e}.")

        return clean(
            {
                "FoundDate": self.found_date,
                "Details": {
                    "Title": self.title,
                    "Description": self.description,
                    "Type": self.type,
                    "SubType": self.sub_type,
                    "Severity": self.severity,
                    "Source": {
                        "Type": self.source_type,
                        "NetworkType": self.source_network_type,
                        "URL": self.source_url,
                        "Date": self.source_date,
                    },
                    "Images": images,
                },
            }
        )


@dataclass
class IOCParams:
    last_updated_from: str
    last_updated_to: str
    last_seen_from: str
    last_seen_to: str
    first_seen_from: str
    first_seen_to: str
    status: str
    type: [str]
    severity: [str]
    source_ids: [str]
    kill_chain_phases: [str]
    limit: int
    offset: str
    enterprise_tactics: [str]

    OFFSET_MINIMUM = 1
    OFFSET_MAXIMUM = 1000
    OFFSET_DEFAULT = 1000

    def limit_range(self, number: int, _min: int, _max: int) -> int:
        return max(min(_max, number), _min)

    def to_dict(self) -> dict:
        return clean(
            {
                "lastUpdatedFrom": self.last_updated_from if self.last_updated_from else None,
                "lastUpdatedTo": self.last_updated_to if self.last_updated_to else None,
                "lastSeenFrom": self.last_seen_from if self.last_seen_from else None,
                "lastSeenTo": self.last_seen_to if self.last_seen_to else None,
                "firstSeenFrom": self.first_seen_from if self.first_seen_from else None,
                "firstSeenTo": self.first_seen_to if self.first_seen_to else None,
                "status": self.status if self.status else None,
                "type[]": list(self.type) if self.type else None,
                "severity[]": list(self.severity) if self.severity else None,
                "sourceIds[]": list(self.source_ids) if self.source_ids else None,
                "killChainPhases[]": list(self.kill_chain_phases) if self.kill_chain_phases else None,
                "limit": self.limit_range(self.limit, self.OFFSET_MINIMUM, self.OFFSET_MAXIMUM)
                if self.limit
                else self.OFFSET_DEFAULT,
                "offset": self.offset if self.offset else None,
                "enterpriseTactics[]": list(self.enterprise_tactics) if self.enterprise_tactics else None,
            }
        )


def current_milli_time():
    return round(time.time() * 1000)


def subtract_day(time: int):
    day_in_milliseconds = 86400 * 1000
    minus_day_in_milliseconds = time - day_in_milliseconds
    return minus_day_in_milliseconds


def subtract_hour(time: int):
    hour_in_milliseconds = 3600 * 1000
    minus_hour_in_milliseconds = time - hour_in_milliseconds
    return minus_hour_in_milliseconds


def subtract_week(time: int):
    week_in_milliseconds = 604800 * 1000
    minus_week_in_milliseconds = time - week_in_milliseconds
    return minus_week_in_milliseconds


class IntSightsAPI:
    def __init__(self, account_id: str, api_key: str, logger: Logger):
        self.account_id = account_id
        self.api_key = api_key
        self.url = "https://api.intsights.com"
        self.logger = logger

    def get_indicator_by_value(self, ioc_value: str) -> dict:
        return self.make_json_request("GET", f"public/v3/iocs/ioc-by-value?iocValue={ioc_value}")

    def get_indicators_by_filter(self, query_params: IOCParams) -> dict:
        return self.make_json_request("GET", "public/v3/iocs", params=query_params.to_dict())

    def enrich_indicator(self, ioc_value: str) -> dict:
        response = {}
        for _ in range(0, 9999):
            response = self.make_json_request("GET", f"public/v1/iocs/enrich/{ioc_value}")
            if response.get("Status", "InProgress") in ["Done", "Failed"]:
                break
            time.sleep(5)

        return response

    def rescan_indicator(self, indicator_file_hash: str) -> dict:
        return self.make_json_request("POST", "public/v1/iocs/rescan", json_data={"IocValue": indicator_file_hash})

    def get_scan_status(self, task_id: str) -> dict:
        return self.make_json_request("GET", f"public/v1/iocs/rescan/status/{task_id}")

    def get_complete_alert_by_id(self, alert_id: str) -> dict:
        return self.make_json_request("GET", f"public/v1/data/alerts/get-complete-alert/{alert_id}")

    def takedown_request(self, alert_id: str, target: str) -> dict:
        return self.make_json_request(
            "PATCH", f"public/v1/data/alerts/takedown-request/{alert_id}", json_data={"Target": target}
        )

    def get_alerts(self, alert_params: AlertParams) -> list:
        response = self.make_request("GET", "public/v1/data/alerts/alerts-list", params=alert_params.to_dict())
        try:
            if response.text:
                return response.json()
        except json.decoder.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=e)

        return []

    def add_manual_alert(self, manual_alert_params: ManualAlertParams) -> str:
        return self.make_request("PUT", "public/v1/data/alerts/add-alert", json_data=manual_alert_params.to_dict()).text

    def get_cve(self, cve_ids: [str], offset: str = None) -> dict:
        path = "public/v1/cves/get-cves-list"
        query_params = {}
        if offset:
            query_params["offset"] = offset
        if cve_ids:
            query_params["cveId[]"] = cve_ids
        response_cve_list = self.make_json_request("GET", path, params=query_params)
        return {"content": response_cve_list.get("content", []), "next_offset": response_cve_list.get("nextOffset", "")}

    def add_cve(self, cve_ids: [str]) -> dict:
        path = "public/v1/cves/add-cves"
        response = self.make_json_request("POST", path, json_data={"cveIds": cve_ids})

        return response

    def delete_cve(self, cve_ids: [str]) -> dict:
        path = "public/v1/cves/delete-cves"
        response = self.make_json_request("DELETE", path, json_data={"cveIds": cve_ids})

        return response

    def test_credentials(self) -> bool:
        return self.make_request("HEAD", "public/v1/test-credentials").status_code == 200

    def get_iocs_for_cyber_term(self, cyber_term_id: str, parameters: dict) -> dict:
        return self.make_json_request(
            "GET", f"public/v1/threat-library/cyber-terms/{cyber_term_id}/iocs", params=parameters
        )

    def get_cves_for_cyber_term(self, cyber_term_id: str) -> dict:
        return self.make_json_request("GET", f"public/v1/threat-library/cyber-terms/{cyber_term_id}/cves")

    def get_cyber_terms_by_filter(self, parameters: dict) -> dict:
        return self.make_json_request("GET", "public/v1/threat-library/cyber-terms", params=parameters)

    def close_alert(self, alert_id: str, json_data: dict) -> bool:
        self.make_request("PATCH", f"public/v1/data/alerts/close-alert/{alert_id}", json_data=json_data)
        return True

    def make_json_request(self, method: str, path: str, json_data: dict = None, params: dict = None) -> dict:
        try:
            response = self.make_request(method=method, path=path, json_data=json_data, params=params)
            if response.status_code == 204:
                return {}

            json_response = response.json()
            if json_response.get("Status") == "Invalid":
                raise PluginException(
                    cause="IntSights returned an error response: ", assistance=f"{json_response.get('FailedReason')}."
                )
            return json_response
        except json.decoder.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=e)

    def make_request(self, method: str, path: str, json_data: dict = None, params: dict = None) -> requests.Response:
        try:
            response = requests.request(
                method=method,
                url=f"{self.url}/{path}",
                headers={"Content-Type": "application/json"},
                verify=True,
                params=params,
                json=json_data,
                auth=HTTPBasicAuth(self.account_id, self.api_key),
            )
            if response.status_code == 400:
                raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response.text)
            if response.status_code in [401, 403]:
                raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
            if response.status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.text)
            if response.status_code == 422:
                raise PluginException(
                    cause=Cause.INVALID_DETAILS,
                    assistance=Assistance.VERIFY_INPUT,
                    data=response.text,
                )
            if 400 <= response.status_code < 500:
                raise PluginException(
                    preset=PluginException.Preset.UNKNOWN,
                    data=response.text,
                )
            if response.status_code >= 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)

            if 200 <= response.status_code < 300:
                return response

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except requests.exceptions.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)
