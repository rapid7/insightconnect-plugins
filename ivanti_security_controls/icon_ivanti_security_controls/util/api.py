import requests
from insightconnect_plugin_runtime.exceptions import PluginException
import json
from requests_ntlm import HttpNtlmAuth
from urllib.parse import parse_qs, urlparse


class IvantiSecurityControlsAPI:
    def __init__(self, host, port, ssl_verify, username, password, logger):
        self.url = f"https://{host}:{port}/st/console/api/v1.0"
        self.ntlm_auth = HttpNtlmAuth(username, password)
        self.logger = logger
        self.ssl_verify = ssl_verify

    def get_patch_details(self, patch_id):
        return self._call_api("GET", f"{self.url}/patches/{patch_id}")

    def search_patches(self, security_ids: list):
        cves = []
        kbs = []
        bulletin_ids = []
        patch_ids = []

        if security_ids:
            for security_id in security_ids:
                security_id_upper = security_id.upper()
                if security_id_upper.startswith("CVE"):
                    cves.append(security_id_upper)
                elif security_id_upper.startswith("MS"):
                    bulletin_ids.append(security_id_upper)
                elif security_id_upper.startswith("Q"):
                    kbs.append(security_id_upper)
                elif security_id_upper.isnumeric():
                    patch_ids.append(security_id_upper)

        vulnerabilities = []
        if cves:
            vulnerabilities.extend(self._get_id("cves", cves))

        if kbs:
            vulnerabilities.extend(self._get_id("kbs", kbs))

        if bulletin_ids:
            vulnerabilities.extend(self._get_id("bulletin_ids", bulletin_ids))

        for patch_id in patch_ids:
            vulnerabilities.append(self._call_api("GET", f"{self.url}/patches/{patch_id}"))

        return self._remove_duplicates(vulnerabilities)

    def _get_id(self, id_name: str, ids: list) -> list:
        vulnerabilities = []
        output = self._call_api("GET", f"{self.url}/patches", params={id_name: ",".join(ids)})
        if output and "value" in output:
            for e in output.get("value"):
                vulnerabilities.extend(e.get("vulnerabilities"))

        return vulnerabilities

    @staticmethod
    def _remove_duplicates(vulnerabilities: list) -> list:
        duplicates = {d.get("id"): d for d in vulnerabilities}
        return [v for k, v in duplicates.items()]

    def get_agent(self, agent_id):
        return self._call_api("GET", f"{self.url}/agents/{agent_id}")

    def get_agent_status(self, agent_id):
        return self._call_api("GET", f"{self.url}/agents/{agent_id}/status")

    def get_agents(self, count=1000, name="", listening=""):
        agents = []
        url = f"{self.url}/agents"
        params = {'count': count, 'name': name, 'listening': listening}

        while True:
            response = self._call_api("GET", url, params=params)

            agents = agents + response.get('value', [])

            try:
                # Only retrieve start parameter from next url href since API does NOT include name and listening
                # parameters even if included in original request so the next href can't be used blindly
                query_params = parse_qs(urlparse(response['links']['next']['href']).query)
                # Add or overwrite start parameter for next request
                params['start'] = query_params['start']
            except KeyError:
                # Return current list of agents when there are no more links to follow
                return agents

    def start_patch_scan(self, payload):
        return self._call_api("POST", f"{self.url}/patch/scans", json_data=payload)

    def get_patch_scan_machines(self, scan_id):
        return self._call_api("GET", f"{self.url}/patch/scans/{scan_id}/machines")

    def get_patch_scan_status_details(self, scan_id, allow_404=False):
        return self._call_api("GET", f"{self.url}/patch/scans/{scan_id}", allow_404=allow_404)

    def get_detected_patches(self, scan_id, machine_id):
        return self._call_api("GET", f"{self.url}/patch/scans/{scan_id}/machines/{machine_id}/patches")

    def get_patch_deployment(self, deployment_id):
        return self._call_api("GET", f"{self.url}/patch/deployments/{deployment_id}")

    def get_patch_deployment_machines(self, deployment_id):
        return self._call_api("GET", f"{self.url}/patch/deployments/{deployment_id}/machines")

    def get_patch_deployment_machine(self, deployment_id, machine_id):
        return self._call_api("GET", f"{self.url}/patch/deployments/{deployment_id}/machines/{machine_id}")

    def create_patch_group(self, payload):
        return self._call_api("POST", f"{self.url}/patch/groups", json_data=payload)

    def add_cves_to_patch_group(self, patch_group_id, payload):
        return self._call_api("POST", f"{self.url}/patch/groups/{patch_group_id}/patches/cves", json_data=payload)

    def create_patch_scan_template(self, payload):
        return self._call_api("POST", f"{self.url}/patch/scanTemplates", json_data=payload)

    def get_patch_scan_template(self, patch_scan_template_id):
        return self._call_api("GET", f"{self.url}/patch/scanTemplates/{patch_scan_template_id}")

    def _call_api(self, method, url, params=None, json_data=None, allow_404=False):
        try:
            response = requests.request(method, url,
                                        auth=self.ntlm_auth,
                                        json=json_data,
                                        params=params,
                                        verify=self.ssl_verify)
            if response.status_code == 401:
                raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD)
            if response.status_code == 404:
                if allow_404:
                    return None
                else:
                    raise PluginException(preset=PluginException.Preset.NOT_FOUND)
            if response.status_code == 409:
                raise PluginException(cause='Conflict.', assistance='Resource with this name already exists.')
            if 200 <= response.status_code < 300:
                return response.json()

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            self.logger.info(f"Invalid json: {e}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)
        except requests.exceptions.SSLError as e:
            raise PluginException(cause='Failed to connect to Ivanti Security Controls API.',
                                  assistance='Likely related to untrusted TLS/SSL certificate chain.',
                                  data=e)
        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Call to Ivanti Security Controls failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN)
