import insightconnect_plugin_runtime
import requests
from insightconnect_plugin_runtime.exceptions import PluginException
import validators
from typing import Optional


class MicrosoftIntuneAPI:
    def __init__(self, username, password, client_id, client_secret, tenant_id, api_url, logger):
        self.username = username
        self.password = password
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
        self.api_url = api_url
        self.logger = logger
        self.access_token = None

    def add_app_to_policy(self, application_name: str, policy_name: str, device_type: str):
        managed_app_policies = self._call_api("GET", "/deviceAppManagement/managedAppPolicies")
        policy_id = self._filter_policy_id(managed_app_policies, policy_name)

        if not policy_id:
            raise PluginException(
                cause=f"Policy: {policy_name}, was not found.",
                assistance="Contact support for help. See log for more details.",
            )

        managed_app_policies_with_apps = self._call_api(
            "GET", f"deviceAppManagement/{device_type}ManagedAppProtections('{policy_id}')?$expand=apps"
        )
        managed_app_list = self._call_api("GET", "deviceAppManagement/managedAppStatuses('managedAppList')")
        application_package_id = self._filter_app_package_id(managed_app_list, application_name)

        if not application_package_id:
            raise PluginException(
                cause=f"Application: {application_name}, was not found.",
                assistance="Contact support for help. See log for more details.",
            )

        target_apps = []

        for item in managed_app_policies_with_apps["apps"]:
            target_apps.append(
                {
                    "mobileAppIdentifier": {
                        "@odata.type": item["mobileAppIdentifier"]["@odata.type"],
                        "packageId": item["mobileAppIdentifier"]["packageId"],
                    }
                }
            )

        target_apps.append(
            {
                "mobileAppIdentifier": {
                    "@odata.type": f"#microsoft.graph.{device_type}MobileAppIdentifier",
                    "packageId": application_package_id,
                }
            }
        )

        return self._call_api(
            "POST",
            f"deviceAppManagement/{device_type}ManagedAppProtections('{policy_id}')/targetApps",
            request_body={"apps": target_apps},
        )

    def delete_app_from_policy(self, application_name: str, policy_name: str, device_type: str):
        managed_app_policies = self._call_api("GET", "/deviceAppManagement/managedAppPolicies")
        policy_id = self._filter_policy_id(managed_app_policies, policy_name)

        if not policy_id:
            raise PluginException(
                cause=f"Policy: {policy_name}, was not found.",
                assistance="Contact support for help. See log for more details.",
            )

        managed_app_policies_with_apps = self._call_api(
            "GET", f"deviceAppManagement/{device_type}ManagedAppProtections('{policy_id}')?$expand=apps"
        )
        managed_app_list = self._call_api("GET", "deviceAppManagement/managedAppStatuses('managedAppList')")
        application_package_id = self._filter_app_package_id(managed_app_list, application_name)

        if not application_package_id:
            raise PluginException(
                cause=f"Application: {application_name}, was not found.",
                assistance="Contact support for help. See log for more details.",
            )

        target_apps = []

        for item in managed_app_policies_with_apps["apps"]:
            if item["mobileAppIdentifier"]["packageId"] != application_package_id:
                target_apps.append(
                    {
                        "mobileAppIdentifier": {
                            "@odata.type": item["mobileAppIdentifier"]["@odata.type"],
                            "packageId": item["mobileAppIdentifier"]["packageId"],
                        }
                    }
                )

        return self._call_api(
            "POST",
            f"deviceAppManagement/{device_type}ManagedAppProtections('{policy_id}')/targetApps",
            request_body={"apps": target_apps},
        )

    def wipe_managed_device(
        self,
        managed_device_id,
        keep_enrollment_data=None,
        keep_user_data=None,
        mac_os_unlock_code=None,
    ):
        return self._call_api(
            "POST",
            f"deviceManagement/managedDevices/{managed_device_id}/wipe",
            request_body={
                "keepEnrollmentData": keep_enrollment_data,
                "keepUserData": keep_user_data,
                "macOsUnlockCode": mac_os_unlock_code,
            },
        )

    def managed_device_action(self, device_id: str, action: str):
        return self._call_api("POST", f"deviceManagement/managedDevices/{device_id}/{action}")

    def get_managed_app(self, uuid: str) -> list:
        return [self._call_api("GET", f"deviceAppManagement/mobileApps/{uuid}")]

    @staticmethod
    def filter_managed_apps_result(response, app_filter) -> list:
        return list(
            filter(
                lambda iter_app: iter_app.get("displayName", "").lower() == app_filter.lower(),
                response.get("value", []),
            )
        )

    def get_managed_apps_all_pages(self, app_filter: Optional[str]) -> list:
        results = []
        endpoint = "deviceAppManagement/mobileApps?$top=500"
        i = 9999
        while i > 0:
            response = insightconnect_plugin_runtime.helper.clean(self._call_api("GET", endpoint))
            if app_filter:
                results.extend(self.filter_managed_apps_result(response, app_filter))
            else:
                results.extend(response.get("value", []))
            endpoint = response.get("@odata.nextLink", "")
            if not endpoint:
                break
            i -= 1

        return results

    def search_managed_devices(self, device):
        if validators.uuid(device):
            return list(
                filter(
                    lambda iter_device: iter_device["userId"] == device or iter_device["id"] == device,
                    self._call_api("GET", "deviceManagement/managedDevices")["value"],
                )
            )
        elif validators.email(device):
            param = "emailAddress"
        else:
            param = "deviceName"

        value = self._call_api("GET", f"deviceManagement/managedDevices?$filter={param} eq '{device}'")["value"]
        if value:
            return value

        device = device.strip().lower()
        return list(
            filter(
                lambda iter_device: iter_device["emailAddress"].lower() == device
                or iter_device["userPrincipalName"].lower() == device,
                self._call_api("GET", "deviceManagement/managedDevices")["value"],
            )
        )

    def windows_defender_update_signatures(self, managed_device):
        return self._call_api(
            "POST",
            f"deviceManagement/managedDevices/{managed_device}/windowsDefenderUpdateSignatures",
        )

    def windows_defender_scan(self, managed_device):
        return not self._call_api(
            "POST",
            f"deviceManagement/managedDevices/{managed_device}/windowsDefenderScan",
            request_body={"quickScan": False},
        )

    def refresh_access_token(self):
        self.access_token = self._oauth2_get_token()

    def _oauth2_get_token(self):
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
            token = self._handle_json_to_dict(response)["access_token"]
            self.logger.info(f"Access Token: ******************** {str(token[len(token) - 5:len(token)])}")
            return token
        if response.status_code == 400:
            raise PluginException(
                cause="Could not authenticate user. Please make sure your connection data is valid.",
                assistance="If the issue persists please contact support.",
            )

        raise PluginException(preset=PluginException.Preset.UNKNOWN)

    def _call_api(self, method, endpoint, params=None, request_body=None, retry_on_unauthenticated=True):
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
            return self._handle_json_to_dict(response)
        elif response.status_code == 400:
            raise PluginException(
                cause="Bad request. URL or parameters were invalid.",
                assistance="If the issue persists please contact support.",
                data=response.text,
            )
        elif response.status_code == 401 and retry_on_unauthenticated is True:
            self.logger.info("Token expired, reauthenticating...")
            self.refresh_access_token()
            return self._call_api(method, endpoint, params, request_body, retry_on_unauthenticated=False)

        raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)

    def _handle_json_to_dict(self, response):
        try:
            return response.json()
        except ValueError as e:
            self.logger.info(f"Invalid json: {e}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)

    def _request(self, method, url, params=None, request_body=None, headers=None, data=None):
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
        except requests.exceptions.RequestException as e:
            self.logger.info(f"Call to API failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN)

    def get_device_by_uuid_if_not_whitelisted(self, device, whitelist):
        device_response = self.search_managed_devices(device)

        if not device_response:
            raise PluginException(
                cause=f"Managed device: {device}, was not found.",
                assistance="Contact support for help. See log for more details.",
            )
        elif len(device_response) > 1:
            raise PluginException(
                cause=f"Search criteria: {device} returned too many results. Results returned: {len(device_response)}",
                assistance="Contact support for help. See log for more details",
            )

        device_response = device_response[0]
        data_to_look_for_in_whitelist = []
        for key in ["deviceName", "userId", "id", "emailAddress"]:
            data_to_look_for_in_whitelist.append(device_response[key])

        if whitelist and any(item in whitelist for item in data_to_look_for_in_whitelist):
            return {}

        return device_response

    @staticmethod
    def create_necessary_headers(access_token):
        return {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

    def _filter_policy_id(self, managed_app_policies, policy_name):
        for item in managed_app_policies["value"]:
            if item["displayName"] == policy_name:
                return item["id"]
        return None

    def _filter_app_package_id(self, managed_app_list, application_name):
        for item in managed_app_list["content"]["appList"]:
            if item["displayName"] == application_name and "packageId" in item["appIdentifier"]:
                return item["appIdentifier"]["packageId"]
        return None
