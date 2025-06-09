from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean
import requests
import json
from icon_rapid7_insightcloudsec.util.helpers import dict_keys_to_camel_case, process_list
from icon_rapid7_insightcloudsec.util.endpoints import (
    CREATE_EXEMPTION_ENDPOINT,
    DELETE_EXEMPTION_ENDPOINT,
    DETACH_POLICY_ENDPOINT,
    GET_RESOURCE_DETAILS_ENDPOINT,
    GET_RESOURCE_ID_ENDPOINT,
    LIST_ORGANIZATIONS_ENDPOINT,
    LIST_RESOURCE_TAGS_ENDPOINT,
    SWITCH_ORGANIZATION_ENDPOINT,
    LIST_CLOUDS,
)


class InsightCloudSecAPI:
    def __init__(self, url: str, api_key: str, ssl_verify: bool, logger):
        self.base_url = url
        self._api_key = api_key
        self.ssl_verify = ssl_verify
        self.logger = logger

    def get_headers(self) -> dict:
        return {"accept": "application/json", "Api-Key": self._api_key}

    def list_organizations(self) -> dict:
        return self.make_json_request(path=LIST_ORGANIZATIONS_ENDPOINT, headers=self.get_headers())

    def switch_organization(self, json_data: dict) -> bool:
        self.make_request(
            path=SWITCH_ORGANIZATION_ENDPOINT,
            method="POST",
            json_data=json_data,
            headers=self.get_headers(),
        )
        return True

    def create_exemption(self, json_data: dict) -> list:
        return process_list(
            self.make_json_request(
                path=CREATE_EXEMPTION_ENDPOINT, method="POST", json_data=json_data, headers=self.get_headers()
            )
        )

    def remove_exemption(self, json_data: dict) -> bool:
        self.make_json_request(
            path=DELETE_EXEMPTION_ENDPOINT, method="POST", json_data=json_data, headers=self.get_headers()
        )
        return True

    def detach_policy(self, resource_id: str, policy_resource_id: str) -> bool:
        self.make_request(
            path=DETACH_POLICY_ENDPOINT.format(resource_id=resource_id, policy_id=policy_resource_id),
            method="POST",
            headers=self.get_headers(),
        )
        return True

    def get_resource_details(self, resource_id: str) -> dict:
        resource_details = self.make_json_request(
            path=GET_RESOURCE_DETAILS_ENDPOINT.format(resource_id=resource_id), headers=self.get_headers()
        )
        return dict_keys_to_camel_case(resource_details)

    def list_resource_tags(self, resource_id: str) -> dict:
        return self.make_json_request(
            path=LIST_RESOURCE_TAGS_ENDPOINT.format(resource_id=resource_id), headers=self.get_headers()
        )

    def get_resource_id(self, json_data: dict) -> dict:
        return dict_keys_to_camel_case(
            self.make_json_request(
                path=GET_RESOURCE_ID_ENDPOINT, method="POST", json_data=json_data, headers=self.get_headers()
            )
        )

    def list_clouds(self, json_data: dict) -> dict:
        return self.make_json_request(path=LIST_CLOUDS, method="POST", json_data=json_data, headers=self.get_headers())

    def make_request(  # noqa: C901
        self,
        path: str,
        method: str = "GET",
        params: dict = None,
        json_data: dict = None,
        data: dict = None,
        headers: dict = None,
    ) -> requests.Response:
        try:
            response = requests.request(
                method=method.upper(),
                url=f"{self.base_url}/v2{path}",
                verify=self.ssl_verify,
                json=json_data,
                params=params,
                data=data,
                headers=headers,
            )
            if response.status_code == 400:
                raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response.text)
            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
            if response.status_code == 404:
                raise PluginException(
                    cause="Resource not found.",
                    assistance="Verify your input is correct and not malformed and try again. If the issue persists, "
                    "please contact support.",
                    data=response.text,
                )
            if 400 < response.status_code < 500:
                raise PluginException(
                    preset=PluginException.Preset.UNKNOWN,
                    data=response.text,
                )
            if response.status_code >= 500:
                raise PluginException(
                    cause="Server error occurred.",
                    assistance="Verify your plugin connection and action inputs are correct and not malformed and try "
                    "again. If the issue persists, please contact support.",
                    data=response.text,
                )
            if 200 <= response.status_code < 300:
                return response

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as error:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)
        except requests.exceptions.HTTPError as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    def make_json_request(
        self,
        path: str,
        method: str = "GET",
        params: dict = None,
        json_data: dict = None,
        data: dict = None,
        headers: dict = None,
    ) -> dict:
        try:
            response = self.make_request(
                path=path, method=method, params=params, json_data=json_data, data=data, headers=headers
            )
            return clean(response.json())
        except json.decoder.JSONDecodeError as error:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)
