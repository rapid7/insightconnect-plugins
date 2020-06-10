from re import match

import requests
from insightconnect_plugin_runtime.exceptions import PluginException
import json
import jwt
import uuid
from datetime import datetime, timedelta
from insightconnect_plugin_runtime.helper import clean


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

    def create_blacklist_item(self, payload):
        return self._call_api("POST", f"{self.url}/globallists/v2", "globallist:create", json_data=payload)

    def delete_blacklist_item(self, payload):
        return self._call_api("DELETE", f"{self.url}/globallists/v2", "globallist:delete", json_data=payload)

    def _call_api(self, method, url, scope, params=None, json_data=None):
        token = self.generate_token(self.tenant_id, self.app_id, self.app_secret, scope)
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
                                      assistance="The Tenant ID cannot be retrieved from the JWT token.")
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
                    assistance="Request made conflicts with an existing resource."
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
            self.logger.info(f"Call to Any Run failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)

    def generate_token(self, tenant_id, app_id, app_secret, scope):
        timeout = 1800
        now = datetime.utcnow()
        timeout_datetime = now + timedelta(seconds=timeout)
        claims = {
            "exp": int((timeout_datetime - datetime(1970, 1, 1)).total_seconds()),
            "iat": int((now - datetime(1970, 1, 1)).total_seconds()),
            "iss": "http://cylance.com",
            "sub": app_id,
            "tid": tenant_id,
            "jti": str(uuid.uuid4()),
            "scp": scope
        }

        response = self._make_request(method="POST",
                                      url=f"{self.url}/auth/v2/token",
                                      data=json.dumps({"auth_token": jwt.encode(claims, app_secret,
                                                                                algorithm='HS256').decode(
                                          'utf-8')}),
                                      headers={"Content-Type": "application/json; charset=utf-8"})

        return response['access_token']
