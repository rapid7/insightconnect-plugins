import json
from collections import OrderedDict
from logging import Logger
from typing import Any, Dict, Tuple, Union

import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_sonicwall.util.util import Message


class SonicWallAPI:
    def __init__(self, username: str, password: str, url: str, verify_ssl: bool, port: int, logger: Logger) -> None:
        self.url = f"{url}:{port}/api/sonicos/"
        self.verify_ssl = verify_ssl
        self.logger = logger
        self.username = username
        self.password = password

    def login(self) -> None:
        self._call_api("POST", "auth", auth=(self.username, self.password), json_data={"override": True})

    def logout(self) -> None:
        self._call_api("DELETE", "auth", auth=(self.username, self.password))

    def get_object_type(self, name: str) -> str:
        return self.get_address_object(name).get("object_type")

    def get_group(self, name: str) -> Dict[str, Any]:
        urls_to_check = (f"address-groups/ipv4/name/{name}", f"address-groups/ipv6/name/{name}")
        for url in urls_to_check:
            try:
                response = self._make_request("GET", url)
                if response:
                    return response
            except PluginException:
                pass

        raise PluginException(
            cause="The address group does not exist in SonicWall.",
            assistance="Please enter valid names and try again.",
        )

    def get_group_type(self, name: str) -> str:
        group = self.get_group(name)
        for groups in group.get("address_group", {}):
            if "ipv4" in groups:
                return "ipv4"
            elif "ipv6" in groups:
                return "ipv6"

        raise PluginException(
            cause=Message.ADDRESS_GROUP_NOT_FOUND_CAUSE,
            assistance=Message.ADDRESS_GROUP_NOT_FOUND_ASSISTANCE,
        )

    def get_address_object(self, name: str) -> Union[Dict[str, Any], None]:
        self.login()
        for object_type in ["fqdn", "mac", "ipv6", "ipv4"]:
            try:
                address_object = self._call_api("GET", f"address-objects/{object_type}/name/{name}")
                if address_object:
                    return {"object_type": object_type, "address_object": address_object}
            except PluginException:
                continue
        self.logout()
        raise PluginException(
            cause=Message.ADDRESS_GROUP_NOT_FOUND_CAUSE,
            assistance=Message.ADDRESS_GROUP_NOT_FOUND_ASSISTANCE,
        )

    def add_address_object_to_group(self, group_type: str, group_name: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        return self._make_request("PUT", f"address-groups/{group_type}/name/{group_name}", json_data=payload)

    def create_address_object(self, object_type: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        if object_type == "cidr":
            object_type = "ipv4"
        return self._make_request("POST", f"address-objects/{object_type}", json_data=payload)

    def delete_address_object(self, object_name: str, object_type: str) -> Dict[str, Any]:
        return self._make_request("DELETE", f"address-objects/{object_type}/name/{object_name}")

    def validate_if_zone_exists(self, zone_name: str) -> bool:
        self.login()
        try:
            if self._call_api("GET", f"zones/name/{zone_name}"):
                return True
        except PluginException:
            raise PluginException(
                cause=f"The zone: {zone_name} does not exist in SonicWall.",
                assistance="Please enter valid zone name and try again.",
            )
        finally:
            self.logout()

    def invoke_cli_command(self, payload: str) -> Dict[str, Any]:
        self.login()
        try:
            response = self._call_api("POST", "direct/cli", data=payload, content_type="text/plain")
        except PluginException as error:
            raise PluginException(cause=error.cause, assistance=error.assistance, data=error.data)
        finally:
            self.logout()
        return response

    def _make_request(self, method: str, path: str, json_data: Dict[str, Any] = None) -> Dict[str, Any]:
        self.login()
        try:
            response = self._call_api(method, path, json_data)
            self._call_api("POST", "config/pending")
        except PluginException as error:
            raise PluginException(cause=error.cause, assistance=error.assistance, data=error.data)
        finally:
            self.logout()
        return response

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
                self.url + path,
                json=json_data,
                data=data,
                auth=auth,
                headers=headers,
                verify=self.verify_ssl,
            )

            if response.status_code == 401:
                raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD)
            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
            if (
                response.status_code == 400
                and path == "address-objects/ipv4"
                or path == "address-objects/fqdn"
                or path == "address-objects/ipv6"
            ):
                self.logger.error(
                    "Something unexpected occurred. Check the logs and if the issue persists please contact support."
                )
                return response.json()
            if response.status_code >= 400:
                response_data = response.text
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response_data)
            if 200 <= response.status_code < 300:
                return response.json()

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as error:
            self.logger.info(f"Invalid JSON: {error}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
        except requests.exceptions.HTTPError as error:
            self.logger.info(f"Call to SonicWall API failed: {error}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
