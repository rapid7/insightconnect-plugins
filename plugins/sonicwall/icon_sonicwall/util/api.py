import json
from collections import OrderedDict
from logging import Logger
from typing import Any, Dict, Tuple, Union

import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_sonicwall.util.util import Message


DEFAULT_REQUESTS_TIMEOUT = 30


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
        data = {
            "address_group": {
                group_type: {
                    "name": group_name,
                    "address_object": {object_type: [{"name": object_name}]},
                }
            }
        }
        for payload in [data, {"address_groups": [data.get("address_group", {})]}]:
            try:
                return self._make_request(
                    "PUT",
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
        self, method: str, path: str, *args, commit_pending_changes: bool = False, **kwargs
    ) -> Dict[str, Any]:
        try:
            self.login()
            return self._call_api(method, path, *args, **kwargs)
        finally:
            if commit_pending_changes:
                self._call_api("POST", "config/pending")
                self.logger.info("Pending configuration committed.")
            self.logout()

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
