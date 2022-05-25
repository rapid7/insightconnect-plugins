from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
from json.decoder import JSONDecodeError


import requests


class API:
    def __init__(self, url: str, api_key: str, verify_cert: bool, proxies):
        self.base_url = f"{url}/api"
        self.api_key = api_key
        self.verify_cert = verify_cert
        self.proxies = proxies

    def send_request(self, method: str, path: str, data=None, params=None):
        method = method.upper()
        headers = {"Authorization": f"Bearer {self.api_key}"}
        if method in ["POST", "PATCH"]:
            headers["Content-Type"] = "application/json"
        try:
            response = requests.request(
                method,
                f"{self.base_url}/{path}",
                headers=headers,
                json=data,
                params=params,
                proxies=self.proxies,
                verify=self.verify_cert,
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
            raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE, data=e)
        except JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=e)

    def status(self):
        return self.send_request("GET", "status").json()

    def find_all(self, query, _range=0, _sort=""):
        path = "_search"
        query = {"query": query if query else {}}
        # Simplified of https://github.com/TheHive-Project/Cortex4py/blob/2.1.0/cortex4py/controllers/abstract.py#L16
        params = {"range": _range if _range else None, "sort": _sort if _sort else None}
        return self.send_request("POST", path, query, params).json()

    def get_analyzer_by_id(self, analyzer_id: str = None):
        # If no analyzer_id then return all analyzers
        # Example curl request https://github.com/TheHive-Project/CortexDocs/blob/2.1/api/api-guide.md#list-and-search-1
        endpoint = f"analyzer/{analyzer_id}" if analyzer_id else "analyzer"
        return self.send_request("GET", endpoint).json()

    def get_analyzer_by_type(self, analyzer_type: str = None):
        # Example curl request https://github.com/TheHive-Project/CortexDocs/blob/2.1/api/api-guide.md#get-by-type
        return self.send_request("GET", f"analyzer/type/{analyzer_type}").json()

    def get_analyzers(self):
        return self.get_analyzer_by_id()

    def get_job_by_id(self, job_id: str = None):
        # If no job_id then return all jobs
        endpoint = f"job/{job_id}" if job_id else "job"
        return self.send_request("GET", endpoint).json()

    def get_jobs(self):
        return self.get_job_by_id()

    def delete_job_by_id(self, job_id) -> bool:
        self.send_request("DELETE", f"job/{job_id}")
        # Return true if request did not raise exception
        # https://github.com/TheHive-Project/Cortex4py/blob/2.1.0/cortex4py/api.py#L140
        return True

    def get_job_report(self, job_id):
        return self.send_request("GET", f"job/{job_id}/report").json()
