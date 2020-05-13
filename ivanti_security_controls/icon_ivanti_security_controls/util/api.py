import requests
from insightconnect_plugin_runtime.exceptions import PluginException
import json
from requests_ntlm import HttpNtlmAuth


class IvantiSecurityControlsAPI:
    def __init__(self, host, port, ssl_verify, username, password, logger):
        self.url = f"https://{host}:{port}/st/console/api/v1.0"
        self.ntlm_auth = HttpNtlmAuth(username, password)
        self.logger = logger
        self.ssl_verify = ssl_verify

    def get_agent(self, agent_id):
        return self._call_api("GET", f"{self.url}/agents/{agent_id}")

    def get_agent_status(self, agent_id):
        return self._call_api("GET", f"{self.url}/agents/{agent_id}/status")

    def get_agents(self, count=1000, name="", listening=""):
        agents = []
        url = f"{self.url}/agents?count={count}&name={name}&listening={listening}"
        while True:
            response = self._call_api("GET", url)

            agents = agents + response.get('value', [])

            try:
                url = response['links']['next']['href']
            except KeyError:
                # Return current list of agents when there are no more links to follow
                return agents

    def start_patch_scan(self, payload):
        return self._call_api("POST", f"{self.url}/patch/scans", json_data=payload)

    def get_patch_scan_machines(self, scan_id):
        return self._call_api("GET", f"{self.url}/patch/scans/{scan_id}/machines")

    def get_patch_scan_status_details(self, scan_id):
        return self._call_api("GET", f"{self.url}/patch/scans/{scan_id}")

    def get_detected_patches(self, scan_id, machine_id):
        return self._call_api("GET", f"{self.url}/patch/scans/{scan_id}/machines/{machine_id}/patches")

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
