import json
import time
from logging import Logger

import requests
from insightconnect_plugin_runtime.exceptions import PluginException


class ThreadCrowdAPI:
    def __init__(self, ssl_verification: bool = True, logger: Logger = None):
        self.ssl_verification = ssl_verification
        self.logger = logger
        self.url = "https://www.threatcrowd.org/searchApi/v2"

    def health_check(self):
        return self._call_api("GET", f"{self.url}/ip/report/?ip=54.192.230.36", full_response=True).status_code == 200

    def search_address(self, domain):
        return self._call_api("GET", f"{self.url}/ip/report/", params={"ip": domain})

    def antivirus_lookup(self, antivirus):
        return self._call_api("GET", f"{self.url}/antivirus/report/", params={"antivirus": antivirus})

    def search_domain(self, domain):
        return self._call_api("GET", f"{self.url}/domain/report/", params={"domain": domain})

    def search_email(self, email):
        return self._call_api("GET", f"{self.url}/email/report/", params={"email": email})

    def search_hash(self, search_hash):
        return self._call_api("GET", f"{self.url}/file/report/", params={"resource": search_hash})

    def vote_malicious(self, vote, entity):
        return self._call_api(
            "GET", "https://www.threatcrowd.org/vote.php", params={"vote": vote, "value": entity}, full_response=True
        )

    def _call_api(self, method, url, params=None, json_data=None, full_response: bool = False):  # noqa: C901
        response = {"text": ""}
        seconds_to_wait = 5
        try:
            i = 0
            while i < 10:
                response = requests.request(method, url, json=json_data, params=params, verify=self.ssl_verification)
                i += 1
                if 200 <= response.status_code < 300 and "Too many connections" in response.text:
                    self.logger.info(f"Too many connections to ThreatCrowd. Waiting {seconds_to_wait} seconds.")
                    time.sleep(seconds_to_wait)
                else:
                    break
            if response.status_code == 404 or (200 <= response.status_code < 300 and not response.text):
                raise PluginException(preset=PluginException.Preset.NOT_FOUND)
            if response.status_code == 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR)
            if response.status_code == 503:
                raise PluginException(preset=PluginException.Preset.SERVICE_UNAVAILABLE)
            if response.status_code >= 400:
                response_data = response.json()
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response_data.get("message", ""))

            if 200 <= response.status_code < 300:
                if "Too many connections" in response.text:
                    raise PluginException(
                        cause="ThreatCrowd server return 'too many connections' error. ",
                        assistance="Please wait and try again.",
                    )
                if full_response:
                    return response

                return response.json()

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as error:
            self.logger.info(f"Invalid JSON: {error}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
        except requests.exceptions.HTTPError as error:
            self.logger.info(f"Call to Thread Crowd failed: {error}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)

    @staticmethod
    def verdict(vote):
        vote_verdict = {1: "Not malicious", 0: "50/50 chance malicious", -1: "Malicious"}
        return vote_verdict[vote]
