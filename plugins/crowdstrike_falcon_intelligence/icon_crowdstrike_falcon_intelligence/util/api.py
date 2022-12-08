import json
from logging import Logger
from typing import Union

import requests
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_crowdstrike_falcon_intelligence.util.helpers import clean_dict
from icon_crowdstrike_falcon_intelligence.util.endpoints import (
    AUTHENTICATION_ENDPOINT,
    ARTIFACTS_ENDPOINT,
    REPORTS_ENDPOINT,
    REPORTS_QUERY_ENDPOINT,
    REPORT_SUMMARIES_ENDPOINT,
    SUBMISSIONS_ENDPOINT,
    SUBMISSIONS_QUERY_ENDPOINT,
)


class CrowdStrikeAPI:
    def __init__(self, client_id: str, client_secret: str, base_url: str, logger: Logger):
        self._client_id = client_id
        self._client_secret = client_secret
        self._base_url = base_url
        self._logger = logger

    def _get_auth_token(self) -> str:
        self._logger.info("Getting authentication token...")
        response = requests.request(
            method="POST",
            url=self._base_url + AUTHENTICATION_ENDPOINT,
            data={"client_id": self._client_id, "client_secret": self._client_secret},
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        if response.status_code == 201:
            return response.json().get("access_token")

        raise PluginException(preset=PluginException.Preset.API_KEY)

    def get_headers(self) -> dict:
        auth_token = self._get_auth_token()

        headers = {
            "Accepts": "application/json",
            "Authorization": f"Bearer {auth_token}",
        }

        return headers

    def download_artifact(self, artifact_id: str) -> list:
        self._logger.info(f"Downloading an artifact for ID: {artifact_id}...")
        return self.make_json_request(method="GET", url=self._base_url + ARTIFACTS_ENDPOINT, params={"id": artifact_id})

    def get_short_report(self, report_ids: list) -> dict:
        self._logger.info(f"Getting a list of short report summaries for IDs: {report_ids}...")
        response_json = self.make_json_request(
            method="GET", url=self._base_url + REPORT_SUMMARIES_ENDPOINT, params={"ids": report_ids}
        ).get("resources")
        if not response_json:
            raise PluginException(
                cause=f"Reports {report_ids} not found.",
                assistance="Please provide valid report IDs and if the issue persists, contact support.",
            )
        return response_json

    def get_full_report(self, report_ids: list) -> dict:
        self._logger.info(f"Getting a list of report summaries for IDs: {report_ids}...")
        response_json = self.make_json_request(
            method="GET", url=self._base_url + REPORTS_ENDPOINT, params={"ids": report_ids}
        ).get("resources")
        if not response_json:
            raise PluginException(
                cause=f"Reports {report_ids} not found.",
                assistance="Please provide valid report IDs and if the issue persists, contact support.",
            )
        return response_json

    def check_analysis_status(self, analysis_ids: list) -> dict:
        self._logger.info(f"Checking analysis status of IDs: {analysis_ids}...")
        response_json = self.make_json_request(
            method="GET", url=self._base_url + SUBMISSIONS_ENDPOINT, params={"ids": analysis_ids}
        ).get("resources")
        if not response_json:
            raise PluginException(
                cause=f"Analysis {analysis_ids} not found.",
                assistance="Please provide valid analysis IDs and if the issue persists, contact support.",
            )
        return response_json

    def submit_analysis(self, analysis_parameters: dict) -> dict:
        self._logger.info("Submitting analysis...")
        return self.make_json_request(
            method="POST", url=self._base_url + SUBMISSIONS_ENDPOINT, json_data={"sandbox": [analysis_parameters]}
        ).get("resources")[0]

    def get_reports_ids(self, offset: int = None, limit: int = None, filter_query: str = None) -> list:
        self._logger.info("Getting a list of sandbox report IDs...")
        return self.make_json_request(
            method="GET",
            url=self._base_url + REPORTS_QUERY_ENDPOINT,
            params={"limit": limit, "offset": offset, "filter": filter_query},
        ).get("resources")

    def get_submissions_ids(self, offset: int = None, limit: int = None, filter_query: str = None) -> list:
        self._logger.info("Getting a list of submission IDs...")
        return self.make_json_request(
            method="GET",
            url=self._base_url + SUBMISSIONS_QUERY_ENDPOINT,
            params={"limit": limit, "offset": offset, "filter": filter_query},
        ).get("resources")

    def make_request(
        self,
        method: str,
        url: str,
        params: dict = None,
        json_data: dict = None,
    ) -> requests.Response:
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.get_headers(),
                params=clean_dict(params),
                json=clean_dict(json_data),
            )

            if response.status_code == 400:
                raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response.text)
            if response.status_code == 403:
                raise PluginException(
                    cause="Operation is not allowed.",
                    assistance="Please verify inputs and if the issue persists, contact support.",
                    data=response.text,
                )
            if response.status_code == 404:
                raise PluginException(
                    cause="Resource not found.",
                    assistance="Please verify inputs and if the issue persists, contact support.",
                    data=response.text,
                )
            if 400 <= response.status_code < 500:
                raise PluginException(
                    preset=PluginException.Preset.UNKNOWN,
                    data=response.text,
                )
            if response.status_code >= 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)

            if 200 <= response.status_code < 300:
                return response

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except requests.exceptions.HTTPError as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    def make_json_request(
        self, method: str, url: str, params: dict = None, json_data: dict = None
    ) -> Union[list, dict]:
        try:
            response = self.make_request(method=method, url=url, params=params, json_data=json_data)
            return response.json()
        except json.decoder.JSONDecodeError as error:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)
