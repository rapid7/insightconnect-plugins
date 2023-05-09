import json
import logging
from logging import Logger
import requests
import re
import time
from typing import Union, Callable
from urllib.parse import urlsplit
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import rate_limiting
from komand_okta.util.helpers import clean
from komand_okta.util.endpoints import (
    ADD_USER_TO_GROUP_ENDPOINT,
    ASSIGN_USER_TO_APP_SSO_ENDPOINT,
    DEACTIVATE_USER_ENDPOINT,
    GET_FACTORS_ENDPOINT,
    GET_USER_BY_LOGIN_ENDPOINT,
    GET_ZONES_ENDPOINT,
    LIST_GROUP_ENDPOINT,
    LIST_LOGS_ENDPOINT,
    REMOVE_USER_FROM_GROUP_ENDPOINT,
    RESET_FACTORS_ENDPOINT,
    RESET_PASSWORD_ENDPOINT,
    SEND_PUSH_ENDPOINT,
    SUSPEND_USER_ENDPOINT,
    UNSUSPEND_USER_ENDPOINT,
    UPDATE_ZONE_ENDPOINT,
    USER_ENDPOINT,
    USERS_ENDPOINT,
    USERS_IN_GROUP_ENDPOINT,
    GROUP_ENDPOINT,
)


class OktaAPI:
    def __init__(self, okta_key: str, okta_url: str, logger: Logger):
        self.logger = logger
        self._okta_key = okta_key
        self.base_url = okta_url

    def get_headers(self) -> dict:
        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"SSWS {self._okta_key}",
        }

    def get_user_id(self, login: str) -> str:
        user_id = self.make_json_request(method="GET", url=GET_USER_BY_LOGIN_ENDPOINT.format(login=login)).get("id")
        if user_id:
            return user_id
        raise PluginException(
            cause="User with given login not found.",
            assistance=f"Please check if the given login {login} is correct and try again.",
        )

    def get_zones(self) -> list:
        return self.make_json_request(method="GET", url=GET_ZONES_ENDPOINT)

    def update_zone(self, zone_id: str, json_data: dict) -> dict:
        return self.make_json_request(
            method="PUT", url=UPDATE_ZONE_ENDPOINT.format(zone_id=zone_id), json_data=json_data
        )

    def add_user_to_group(self, user_id: str, group_id: str) -> bool:
        self.make_request(method="PUT", url=ADD_USER_TO_GROUP_ENDPOINT.format(user_id=user_id, group_id=group_id))
        return True

    def assign_user_to_app_sso(self, app_id: str, parameters: dict) -> dict:
        return self.make_json_request(
            method="POST", url=ASSIGN_USER_TO_APP_SSO_ENDPOINT.format(app_id=app_id), json_data=parameters
        )

    def deactivate_user(self, user_id: str) -> bool:
        self.make_request(method="POST", url=DEACTIVATE_USER_ENDPOINT.format(user_id=user_id))
        return True

    def delete_user(self, user_id: str, send_admin_email: bool) -> bool:
        self.make_request(
            method="DELETE", url=USER_ENDPOINT.format(user_id=user_id), params={"sendEmail": send_admin_email}
        )
        return True

    def get_factors(self, user_id: str) -> list:
        return self.make_json_request(method="GET", url=GET_FACTORS_ENDPOINT.format(user_id=user_id))

    def get_user(self, user_id: str) -> dict:
        return self.make_json_request(method="GET", url=USER_ENDPOINT.format(user_id=user_id))

    def list_events(self, parameters: dict) -> requests.Response:
        return self.make_request(method="GET", url=LIST_LOGS_ENDPOINT, params=parameters)

    def get_all_pages(self, response: requests.Response) -> list:
        returned_data = response.json()
        links = response.headers.get("link").split(", ")
        next_link = None
        for link in links:
            matched_link = re.match("<(.*?)>", link) if 'rel="next"' in link else None
            next_link = matched_link.group(1) if matched_link else None
        if next_link:
            self.logger.info("Getting the next page of results...")
            returned_data.extend(self.get_all_pages(self.make_request(method="GET", url=self.split_url(next_link))))
        return returned_data

    def list_groups(self, parameters: dict = None) -> dict:
        return self.make_json_request(method="GET", url=LIST_GROUP_ENDPOINT, params=parameters)

    def send_push(self, user_id: str, factor_id: str) -> dict:
        return self.make_json_request(
            method="POST", url=SEND_PUSH_ENDPOINT.format(user_id=user_id, factor_id=factor_id)
        )

    def remove_user_from_group(self, user_id: str, group_id: str) -> bool:
        self.make_request(
            method="DELETE", url=REMOVE_USER_FROM_GROUP_ENDPOINT.format(user_id=user_id, group_id=group_id)
        )
        return True

    def reset_factors(self, user_id: str) -> bool:
        self.make_json_request(method="POST", url=RESET_FACTORS_ENDPOINT.format(user_id=user_id))
        return True

    def reset_password(self, user_id: str, parameters: dict) -> dict:
        return self.make_json_request(
            method="POST", url=RESET_PASSWORD_ENDPOINT.format(user_id=user_id), params=parameters
        )

    def suspend_user(self, user_id: str) -> dict:
        return self.make_json_request(method="POST", url=SUSPEND_USER_ENDPOINT.format(user_id=user_id))

    def unsuspend_user(self, user_id: str) -> dict:
        return self.make_json_request(method="POST", url=UNSUSPEND_USER_ENDPOINT.format(user_id=user_id))

    def verify_poll_status(self, link: str) -> dict:
        return self.make_json_request(method="GET", url=link.replace(self.base_url, ""))

    def create_user(self, query_params: dict, parameters: dict) -> dict:
        return self.make_json_request(method="POST", url=USERS_ENDPOINT, params=query_params, json_data=parameters)

    def get_group(self, group_id: str) -> dict:
        return self.make_json_request(method="GET", url=GROUP_ENDPOINT.format(group_id=group_id))

    def get_users_in_group(self, group_id: str) -> requests.Response:
        return self.make_request(method="GET", url=USERS_IN_GROUP_ENDPOINT.format(group_id=group_id))

    @rate_limiting(10)
    def make_request(self, method: str, url: str, json_data: dict = None, params: dict = None) -> requests.Response:
        try:
            response = requests.request(
                method=method, url=f"{self.base_url}{url}", headers=self.get_headers(), json=json_data, params=params
            )

            if response.status_code == 400:
                raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response.text)
            if response.status_code in [401, 403]:
                raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
            if response.status_code == 404:
                raise PluginException(
                    cause="Resource not found.",
                    assistance="Verify your input is correct and not malformed and try again. If the issue persists, "
                    "please contact support.",
                    data=response.text,
                )
            if response.status_code == 429:
                raise PluginException(preset=PluginException.Preset.RATE_LIMIT, data=response.text)
            if 400 < response.status_code < 500:
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
            if response.status_code >= 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)
            if 200 <= response.status_code < 300:
                return response

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except requests.exceptions.HTTPError as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    def make_json_request(
        self, method: str, url: str, json_data: dict = None, params: dict = None
    ) -> Union[dict, list]:
        try:
            response = self.make_request(method=method, url=url, json_data=json_data, params=params)
            return clean(response.json())
        except json.decoder.JSONDecodeError as error:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)

    @staticmethod
    def split_url(url: str) -> str:
        scheme, netloc, paths, queries, fragments = urlsplit(url.strip())  # pylint: disable=unused-variable
        return f"{paths}?{queries}"
