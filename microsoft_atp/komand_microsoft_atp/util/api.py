import requests
from insightconnect_plugin_runtime.exceptions import PluginException
import json
import time
from logging import Logger
import re


class WindwosDefenderATP_API:
    def __init__(self, app_id: str, app_secret: str, tenant: str, logger: Logger):
        self.session = requests.Session()
        self.resource_url = "https://api.securitycenter.windows.com"
        self.api_token = ""
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
                "grant_type": "client_credentials"
            }
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
            'Authorization': f'Bearer {self.api_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    def find_machines(self, software: str):
        return self._make_request("GET", f"Software/{software}/machineReferences", allow_empty=True)

    def get_machine_action(self, action_id: str) -> dict:
        return self._make_request("GET", f"machineactions/{action_id}")

    def find_first_machine(self, machine_identification: str) -> dict:
        if re.match(r'^[a-z0-9]{40}$', machine_identification.lower()):
            return self.get_machine_information(machine_identification)

        machines = self.get_machines()
        for machine in machines.get('value'):
            for key in ["computerDnsName", "lastIpAddress", "lastExternalIpAddress"]:
                if machine.get(key) == machine_identification:
                    return machine

        self.logger.error(f"Machine {machine_identification} not found")
        raise PluginException(preset=PluginException.Preset.NOT_FOUND)

    def get_machines(self) -> dict:
        return self._make_request("GET", f"machines")

    def get_machine_information(self, machine_id: str) -> dict:
        return self._make_request("GET", f"machines/{machine_id}")

    def get_machine_vulnerabilities(self, machine_id: str) -> dict:
        return self._make_request("GET", f"machines/{machine_id}/vulnerabilities")

    def get_files_from_id(self, alert_id: str) -> dict:
        return self._make_request("GET", f"alerts/{alert_id}/files")

    def isolate_machine(self, id_: str, isolation_type: str, comment: str) -> dict:
        return self._make_request("POST", f"machines/{id_}/isolate", json_data={
            "Comment": comment,
            "IsolationType": isolation_type
        })

    def unisolate_machine(self, id_: str, comment: str) -> dict:
        return self._make_request("POST", f"machines/{id_}/unisolate", json_data={
            "Comment": comment
        })

    def run_antivirus_scan(self, machine_id: str, scan_type: str, comment: str) -> dict:
        self.logger.info(
            f"Run Antivirus Scan with machine id: {machine_id}, scan Type: {scan_type}, comment: {comment}"
        )

        return self._make_request("POST", f"machines/{machine_id}/runAntiVirusScan", json_data={
            "Comment": comment,
            "ScanType": scan_type
        })

    def stop_and_quarantine_file(self, machine_id: str, sha1_id: str, comment: str) -> dict:
        self.logger.info(f"Stop and quarantine file with: {machine_id}, SHA1_ID: {sha1_id}, comment: {comment}")

        return self._make_request("POST", f"machines/{machine_id}/StopAndQuarantineFile", json_data={
            "Comment": comment,
            "Sha1": sha1_id
        })

    def get_all_alerts(self, query_parameters: str) -> dict:
        endpoint = "alerts"
        if query_parameters:
            endpoint = f"alerts{query_parameters}"

        return self._make_request("GET", endpoint)

    def _make_request(self, method: str, path: str, json_data: dict = None, allow_empty: bool = False) -> dict:
        self.check_and_refresh_api_token()
        return self._call_api(
            method,
            f"{self.resource_url}/api/{path}",
            json_data=json_data,
            headers=self.get_session_headers(),
            allow_empty=allow_empty
        )

    def _call_api(
            self,
            method: str,
            url: str,
            params: dict = None,
            json_data: dict = None,
            data: dict = None,
            headers: dict = None,
            allow_empty: bool = False
    ) -> dict:
        response = {"text": ""}
        try:
            response = requests.request(
                method,
                url,
                json=json_data,
                params=params,
                data=data,
                headers=headers
            )

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
                return {
                    "status": "InProgress"
                }
            if response.status_code >= 400:
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
            if 200 <= response.status_code < 300:
                return response.json()

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
        except requests.exceptions.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
