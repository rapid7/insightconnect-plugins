from insightconnect_plugin_runtime.helper import clean
import requests
from insightconnect_plugin_runtime.exceptions import PluginException
import json
from time import sleep
from logging import Logger
from urllib.parse import urljoin


class CheckPhishAPI:
    def __init__(self, api_key: str, logger: Logger):
        self.base_url = "https://developers.checkphish.ai/api"
        self.headers = {"Content-Type": "application/json"}
        self.api_key = api_key
        self.logger = logger

    def test_api(self):
        return self.submit_scan("https://rapid7.com")

    def submit_scan(self, url: str) -> dict:
        return self.send_request("POST", "/neo/scan/", payload={"urlInfo": {"url": url}})

    def get_scan_results(self, job_id: str) -> dict:
        return self.send_request("POST", "/neo/scan/status", payload={"jobID": job_id, "insights": True})

    def submit_and_get_results(self, url: str) -> dict:
        try:
            job_id = self.submit_scan(url)["jobID"]
        except KeyError:
            raise PluginException(
                cause="Job ID not returned.",
                assistance=f"Failed to retrive scan results for {url} from CheckPhish."
            )
        
        scan_results = self.get_scan_results(job_id)

        i = 0
        while scan_results.get("status") != "DONE" or i == 12:
            sleep(5)
            scan_results = self.get_scan_results(job_id)
            i += 1

        return scan_results

    def send_request(self, method: str, path: str, params: dict = None, payload: dict = None) -> dict:
        if payload:
            payload["apiKey"] = self.api_key
        try:
            response = requests.request(
                method.upper(),
                urljoin(self.base_url, path),
                params=params,
                json=payload,
                headers=self.headers,
            )

            if response.status_code == 401:
                raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD, data=response.text)
            if response.status_code == 403:
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
                return clean(json.loads(response.content))

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=e)
        except requests.exceptions.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)
