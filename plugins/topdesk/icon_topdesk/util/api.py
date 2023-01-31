import json
from logging import Logger
import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from typing import Union
from icon_topdesk.util.helpers import clean
from icon_topdesk.util.endpoints import (
    INCIDENTS_ENDPOINT,
    INCIDENT_ENDPOINT_GET_BY_ID,
    INCIDENT_ENDPOINT_GET_BY_NUMBER,
    OPERATOR_GROUPS_ENDPOINT,
    OPERATORS_ENDPOINT,
    SUPPLIERS_ENDPOINT,
    LOCATIONS_ENDPOINT,
)
from icon_topdesk.util.constants import Cause, Assistance


class TopDeskAPI:
    def __init__(self, credentials: dict, domain: str, logger: Logger):
        self._auth = (credentials.get("username"), credentials.get("password"))
        self._domain = domain
        self._headers = {"Content-Type": "application/json"}
        self._logger = logger

    def get_incidents(self, parameters: dict = None) -> list:
        return self.make_json_request(
            method="GET",
            url=INCIDENTS_ENDPOINT.format(domain=self._domain),
            headers=self._headers,
            params=parameters,
        )

    def create_incident(self, parameters: dict = None) -> dict:
        return self.make_json_request(
            method="POST",
            url=INCIDENTS_ENDPOINT.format(domain=self._domain),
            headers=self._headers,
            json_data=parameters,
        )

    def get_incident_by_id(self, incident_id: str) -> dict:
        return self.make_json_request(
            method="GET",
            url=INCIDENT_ENDPOINT_GET_BY_ID.format(domain=self._domain, id=incident_id),
            headers=self._headers,
        )

    def update_incident_by_id(self, incident_id: str, payload: dict) -> dict:
        return self.make_json_request(
            method="PATCH",
            url=INCIDENT_ENDPOINT_GET_BY_ID.format(domain=self._domain, id=incident_id),
            headers=self._headers,
            json_data=payload,
        )

    def get_incident_by_number(self, incident_number: str) -> dict:
        return self.make_json_request(
            method="GET",
            url=INCIDENT_ENDPOINT_GET_BY_NUMBER.format(domain=self._domain, number=incident_number),
            headers=self._headers,
        )

    def update_incident_by_number(self, incident_number: str, payload: dict) -> dict:
        return self.make_json_request(
            method="PATCH",
            url=INCIDENT_ENDPOINT_GET_BY_NUMBER.format(domain=self._domain, number=incident_number),
            headers=self._headers,
            json_data=payload,
        )

    def get_operators(self, parameters: dict) -> list:
        return self.make_json_request(
            method="GET", url=OPERATORS_ENDPOINT.format(domain=self._domain), headers=self._headers, params=parameters
        )

    def get_operator_groups(self, parameters: dict) -> list:
        return self.make_json_request(
            method="GET",
            url=OPERATOR_GROUPS_ENDPOINT.format(domain=self._domain),
            headers=self._headers,
            params=parameters,
        )

    def get_suppliers(self, parameters: dict = None) -> dict:
        return self.make_json_request(
            method="GET",
            url=SUPPLIERS_ENDPOINT.format(domain=self._domain),
            headers=self._headers,
            params=parameters,
        )

    def list_locations_and_branches(self, parameters: dict = None) -> dict:
        return self.make_json_request(
            method="GET", url=LOCATIONS_ENDPOINT.format(domain=self._domain), params=parameters, headers=self._headers
        )

    def make_request(
        self, method: str, url: str, headers: dict, params: dict = None, json_data: dict = None
    ) -> requests.Response:
        try:
            response = requests.request(
                method=method,
                url=url,
                auth=self._auth,
                headers=headers,
                params=params,
                json=json_data,
            )

            if response.status_code == 400:
                raise PluginException(
                    cause=Cause.INVALID_REQUEST,
                    assistance=Assistance.VERIFY_INPUT,
                    data=response.text,
                )
            if response.status_code == 401:
                raise PluginException(
                    cause=Cause.INVALID_CREDENTIALS,
                    assistance=Assistance.VERIFY_CREDENTIALS,
                    data=response.text,
                )
            if response.status_code == 403:
                raise PluginException(
                    cause=Cause.NOT_ENOUGH_PERMISSIONS,
                    assistance=Assistance.VERIFY_CREDENTIALS,
                    data=response.text,
                )
            if response.status_code == 404:
                raise PluginException(
                    cause=Cause.NOT_FOUND,
                    assistance=Assistance.VERIFY_INPUT,
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
        except requests.exceptions.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)

    def make_json_request(
        self,
        method: str,
        url: str,
        headers: dict = None,
        params: dict = None,
        json_data: dict = None,
    ) -> Union[dict, list]:
        try:
            response = self.make_request(method=method, url=url, params=params, json_data=json_data, headers=headers)
            if response.status_code == 204:
                return []
            return clean(response.json())
        except json.decoder.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=e)
