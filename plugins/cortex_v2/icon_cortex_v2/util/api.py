from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
from json.decoder import JSONDecodeError
import requests

# Custom imports below
from icon_cortex_v2.util.util import filter_job, filter_job_artifacts, eq_
from typing import Union, Dict, List, Tuple, Any


class API:
    def __init__(self, url: str, api_key: str, verify_cert: bool, proxies: dict):
        self.base_url = f"{url}/api"
        self.api_key = api_key
        self.verify_cert = verify_cert
        self.proxies = proxies

    def send_request(
        self,
        method: str,
        path: str,
        data: Dict[str, Any] = None,
        params: Dict[str, Any] = None,
        files: Dict[str, Any] = None,
    ) -> requests.Response:
        method = method.upper()
        headers = {"Authorization": f"Bearer {self.api_key}"}
        try:
            if method in ["POST", "PATCH"] and not files:
                # Using the json named input parameter automatically sets header Content-Type = application/json
                response = requests.request(
                    method,
                    f"{self.base_url}/{path}",
                    headers=headers,
                    json=data,
                    files=files,
                    params=params,
                    proxies=self.proxies,
                    verify=self.verify_cert,
                )
            else:
                response = requests.request(
                    method,
                    f"{self.base_url}/{path}",
                    headers=headers,
                    data=data,
                    files=files,
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
        except requests.exceptions.ConnectionError as error:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE, data=error)
        except JSONDecodeError as error:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)

    def status(self) -> Dict[str, Any]:
        return self.send_request("GET", "status").json()

    def search(
        self, path, query: Union[str, Dict[str, Any]] = None, range_: str = None, sort_: str = ""
    ) -> Dict[str, Any]:
        path = f"{path}/_search"
        query = {"query": query if query else {}}
        # Simplified of https://github.com/TheHive-Project/Cortex4py/blob/2.1.0/cortex4py/controllers/abstract.py#L16
        params = {"range": range_ if range_ else None, "sort": sort_ if sort_ else None}
        return self.send_request("POST", path, query, params).json()

    def get_analyzer_by_name(self, analyzer_name: str = None) -> Dict[str, Any]:
        return self.search("analyzer", eq_("name", analyzer_name), range_="0-1")[0]

    def get_analyzer_by_id(self, analyzer_id: str = None) -> Dict[str, Any]:
        # If no analyzer_id then return all analyzers
        # Example curl request https://github.com/TheHive-Project/CortexDocs/blob/2.1/api/api-guide.md#list-and-search-1
        endpoint = f"analyzer/{analyzer_id}" if analyzer_id else "analyzer"
        return self.send_request("GET", endpoint).json()

    def get_analyzer_by_type(self, analyzer_type: str = None) -> Dict[str, Any]:
        # Example curl request https://github.com/TheHive-Project/CortexDocs/blob/2.1/api/api-guide.md#get-by-type
        return self.send_request("GET", f"analyzer/type/{analyzer_type}").json()

    def get_analyzers(self) -> Dict[str, Any]:
        return self.get_analyzer_by_id()

    def run_analyzer(
        self, analyzer_id: str, data: Dict[str, Any] = None, files: Dict[str, Tuple] = None
    ) -> Dict[str, Any]:
        return self.send_request(
            "POST", f"analyzer/{analyzer_id}/run", data=data, params={"force": 1}, files=files
        ).json()

    def run_analyzer_by_name(
        self, analyzer_name: str, data: Dict[str, Any] = None, files: Dict[str, Tuple] = None
    ) -> Dict[str, Any]:
        analyzer = self.get_analyzer_by_name(analyzer_name)
        analyzer_id = analyzer.get("id")
        if not analyzer_id:
            raise PluginException(f"Analyzer {analyzer_name} not found")
        job = filter_job(self.run_analyzer(analyzer_id, data, files))
        if not job or not isinstance(job, dict) or "id" not in job:
            raise PluginException(f"Failed to receive job from analyzer {analyzer_name}")
        job["artifacts"] = filter_job_artifacts(self.get_job_artifacts(job.get("id")))
        return job

    def search_for_all_jobs(self, query, range_: str = None, sort_: str = None) -> Dict[str, Any]:
        return self.search("job", query, range_, sort_)

    def get_job_by_id(self, job_id: str = None) -> Dict[str, Any]:
        # If no job_id then return all jobs
        endpoint = f"job/{job_id}" if job_id else "job"
        return self.send_request("GET", endpoint).json()

    def get_jobs(self) -> Dict[str, Any]:
        return self.get_job_by_id()

    def delete_job_by_id(self, job_id: str) -> bool:
        self.send_request("DELETE", f"job/{job_id}")
        # Return true if request did not raise exception
        # https://github.com/TheHive-Project/Cortex4py/blob/2.1.0/cortex4py/api.py#L140
        return True

    def get_job_report(self, job_id: str) -> Dict[str, Any]:
        return self.send_request("GET", f"job/{job_id}/report").json()

    def get_job_artifacts(self, job_id: str) -> List[Dict[str, Any]]:
        return self.send_request("GET", f"job/{job_id}/artifacts").json()
