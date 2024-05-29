import json
import time
from collections import OrderedDict
from logging import Logger
from typing import Any, Dict, Tuple, Union

import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_sonicwall.util.util import Message


DEFAULT_REQUESTS_TIMEOUT = 30
DEFAULT_MAX_LOGIN_RETRIES = 15


class SonicWallAPI:
    def __init__(self, username: str, password: str, url: str, verify_ssl: bool, port: int, logger: Logger) -> None:
        self.url = f"{url}:{port}/api/sonicos"
        self.verify_ssl = verify_ssl
        self.logger = logger
        self.username = username
        self.password = password

    def login(self) -> None:
        self._call_api("POST", "auth", auth=(self.username, self.password), json_data={"override": True})

    def logout(self) -> None:
        self._call_api("DELETE", "auth", auth=(self.username, self.password))

    def get_group(self, name: str) -> Dict[str, Any]:
        for type_ in ("ipv4", "ipv6"):
            try:
                self.logger.info(f"Looking for group as {type_}...")
                response = self._make_request("GET", f"address-groups/{type_}/name/{name}")
                if response:
                    self.logger.info(f"Group '{name}' has been found. Type: {type_}.")
                    return {"group_object": response, "group_type": type_}
            except PluginException as error:
                if error.preset != PluginException.Preset.UNKNOWN:
                    raise
        raise PluginException(
            cause=Message.ADDRESS_GROUP_NOT_FOUND_CAUSE,
            assistance=Message.ADDRESS_GROUP_NOT_FOUND_ASSISTANCE,
        )

    def get_group_type(self, name: str) -> str:
        return self.get_group(name).get("group_type")

    def get_address_object(self, name: str) -> Union[Dict[str, Any], None]:
        for object_type in ("fqdn", "mac", "ipv6", "ipv4"):
            try:
                self.logger.info(f"Looking for address object as {object_type}...")
                address_object = self._make_request("GET", f"address-objects/{object_type}/name/{name}")
                if address_object:
                    self.logger.info(f"Address object '{name}' has been found.")
                    return {"object_type": object_type, "address_object": address_object}
            except PluginException as error:
                if error.preset != PluginException.Preset.UNKNOWN:
                    raise
        raise PluginException(
            cause=Message.ADDRESS_OBJECT_NOT_FOUND_CAUSE.format(name),
            assistance=Message.ADDRESS_OBJECT_NOT_FOUND_ASSISTANCE,
        )

    def get_object_type(self, name: str) -> str:
        return self.get_address_object(name).get("object_type")

    def add_address_object_to_group(
        self, group_type: str, group_name: str, object_type: str, object_name: str
    ) -> Dict[str, Any]:
        # General payload data structure for SonicWall API less than 7.x.x
        data = {
            "address_group": {
                group_type: {
                    "name": group_name,
                    "address_object": {object_type: [{"name": object_name}]},
                }
            }
        }

        # PUT method in SonicWall API version 7.x.x it behaves as PATCH method, while PATCH behaves as PUT
        # To handle SonicWall API version 6.x.x and 7.x.x I need to handle those two methods as the previous version API
        # Worked fine with PUT method. Also, SonicWall API version 7.x.x has different payload structure
        payload_map = {"PUT": data, "PATCH": {"address_groups": [data.get("address_group", {})]}}
        for method, payload in payload_map.items():
            try:
                return self._make_request(
                    method,
                    f"address-groups/{group_type}/name/{group_name}",
                    json_data=payload,
                    commit_pending_changes=True,
                )
            except PluginException as error:
                if "E_SYNTAX" not in error.data:
                    raise

    def create_address_object(self, object_type: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        if object_type == "cidr":
            object_type = "ipv4"
        self.logger.info("Creating address object...")
        return self._make_request(
            "POST", f"address-objects/{object_type}", json_data=payload, commit_pending_changes=True
        )

    def delete_address_object(self, object_name: str, object_type: str) -> Dict[str, Any]:
        self.logger.info("Deleting the address object...")
        return self._make_request(
            "DELETE", f"address-objects/{object_type}/name/{object_name}", commit_pending_changes=True
        )

    def validate_if_zone_exists(self, zone_name: str) -> bool:
        try:
            if self._make_request("GET", f"zones/name/{zone_name}"):
                return True
        except PluginException as error:
            if error.preset != PluginException.Preset.UNKNOWN:
                raise
            raise PluginException(
                cause=Message.ZONE_NOT_FOUND_CAUSE.format(zone_name=zone_name),
                assistance=Message.ZONE_NOT_FOUND_ASSISTANCE,
                data=error.data,
            )

    def invoke_cli_command(self, payload: str) -> Dict[str, Any]:
        return self._make_request("POST", "direct/cli", data=payload, content_type="text/plain")

    def _make_request(
        self,
        method: str,
        path: str,
        *args,
        commit_pending_changes: bool = False,
        max_tries: int = DEFAULT_MAX_LOGIN_RETRIES,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Constructs and sends an HTTP request to the specified URL path using the given HTTP method. It contains retry
        mechanism as when user logs in using SonicWall API it logs out other sessions for the same account. To allows
        using a couple actions in parallel the retry mechanism has been added.

        :param method: The HTTP method to use for the request (e.g., "GET", "POST").
        :type: str

        :param path: The URL path to which the request should be sent.
        :type: str

        :param args: Additional positional arguments passed to the requests.request.
        :type: tuple

        :param commit_pending_changes: Flag indicating whether to commit any pending changes or not. Defaults to ``False``.
        :type: bool

        :param max_tries: The maximum number of tries to attempt the request in case of failure. Defaults to `DEFAULT_MAX_LOGIN_RETRIES`.
        :type: int

        :param kwargs: Additional keyword arguments passed to the requests.request.
        :type: dict

        :return: A dictionary containing the response data from the server.
        :rtype: Dict[str, Any]

        :raises Exception: If the request fails after the maximum number of tries.
        """

        retry, attempts_counter, error_ = True, 0, None
        while retry and attempts_counter < max_tries:
            try:
                retry = False
                self.login()
                response = self._call_api(method, path, *args, **kwargs)
                if commit_pending_changes:
                    self._call_api("POST", "config/pending")
                    self.logger.info("Pending configuration committed.")
                self.logout()
                return response
            except PluginException as error:
                if error.preset != PluginException.Preset.USERNAME_PASSWORD and "E_LOST_CONN" not in error.data:
                    raise
                attempts_counter += 1
                retry, error_ = True, error
                self.logger.info(f"Retrying to login... ({attempts_counter}/{max_tries})")
                time.sleep(1)
        raise error_

    def _call_api(
        self,
        method: str,
        path: str,
        json_data: Dict[str, Any] = None,
        auth: Tuple[str, str] = None,
        content_type: str = "application/json",
        data: str = None,
    ) -> Dict[str, Any]:
        response = {"text": ""}
        headers = OrderedDict(
            [
                ("Accept", "application/json"),
                ("Content-Type", content_type),
                ("Accept-Encoding", "application/json"),
                ("charset", "UTF-8"),
            ]
        )
        try:
            response = requests.request(
                method,
                f"{self.url}/{path}",
                json=json_data,
                data=data,
                auth=auth,
                headers=headers,
                verify=self.verify_ssl,
                timeout=DEFAULT_REQUESTS_TIMEOUT,
            )

            if response.status_code == 401:
                raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD, data=response.text)
            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.UNAUTHORIZED, data=response.text)
            if (
                response.status_code == 400
                and path == "address-objects/ipv4"
                or path == "address-objects/ipv6"
                or path == "address-objects/fqdn"
            ):
                self.logger.error(
                    "Something unexpected occurred. Check the logs and if the issue persists please contact support."
                )
                return response.json()
            if response.status_code >= 400:
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
            if 200 <= response.status_code < 300:
                return response.json()
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as error:
            self.logger.info(f"Invalid JSON: {error}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
        except requests.exceptions.HTTPError as error:
            self.logger.info(f"Call to SonicWall API failed: {error}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
