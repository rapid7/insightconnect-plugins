import insightconnect_plugin_runtime.exceptions
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
from json.decoder import JSONDecodeError


import requests


class API:
    def __init__(self, url: str, api_key: str, verify_cert: bool, proxies):
        self.base_url = f"{url}/api"
        self.api_key = api_key
        self.verify_cert = verify_cert
        self.proxies = proxies
        self.session = requests.Session()

    def send_request(self, method: str, path: str, params={}, **kwargs):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        try:
            response = self.session.request(
                method.upper(),
                f"{self.base_url}/{path}",
                headers=headers,
                params=params,
                proxies=self.proxies,
                verify=self.verify_cert,
                **kwargs
            )

            if response.status_code == 401:
                # Authentication error. Basic auth with user/pass is deprecated.
                # https://github.com/TheHive-Project/Cortex4py/blob/2.1.0/cortex4py/api.py#L18
                raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.UNAUTHORIZED, data=response.text)
            if response.status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.text)
            if 400 <= response.status_code < 500:
                raise PluginException(
                    preset=PluginException.Preset.UNKNOWN,
                    data=response.text,
                )
            if response.status_code >= 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)

            return response
        except requests.exceptions.ConnectionError as e:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE)
        except JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=e)

    def test_connection(self):
        # List all available analyzers
        return self.send_request("GET", "analyzer").json()

    def find_all(self, query, **kwargs):
        url = f"{self._base_url}/analyzer/_search"
        params = dict((k, kwargs.get(k, None)) for k in ("sort", "range"))
        return self.send_request("POST", url, {"query": query or {}}, params).json()

    def get_jobs_by_id(self, org_id):
        url = f"{self._base_url}/{org_id}"
        return self.send_request("GET", url).json()

    def delete_job_by_id(self, job_id) -> bool:
        self.send_request("DELETE", f"{self._base_url}/{job_id}")
        # Return true if request did not raise exception
        # https://github.com/TheHive-Project/Cortex4py/blob/2.1.0/cortex4py/api.py#L140
        return True
