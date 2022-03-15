import json
import time
from dataclasses import dataclass
from logging import Logger
import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean
from requests.auth import HTTPBasicAuth


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
                "assigned": self.assigned == "Assigned" if self.assigned else None,
                "isFlagged": self.is_flagged == "Flagged" if self.is_flagged else None,
                "isClosed": self.is_closed == "Closed" if self.is_closed else None,
                "hasIoc": self.has_ioc,
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


class IntSightsAPI:
    def __init__(self, account_id: str, api_key: str, logger: Logger):
        self.account_id = account_id
        self.api_key = api_key
        self.url = "https://api.intsights.com"
        self.logger = logger

    def get_indicator_by_value(self, ioc_value: str) -> dict:
        return self.make_json_request("GET", f"public/v2/iocs/ioc-by-value?iocValue={ioc_value}")

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

    def get_cve(self, cve_ids: [str]) -> list:
        content = []
        path = "public/v1/cves/get-cves-list"
        query_params = {}
        for _ in range(0, 9999):
            if cve_ids:
                query_params["cveId[]"] = cve_ids

            response_cve_list = self.make_json_request("GET", path, params=query_params)
            content.extend(response_cve_list.get("content", []))

            query_params["offset"] = response_cve_list.get("nextOffset", "")
            if not query_params["offset"]:
                break

        return content

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

            if response.status_code in [401, 403]:
                raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
            if response.status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.text)
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
