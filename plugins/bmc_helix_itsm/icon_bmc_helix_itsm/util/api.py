import json
from logging import Logger
from typing import Union

import requests
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_bmc_helix_itsm.util.constants import (
    TaskRequest,
    IncidentRequest,
    IncidentResponse,
    TaskResponse,
    ProblemResponse,
)
from icon_bmc_helix_itsm.util.helpers import clean_dict
from icon_bmc_helix_itsm.util.endpoints import (
    AUTHENTICATION_ENDPOINT,
    GET_INCIDENT_ENDPOINT,
    CREATE_INCIDENT_ENDPOINT,
    MODIFY_INCIDENT_ENDPOINT,
    CREATE_TASK_ENDPOINT,
    CREATE_PROBLEM_ENDPOINT,
    INCIDENT_QUERY_ENDPOINT,
)


class BmcHelixItsmApi:
    def __init__(self, username_password: dict, base_url: str, ssl_verify: bool, logger: Logger):
        self._username = username_password.get("username")
        self._password = username_password.get("password")
        self._base_url = base_url
        self._ssl_verify = ssl_verify
        self._auth_token = None
        self._logger = logger

    @property
    def auth_token(self) -> str:
        if self._auth_token:
            return self._auth_token
        self._logger.info("Getting authentication token...")
        response = requests.request(
            method="POST",
            url=self._base_url + AUTHENTICATION_ENDPOINT,
            data={"username": self._username, "password": self._password},
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        if response.status_code == 200:
            self._auth_token = response.text
            return self._auth_token
        else:
            raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD)

    @auth_token.setter
    def auth_token(self, auth_token):
        self._auth_token = auth_token

    def get_headers(self) -> dict:
        return {
            "Content-Type": "application/json",
            "Authorization": f"AR-JWT {self.auth_token}",
        }

    def get_incident_entry_id_by_query(self, incident_number: str) -> str:
        response_json = self.make_json_request(
            method="GET",
            url=self._base_url + INCIDENT_QUERY_ENDPOINT,
            params={"q": f"'Incident Number'=\"{incident_number}\""},
        )
        response_entries = response_json.get(IncidentResponse.ENTRIES)
        if not response_entries:
            raise PluginException(
                cause=f"Incident {incident_number} not found.",
                assistance="Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            )
        return response_entries[0].get(IncidentResponse.VALUES, {}).get(IncidentResponse.ENTRY_ID)

    def get_incident(self, incident_number: str, params: dict = None) -> dict:
        self._logger.info(f"Getting details about {incident_number} incident...")
        incident_entry_id = self.get_incident_entry_id_by_query(incident_number)
        url = self._base_url + GET_INCIDENT_ENDPOINT.format(incident_entry_id=incident_entry_id)
        return self.make_json_request(method="GET", url=url, params=params)

    def create_incident(self, incident_params: dict) -> str:
        self._logger.info(f"Creating an incident with following parameters: \n{incident_params}...")
        response = self.make_request(
            method="POST", url=self._base_url + CREATE_INCIDENT_ENDPOINT, json_data={"values": incident_params}
        )
        incident_url = dict(response.headers).get(IncidentResponse.LOCATION)
        incident = self.make_json_request(method="GET", url=incident_url)
        return incident.get(IncidentResponse.VALUES, {}).get(IncidentResponse.INCIDENT_NUMBER)

    def modify_incident(self, incident_number: str, incident_params: dict) -> bool:
        self._logger.info(f"Modifying an {incident_number} incident with following parameters: \n{incident_params}...")
        incident_entry_id = self.get_incident_entry_id_by_query(incident_number)
        self.make_request(
            method="PUT",
            url=self._base_url + MODIFY_INCIDENT_ENDPOINT.format(incident_entry_id=incident_entry_id),
            json_data={"values": incident_params},
        )
        return True

    def get_incident_work_information(self, incident_number: str) -> list:
        self._logger.info(f"Getting work information about {incident_number} incident...")
        response_json = self.get_incident(incident_number, params={"fields": "assoc(HPD:INC:Worklog)"})
        worklogs = []
        for link in response_json.get(IncidentResponse.LINKS, {}).get(IncidentResponse.WORKLOG_LINKS, []):
            worklog = self.make_json_request(method="GET", url=link.get(IncidentResponse.WORKLOG_LINK_HREF))
            worklogs.append(worklog.get(IncidentResponse.WORKLOG_VALUES))
        return worklogs

    def create_task(self, incident_number: str, task_parameters: dict) -> str:
        self._logger.info(
            f"Creating an task related to {incident_number} incident with following parameters: \n{task_parameters}..."
        )
        incident = self.get_incident(incident_number)
        task_parameters[TaskRequest.ROOT_REQUEST_INSTANCE_ID] = incident.get(IncidentResponse.VALUES, {}).get(
            IncidentRequest.INSTANCE_ID
        )
        task_parameters[TaskRequest.ROOT_REQUEST_NAME] = incident_number
        response = self.make_request(
            method="POST",
            url=self._base_url + CREATE_TASK_ENDPOINT,
            json_data={"values": task_parameters},
        )
        task = self.make_json_request(method="GET", url=dict(response.headers).get(TaskResponse.LOCATION))
        return task.get(TaskResponse.VALUES, {}).get(TaskResponse.TASK_ID)

    def create_problem_investigation(self, problem_parameters: dict) -> str:
        self._logger.info(f"Creating a problem investigation with following parameters: \n{problem_parameters}...")
        response = self.make_request(
            method="POST", url=self._base_url + CREATE_PROBLEM_ENDPOINT, json_data={"values": problem_parameters}
        )
        problem = self.make_json_request("GET", dict(response.headers).get(ProblemResponse.LOCATION))
        return problem.get(ProblemResponse.VALUES, {}).get(ProblemResponse.PROBLEM_ID)

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
