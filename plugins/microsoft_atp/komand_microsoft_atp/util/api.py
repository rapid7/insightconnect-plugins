import json
import re
import socket
import time
from logging import Logger
from typing import Any, Dict, List, Union

import requests
from insightconnect_plugin_runtime.exceptions import PluginException


class WindwosDefenderATP_API:
    def __init__(self, app_id: str, app_secret: str, tenant: str, logger: Logger):
        self.session = requests.Session()
        self.resource_url = "https://api.securitycenter.windows.com"
        self.api_token = None
        self.time_ago = 0  # Jan 1, 1970
        self.time_now = time.time()  # More than 1 hour since 1978

        self.app_id = app_id
        self.app_secret = app_secret
        self.tenant = tenant
        self.logger = logger

        self.check_and_refresh_api_token()

    def get_token(self):
        auth_url = f"https://login.windows.net/{self.tenant}/oauth2/token"
        self.logger.info("Updating Auth Token...")
        self.logger.info(f"Getting token from: {auth_url}")
        result_json = self._call_api(
            "POST",
            auth_url,
            data={
                "resource": self.resource_url,
                "client_id": self.app_id,
                "client_secret": self.app_secret,
                "grant_type": "client_credentials",
            },
        )
        self.api_token = result_json.get("access_token")
        self.logger.info(f"Authentication was successful, token is: ******************{self.api_token[-5:]}")

    def check_and_refresh_api_token(self, force_refresh_token: bool = False):
        self.time_now = time.time()
        self.logger.info(f"Time Now: {self.time_now}")
        self.logger.info(f"Time Ago: {self.time_ago}")
        self.logger.info(f"Seconds elapsed:{int(self.time_now - self.time_ago)}")

        if (self.time_now - self.time_ago) > 3500 or force_refresh_token:  # 1 hour in seconds (minus some buffer time)
            self.logger.info("Refreshing auth token")
            self.get_token()
            self.time_ago = time.time()
        else:
            self.logger.info("Token is valid, not refreshing.")

    def get_session_headers(self) -> dict:
        self.logger.info("Updating session headers.")
        return {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def find_machines(self, software: str):
        return self._make_request("GET", f"Software/{software}/machineReferences", allow_empty=True)

    def get_missing_software_updates(self, machine_id: str):
        return self._make_request("GET", f"machines/{machine_id}/getmissingkbs")

    def get_machine_action(self, action_id: str) -> dict:
        return self._make_request("GET", f"machineactions/{action_id}")

    @staticmethod
    def _validate_ip_address(ip_address: str) -> bool:
        """
        Validates the IP address. Returns True if the entered string is an IP address, otherwise False.

        :param ip_address: String to check if it's an IP address.
        :type: str

        :return: Value indicates whether the given string is an IP address or not.
        :rtype: bool
        """

        try:
            socket.inet_aton(ip_address)
            return True
        except Exception:
            return False

    @staticmethod
    def _look_for_machine(machines: List[Dict[str, Any]], machine_identification: str) -> Union[Dict[str, Any], None]:
        """
        Returns machine details that match the given identification string from computerDnsName, lastIpAddress or lastExternalIpAddress. If the machine is not found, the method returns None.        :param machines:

        :param machines: List of existing machines.
        :type: List[Dict[str, Any]]

        :param machine_identification: Machine identification string, this can be computerDnsName or IP address..
        :type: str

        :return: Machine that match given identification string
        :rtype: Dict[str, Any] | None
        """

        for machine in machines:
            for key in ["computerDnsName", "lastIpAddress", "lastExternalIpAddress"]:
                if machine.get(key) == machine_identification:
                    return machine
        return None

    def find_first_machine(self, machine_identification: str, return_identifier: bool = False) -> dict:
        # If the input is a machine ID, pass it directly to the Get Machine Information endpoint
        if re.match(r"^[a-z0-9]{40}$", machine_identification.lower()):
            return (
                self.get_machine_information(machine_identification)
                if not return_identifier
                else machine_identification
            )

        # Look for a machine in a list of machines (first 10,000 records)
        odata_query = {"$top": 10000}
        machine = self._look_for_machine(self.get_machines(odata_query).get("value"), machine_identification)
        if machine:
            return machine

        # Retry with OData queries if machine is not in the list (if more than 10,000 machines assigned...)
        if self._validate_ip_address(machine_identification):
            odata_query.update({"$filter": f"lastIpAddress eq '{machine_identification}'"})
        else:
            odata_query.update({"$filter": f"computerDnsName eq '{machine_identification}'"})

        self.logger.info("Attempting to search for machine using OData query")
        machine = self._look_for_machine(self.get_machines(odata_query).get("value"), machine_identification)
        if machine:
            return machine

        self.logger.error(f"Machine {machine_identification} not found")
        raise PluginException(preset=PluginException.Preset.NOT_FOUND)

    def get_machines(self, odata_queries: dict = None) -> dict:
        return self._make_request("GET", "machines", params=odata_queries)

    def get_machine_information(self, machine_id: str) -> dict:
        return self._make_request("GET", f"machines/{machine_id}")

    def get_machine_vulnerabilities(self, machine_id: str) -> dict:
        return self._make_request("GET", f"machines/{machine_id}/vulnerabilities")

    def get_files_from_id(self, alert_id: str) -> dict:
        return self._make_request("GET", f"alerts/{alert_id}/files")

    def isolate_machine(self, id_: str, isolation_type: str, comment: str) -> dict:
        return self._make_request(
            "POST",
            f"machines/{id_}/isolate",
            json_data={"Comment": comment, "IsolationType": isolation_type},
        )

    def unisolate_machine(self, id_: str, comment: str) -> dict:
        return self._make_request("POST", f"machines/{id_}/unisolate", json_data={"Comment": comment})

    def run_antivirus_scan(self, machine_id: str, scan_type: str, comment: str) -> dict:
        self.logger.info(
            f"Run Antivirus Scan with machine id: {machine_id}, scan Type: {scan_type}, comment: {comment}"
        )

        return self._make_request(
            "POST",
            f"machines/{machine_id}/runAntiVirusScan",
            json_data={"Comment": comment, "ScanType": scan_type},
        )

    def stop_and_quarantine_file(self, machine_id: str, sha1_id: str, comment: str) -> dict:
        self.logger.info(f"Stop and quarantine file with: {machine_id}, SHA1_ID: {sha1_id}, comment: {comment}")

        return self._make_request(
            "POST",
            f"machines/{machine_id}/StopAndQuarantineFile",
            json_data={"Comment": comment, "Sha1": sha1_id},
        )

    def get_all_alerts(self, query_parameters: str) -> dict:
        endpoint = "alerts"
        if query_parameters:
            endpoint = f"alerts{query_parameters}"

        return self._make_request("GET", endpoint)

    def submit_or_update_indicator(self, payload) -> dict:
        return self._make_request("POST", "indicators", json_data=payload)

    def delete_indicator(self, indicator_id: str) -> dict:
        return self._make_request("DELETE", f"indicators/{indicator_id}")

    def search_indicators(self, query_parameters) -> dict:
        return self._make_request("GET", f"indicators{query_parameters}")

    def get_security_recommendations(self, machine_id: str) -> dict:
        return self._make_request("GET", f"machines/{machine_id}/recommendations")

    def get_installed_software(self, machine: str) -> dict:
        return self._make_request("GET", f"machines/{machine}/software")

    def manage_tags(self, machine: str, tag: str, action_type: str) -> dict:
        return self._make_request("POST", f"machines/{machine}/tags", json_data={"Value": tag, "Action": action_type})

    def get_related_machines(self, indicator: str, indicator_type: str) -> dict:
        return self._make_request("GET", f"{indicator_type}/{indicator}/machines")

    def collect_investigation_package(self, machine: str, comment: str) -> dict:
        return self._make_request(
            "POST", f"machines/{machine}/collectInvestigationPackage", json_data={"Comment": comment}
        )

    def find_machine_id(self, machine_identification: str) -> str:
        return self.find_first_machine(machine_identification, return_identifier=True).get("id", "")

    def _make_request(
        self, method: str, path: str, json_data: dict = None, allow_empty: bool = False, params: dict = None
    ) -> dict:
        self.check_and_refresh_api_token()
        return self._call_api(
            method,
            f"{self.resource_url}/api/{path}",
            json_data=json_data,
            headers=self.get_session_headers(),
            allow_empty=allow_empty,
            params=params,
        )

    def _call_api(  # noqa: C901
        self,
        method: str,
        url: str,
        params: dict = None,
        json_data: dict = None,
        data: dict = None,
        headers: dict = None,
        allow_empty: bool = False,
    ) -> dict:
        response = {"text": ""}
        try:
            response = requests.request(method, url, json=json_data, params=params, data=data, headers=headers)

            if response.status_code == 401:
                raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD, data=response.text)
            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
            if response.status_code == 404 and allow_empty:
                return {}
            if response.status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.text)
            if response.status_code == 400 and '"message":"Action is already in progress"' in response.text:
                self.logger.info("Action is already in progress")
                return {"status": "InProgress"}
            if response.status_code >= 400:
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
            if 200 <= response.status_code < 300:
                if response.text:
                    return response.json()
                return {}

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
        except requests.exceptions.HTTPError:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
