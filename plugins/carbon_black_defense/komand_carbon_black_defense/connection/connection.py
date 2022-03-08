import json
from typing import Optional

import insightconnect_plugin_runtime

# Custom imports below
import requests
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import ConnectionSchema, Input


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.job_id = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        self.host = params.get(Input.URL)
        self.token = params.get(Input.API_KEY).get("secretKey")
        self.org_key = params.get(Input.ORG_KEY)
        self.connector = params.get(Input.CONNECTOR)
        self.headers = {"X-Auth-Token": f"{self.token}/{self.connector}"}

    def get_job_id_for_enriched_event(
        self, criteria: dict, exclusions: dict = None, time_range: dict = None
    ) -> Optional[dict]:
        response = self.call_api(
            "POST",
            f"{self.host}/api/investigate/v2/orgs/{self.org_key}/enriched_events/search_jobs",
            json_data={"criteria": criteria, "exclusions": exclusions, "time_range": {"window": time_range}},
        )
        return response.get("job_id")

    def get_enriched_event_status(self, job_id: str = None) -> bool:
        response = self.call_api(
            "GET",
            f"{self.host}/api/investigate/v1/orgs/{self.org_key}/enriched_events/search_jobs/{job_id}",
            json_data={"cb_job_id": job_id},
        )
        contacted = response.get("contacted")
        completed = response.get("completed")
        return contacted and completed and (contacted == completed)

    def retrieve_results_for_enriched_event(self, job_id: str = None) -> Optional[dict]:
        response = self.call_api(
            "GET",
            f"{self.host}/api/investigate/v2/orgs/{self.org_key}/enriched_events/search_jobs/{job_id}/results",
            json_data={"job_id": job_id},
        )

        return response

    def get_job_id_for_detail_search(self, event_ids: str) -> Optional[str]:
        response = self.call_api(
            "POST",
            f"{self.host}/api/investigate/v2/orgs/{self.org_key}/enriched_events/detail_jobs",
            json_data={"event_ids": [event_ids]},
        )

        return response.get("job_id")

    def check_status_of_detail_search(self, job_id: str = None) -> bool:
        response = self.call_api(
            "GET",
            f"{self.host}/api/investigate/v2/orgs/{self.org_key}/enriched_events/detail_jobs/{job_id}",
            json_data={"job_id": job_id},
        )
        contacted = response.get("contacted")
        completed = response.get("completed")
        return contacted and completed and (contacted == completed)

    def retrieve_results_for_detail_search(self, job_id: str) -> dict:
        results = self.call_api(
            "GET",
            f"{self.host}/api/investigate/v2/orgs/{self.org_key}/enriched_events/detail_jobs/{job_id}/results",
            json_data={"job_id": job_id},
        )
        return results

    def call_api(self, method: str, url: str, params: dict = None, data: str = None, json_data: object = None) -> dict:
        try:
            response = requests.request(method, url, headers=self.headers, params=params, data=data, json=json_data)
            if 200 <= response.status_code < 300:
                return response.json()
            if 400 <= response.status_code < 500:
                if response.status_code == 403:
                    raise PluginException(
                        cause=f"Access to resource at {url} is forbidden. The client has authenticated but "
                        f"does not have permission to perform the {method} operation.",
                        assistance="Please ensure the org key is valid.",
                    )
                elif response.status_code == 401:
                    raise PluginException(
                        cause="Either the organization key, API key, or connector ID configured in your connection is "
                        "invalid.",
                        assistance="Please enter valid credentials in the connection.",
                    )
                raise PluginException(
                    preset=PluginException.Preset.UNKNOWN,
                    data=response.text,
                )

            if response.status_code >= 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)

        except json.decoder.JSONDecodeError as e:
            raise PluginException(
                preset=PluginException.Preset.INVALID_JSON,
                data=e,
            )
