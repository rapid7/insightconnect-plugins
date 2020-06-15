import insightconnect_plugin_runtime
import requests
from insightconnect_plugin_runtime.exceptions import PluginException
import validators


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

    def search_managed_devices(self, device):
        if validators.uuid(device):
            return list(filter(lambda iter_device: iter_device['userId'] == device or iter_device['id'] == device,
                               self._call_api("GET", f"deviceManagement/managedDevices")["value"]))
        elif validators.email(device):
            filtering_params = ['emailAddress']
        else:
            filtering_params = ['deviceName']
        filtering_params = " or ".join(map(lambda param: f"{param} eq '{device}'", filtering_params))

        return self._call_api("GET", f"deviceManagement/managedDevices?$filter={filtering_params}")["value"]

    def windows_defender_update_signatures(self, managed_device):
        return self._call_api(
            "POST",
            f"deviceManagement/managedDevices/{managed_device}/windowsDefenderUpdateSignatures"
        )

    def windows_defender_scan(self, managed_device):
        return not self._call_api(
            "POST",
            f"deviceManagement/managedDevices/{managed_device}/windowsDefenderScan",
            request_body={"quickScan": False}
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
                "password": self.password
            },
            headers={
                "Content-Type": "application/x-www-form-urlencoded"
            }
        )
        if 200 <= response.status_code < 300:
            token = self._handle_json_to_dict(response)["access_token"]
            self.logger.info(f"Access Token: ********************{str(token[len(token) - 5:len(token)])}")
            return token
        if response.status_code == 400:
            raise PluginException(cause="Could not authenticate user. Please make sure your connection data is valid.",
                                  assistance="If the issue persists please contact support.")

        raise PluginException(preset=PluginException.Preset.UNKNOWN)

    def _call_api(self, method, endpoint, params=None, request_body=None, retry_on_unauthenticated=True):
        response = self._request(
            method,
            self.api_url + endpoint,
            request_body=request_body,
            params=params,
            headers=MicrosoftIntuneAPI.create_necessary_headers(self.access_token)
        )

        if response.status_code == 204:
            return {}
        if 200 <= response.status_code < 300:
            return self._handle_json_to_dict(response)
        elif response.status_code == 400:
            raise PluginException(cause="Bad request. URL or parameters were invalid",
                                  assistance="If the issue persists please contact support.",
                                  data=response.text)
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
        self.logger.info(f"[Calling api] method: {method} url: {url}")

        try:
            return requests.request(
                method,
                url,
                json=request_body and insightconnect_plugin_runtime.helper.clean(request_body),
                params=params and insightconnect_plugin_runtime.helper.clean(params),
                data=data and insightconnect_plugin_runtime.helper.clean(data),
                headers=headers and insightconnect_plugin_runtime.helper.clean(headers)
            )
        except requests.exceptions.RequestException as e:
            self.logger.info(f"Call to API failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN)

    @staticmethod
    def create_necessary_headers(access_token):
        return {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }
