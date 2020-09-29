from re import match
import requests
from insightconnect_plugin_runtime.exceptions import PluginException
import json
import jwt
import uuid
from datetime import datetime, timedelta
from insightconnect_plugin_runtime.helper import clean
import validators


class CylanceProtectAPI:
    def __init__(self, logger, url, tenant_id, app_id, app_secret):
        self.url = url
        self.tenant_id = tenant_id
        self.app_id = app_id
        self.app_secret = app_secret
        self.logger = logger

    def get_agent_details(self, agent):
        devices = [{}]
        if len(agent) == 36 and match(r"((?:[[\da-fA-F]{8}-([\da-fA-F]{4}-){3}[\da-fA-F]{12}))", agent):
            devices = [self._call_api("GET", f"{self.url}/devices/v2/{agent}", "device:read")]
        elif match(r"((?:[\da-fA-F]{2}[:\-]){5}[\da-fA-F]{2})", agent):
            ret = self._call_api("GET", f"{self.url}/devices/v2/macaddress/{agent}", "device:read")
            if len(ret) > 0:
                devices = ret
        else:
            ret = self._call_api("GET", f"{self.url}/devices/v2/hostname/{agent}", "device:read")
            if len(ret) > 0:
                devices = ret
        if len(devices) > 1:
            self.logger.info(f"Multiple agents found that matched the query: {devices}. We will act upon the first match.")
        return clean(devices[0])

    def search_agents_all(self, agent):
        i = 1
        agents = []
        while i < 9999:
            response = self.get_agents(i, "20")
            if i > response.get('total_pages'):
                break
            agents.extend(self.search_agents(agent, response.get('page_items')))
            i += 1

        if len(agents) == 0:
            raise PluginException(
                cause="Agent not found.",
                assistance=f"Unable to find any agents using identifier provided: {agent}."
            )
            
        return agents

    def search_agents(self, agent: str, device_list: list) -> list:
        agents = []
        if validators.ipv4(agent):
            agents.extend(self.get_device_by_ip(agent, device_list))
        elif match('[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$', agent.lower()):
            agents.extend(self.get_device_by_mac(agent, device_list))
        elif validators.uuid(agent):
            agents.extend(self.get_device_by_id(agent, device_list))
        else:
            agents.extend(self.get_device_by_name(agent, device_list))
        return agents

    @staticmethod
    def get_device_by_ip(ip_address: str, device_list: list) -> list:
        matching_devices = []
        for device in device_list:
            for ip in device.get('ip_addresses'):
                if ip_address == ip:
                    matching_devices.append(device)
        return matching_devices

    @staticmethod
    def get_device_by_mac(mac_address: str, device_list: list) -> list:
        matching_devices = []
        for device in device_list:
            for mac in device.get('mac_addresses'):
                if mac_address.replace(':', '-').upper() == mac:
                    matching_devices.append(device)
        return matching_devices

    @staticmethod
    def get_device_by_id(device_id: str, device_list: list) -> list:
        matching_devices = []
        for device in device_list:
            if device_id.lower() == device.get('id'):
                matching_devices.append(device)
        return matching_devices

    @staticmethod
    def get_device_by_name(name: str, device_list: list) -> list:
        matching_devices = []
        for device in device_list:
            if name.upper() == device.get('name').upper():
                matching_devices.append(device)
        return matching_devices

    def create_blacklist_item(self, payload):
        return self._call_api("POST", f"{self.url}/globallists/v2", "globallist:create", json_data=payload)

    def delete_blacklist_item(self, payload):
        return self._call_api("DELETE", f"{self.url}/globallists/v2", "globallist:delete", json_data=payload)

    def device_lockdown(self, device_id):
        device_id = device_id.replace('-', '').upper()
        return self._call_api("PUT", f"{self.url}/devicecommands/v2/{device_id}/lockdown?value=true", None)

    def get_agents(self, page, page_size):
        return self._call_api("GET", f"{self.url}/devices/v2?page={page}?page_size={page_size}", "device:list")

    def search_threats(self, identifiers):
        threats = self._call_api("GET", f"{self.url}/threats/v2?page=1&page_size=100", "threat:list").get("page_items")
        matching_threats = []
        for identifier in identifiers:
            if match('^[a-fA-F\d]{32}$', identifier):
                for threat in threats:
                    if identifier.upper() == threat.get('md5'):
                        matching_threats.append(threat)
            elif match('^[A-Fa-f0-9]{64}$', identifier):
                for threat in threats:
                    if identifier.upper() == threat.get('sha256'):
                        matching_threats.append(threat)
            else:
                for threat in threats:
                    if identifier.upper() == threat.get('name').upper():
                        matching_threats.append(threat)

        if len(matching_threats) == 0:
            raise PluginException(
                cause="Threat not found.",
                assistance=f"Unable to find any threats using identifier provided: {identifier}."
            )

        return clean(matching_threats)

    def get_threat_devices(self, sha256, page, page_size):
        return self._call_api("GET", f"{self.url}/threats/v2/{sha256}/devices?page={page}?page_size={page_size}", None)

    def update_agent_threat(self, agent_id, payload):
        return self._call_api("POST", f"{self.url}/devices/v2/{agent_id}/threats", "threat:update", json_data=payload)

    def update_agent(self, agent_id, payload):
        return self._call_api("PUT", f"{self.url}/devices/v2/{agent_id}", "device:update", json_data=payload)

    def get_policies(self, page):
        return self._call_api("GET", f"{self.url}/policies/v2?page={page}", "policy:list")

    def _call_api(self, method, url, scope, params=None, json_data=None):
        token = self.generate_token(scope)
        return self._make_request(
            method, url, params, json_data, headers={
                "Authorization": f"Bearer {token}"
            }
        )

    def _make_request(self, method, url, params=None, json_data=None, data=None, headers=None):
        response = {"text": ""}
        try:
            response = requests.request(method, url,
                                        json=json_data,
                                        data=data,
                                        params=params,
                                        headers=headers)

            if response.status_code == 400:
                raise PluginException(cause="Bad request.",
                                      data=response.text)
            if response.status_code == 401:
                raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
            if response.status_code == 403:
                raise PluginException(
                    cause="Forbidden.",
                    assistance="The JWT Token did not contain the proper scope to perform this action."
                )
            if response.status_code == 404:
                raise PluginException(
                    cause="Not found.",
                    assistance="The request was made for a resource that doesn't exist."
                )
            if response.status_code == 409:
                raise PluginException(
                    cause="Conflict.",
                    assistance="Request made conflicts with an existing resource.",
                    data=response.text
                )
            if response.status_code >= 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR)
            if response.status_code >= 400:
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
            if 200 <= response.status_code < 300:
                if response.text:
                    return response.json()
                return {}

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            self.logger.info(f"Invalid json: {e}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Call to CylancePROTECT failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)

    def generate_token(self, scope):
        timeout = 1800
        now = datetime.utcnow()
        timeout_datetime = now + timedelta(seconds=timeout)
        claims = {
            "exp": int((timeout_datetime - datetime(1970, 1, 1)).total_seconds()),
            "iat": int((now - datetime(1970, 1, 1)).total_seconds()),
            "iss": "http://cylance.com",
            "sub": self.app_id,
            "tid": self.tenant_id,
            "jti": str(uuid.uuid4())
        }

        if scope:
            claims["scp"] = scope

        response = self._make_request(method="POST",
                                      url=f"{self.url}/auth/v2/token",
                                      data=json.dumps({"auth_token": jwt.encode(claims, self.app_secret,
                                                                                algorithm='HS256').decode(
                                          'utf-8')}),
                                      headers={"Content-Type": "application/json; charset=utf-8"})

        return response['access_token']
