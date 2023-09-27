import insightconnect_plugin_runtime
import requests
import validators
import json
from insightconnect_plugin_runtime.exceptions import PluginException
from logging import Logger
from typing import Optional

from icon_microsoft_intune.util.constants import (
    GET_AUTOPILOT_DEVICE_ENDPOINT,
    GET_MANAGED_APP_ENDPOINT,
    GET_MANAGED_APPS_ENDPOINT,
    GET_MANAGED_DEVICE_ENDPOINT,
    GET_MANAGED_DEVICES_ENDPOINT,
    MANAGED_DEVICE_ACTION_ENDPOINT,
    SCAN_DEVICE_ENDPOINT,
    WINDOWS_AUTOPILOT_DEVICE_ENDPOINT,
    WINDOWS_DEFENDER_SIGNATURES_ENDPOINT,
    WIPE_DEVICE_ENDPOINT,
)


class MicrosoftIntuneAPI:
    def __init__(
        self,
        username: str,
        password: str,
        client_id: str,
        client_secret: str,
        tenant_id: str,
        api_url: str,
        logger: Logger,
    ):
        self.username = username
        self.password = password
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
        self.api_url = api_url
        self.logger = logger
        self.access_token = None

    def wipe_managed_device(
        self,
        managed_device_id: str,
        keep_enrollment_data: bool = None,
        keep_user_data: bool = None,
        mac_os_unlock_code: str = None,
    ) -> bool:
        self._call_api(
            "POST",
            WIPE_DEVICE_ENDPOINT.format(device_id=managed_device_id),
            request_body={
                "keepEnrollmentData": keep_enrollment_data,
                "keepUserData": keep_user_data,
                "macOsUnlockCode": mac_os_unlock_code,
            },
        )
        return True

    def managed_device_action(self, device_id: str, action: str) -> bool:
        self._call_api("POST", MANAGED_DEVICE_ACTION_ENDPOINT.format(device_id=device_id, action=action))
        return True

    def get_managed_app(self, uuid: str) -> list:
        return [self._call_api("GET", GET_MANAGED_APP_ENDPOINT.format(app_id=uuid))]

    @staticmethod
    def filter_managed_apps_result(response: dict, app_filter: str) -> list:
        return list(
            filter(
                lambda iter_app: iter_app.get("displayName", "").lower() == app_filter.lower(),
                response.get("value", []),
            )
        )

    def get_managed_apps_all_pages(self, app_filter: Optional[str]) -> list:
        results = []
        response = self._call_api("GET", GET_MANAGED_APPS_ENDPOINT, params={"$top": 500})
        for _ in range(9999):
            if app_filter:
                results.extend(self.filter_managed_apps_result(response, app_filter))
            else:
                results.extend(response.get("value", []))
            endpoint = response.get("@odata.nextLink", "")
            if endpoint:
                response = self._call_api("GET", endpoint)
            else:
                break
        return results

    def search_managed_devices(self, device: str) -> list:
        if validators.uuid(device):
            return list(
                filter(
                    lambda iter_device: device in [iter_device.get("userId"), iter_device.get("id")],
                    self._call_api("GET", GET_MANAGED_DEVICES_ENDPOINT).get("value", []),
                )
            )
        elif validators.email(device):
            filters = {"$filter": f"emailAddress eq '{device}'"}
        else:
            filters = {"$filter": f"deviceName eq '{device}'"}

        value = self._call_api("GET", GET_MANAGED_DEVICES_ENDPOINT, params=filters).get("value", [])
        if value:
            return value

        device = device.strip().lower()
        return list(
            filter(
                lambda iter_device: device
                in [iter_device.get("emailAddress").lower(), iter_device.get("userPrincipalName").lower()],
                self._call_api("GET", GET_MANAGED_DEVICES_ENDPOINT).get("value", []),
            )
        )

    def windows_defender_update_signatures(self, managed_device: str) -> bool:
        self._call_api("POST", WINDOWS_DEFENDER_SIGNATURES_ENDPOINT.format(device_id=managed_device))
        return True

    def windows_defender_scan(self, managed_device: str, quick_scan: bool) -> bool:
        self._call_api(
            "POST", SCAN_DEVICE_ENDPOINT.format(device_id=managed_device), request_body={"quickScan": quick_scan}
        )
        return True

    def refresh_access_token(self):
        self.access_token = self._oauth2_get_token()

    def _oauth2_get_token(self) -> str:
        response = self._request(
            "POST",
            f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token",
            data={
                "grant_type": "password",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "scope": "https://graph.microsoft.com/.default",
                "username": self.username,
                "password": self.password,
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        if 200 <= response.status_code < 300:
            token = self._handle_json_to_dict(response).get("access_token")
            self.logger.info(f"Access Token: ******************** {str(token[len(token) - 5:len(token)])}")
            return token
        self.raise_for_status(response)

    def _call_api(
        self,
        method: str,
        endpoint: str,
        params: dict = None,
        request_body: dict = None,
        retry_on_unauthenticated: bool = True,
    ) -> dict:
        if not endpoint.startswith("https"):
            endpoint = self.api_url + endpoint
        response = self._request(
            method,
            endpoint,
            request_body=request_body,
            params=params,
            headers=MicrosoftIntuneAPI.create_necessary_headers(self.access_token),
        )
        if response.status_code == 204:
            return {}
        if 200 <= response.status_code < 300:
            if method.lower() == "delete":
                return {}
            return self._handle_json_to_dict(response)
        if response.status_code == 401 and retry_on_unauthenticated is True:
            self.logger.info("Token expired, reauthenticating...")
            self.refresh_access_token()
            return self._call_api(method, endpoint, params, request_body, retry_on_unauthenticated=False)
        self.raise_for_status(response)
        raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)

    def _handle_json_to_dict(self, response: requests.Response) -> dict:
        try:
            return response.json()
        except json.decoder.JSONDecodeError as error:
            self.logger.error(f"Invalid json: {error}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)

    def _request(
        self,
        method: str,
        url: str,
        params: dict = None,
        request_body: dict = None,
        data: dict = None,
        headers: dict = None,
    ) -> requests.Response:
        self.logger.debug(f"[Calling API] method: {method}, url: {url}")

        try:
            return requests.request(
                method,
                url,
                json=request_body and insightconnect_plugin_runtime.helper.clean(request_body),
                params=params and insightconnect_plugin_runtime.helper.clean(params),
                data=data and insightconnect_plugin_runtime.helper.clean(data),
                headers=headers and insightconnect_plugin_runtime.helper.clean(headers),
            )
        except requests.exceptions.RequestException as error:
            self.logger.error(f"Call to API failed: {error}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    def get_device_by_uuid_if_not_whitelisted(self, device: str, whitelist: list) -> dict:
        device_response = self.search_managed_devices(device)

        if not device_response:
            raise PluginException(
                cause=f"Managed device '{device}' was not found.",
                assistance="Check if the provided input is correct and try again.",
            )
        elif len(device_response) > 1:
            raise PluginException(
                cause=f"Search criteria '{device}' returned too many results. Results returned: {len(device_response)}.",
                assistance="Check if the provided input is correct and try again.",
            )

        device_response = device_response[0]
        data_to_look_for_in_whitelist = []
        for key in ["deviceName", "userId", "id", "emailAddress"]:
            data_to_look_for_in_whitelist.append(device_response.get(key))

        if whitelist and any(item in whitelist for item in data_to_look_for_in_whitelist):
            return {}

        return device_response

    @staticmethod
    def create_necessary_headers(access_token):
        return {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

    @staticmethod
    def raise_for_status(response: requests.Response):
        if response.status_code == 401:
            raise PluginException(
                cause="Invalid tenant ID, application ID or application secret provided.",
                assistance="Verify your connection inputs are correct and try again.",
                data=response.text,
            )
        elif response.status_code == 403:
            raise PluginException(
                preset=PluginException.Preset.UNAUTHORIZED,
                data=response.text,
            )
        elif response.status_code == 404:
            raise PluginException(
                cause="Resource not found.",
                assistance="Please provide valid inputs and try again.",
                data=response.text,
            )
        elif response.status_code == 400:
            raise PluginException(
                preset=PluginException.Preset.BAD_REQUEST,
                data=response.text,
            )
        elif response.status_code == 429:
            raise PluginException(
                preset=PluginException.Preset.RATE_LIMIT,
                data=response.text,
            )
        elif 400 < response.status_code < 500:
            raise PluginException(
                preset=PluginException.Preset.UNKNOWN,
                data=response.text,
            )
        elif response.status_code >= 500:
            raise PluginException(
                preset=PluginException.Preset.SERVER_ERROR,
                data=response.text,
            )

    def get_device(self, device_id: str) -> dict:
        return self._call_api(
            "GET",
            GET_MANAGED_DEVICE_ENDPOINT.format(device_id=device_id),
        )

    def get_autopilot_device(self, device_id: str) -> dict:
        return self._call_api(
            "GET",
            GET_AUTOPILOT_DEVICE_ENDPOINT.format(device_id=device_id),
        )

    def delete_device_from_intune(self, device_id: str) -> bool:
        self._call_api("DELETE", GET_MANAGED_DEVICE_ENDPOINT.format(device_id=device_id))
        return True

    def delete_device_from_autopilot(self, device_id: str) -> bool:
        self._call_api("DELETE", WINDOWS_AUTOPILOT_DEVICE_ENDPOINT.format(device_id=device_id))
        return True
