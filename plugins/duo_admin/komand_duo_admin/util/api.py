import requests
import base64
import hmac
import hashlib
import json
import time
from insightconnect_plugin_runtime.exceptions import PluginException
from logging import Logger
from urllib.parse import quote
from datetime import datetime, timezone
from komand_duo_admin.util.constants import Cause, Assistance
from komand_duo_admin.util.exceptions import ApiException
from komand_duo_admin.util.endpoints import (
    ADMINISTRATOR_LOGS_ENDPOINT,
    AUTHENTICATION_LOGS_ENDPOINT,
    ENROLL_USER_ENDPOINT,
    TRUST_MONITOR_EVENTS_ENDPOINT,
    USER_ENDPOINT,
    USER_PHONES_ENDPOINT,
    USERS_ENDPOINT,
    TASK_PATHS_ALLOW_403,
)


def rate_limiting(max_tries: int):
    def _decorate(func):
        def _wrapper(*args, **kwargs):
            self = args[0]
            if not self.toggle_rate_limiting:
                return func(*args, **kwargs)
            retry = True
            counter, delay = 0, 0
            while retry and counter < max_tries:
                if counter:
                    time.sleep(delay)
                try:
                    retry = False
                    return func(*args, **kwargs)
                except ApiException as error:
                    counter += 1
                    delay = 2 ** (counter * 0.6)
                    if error.cause == PluginException.causes[PluginException.Preset.RATE_LIMIT]:
                        self.logger.info(f"Rate limiting error occurred. Retrying in {delay:.1f} seconds.")
                        retry = True
            return func(*args, **kwargs)

        return _wrapper

    return _decorate


class DuoAdminAPI:
    def __init__(self, hostname: str, integration_key: str, secret_key: str, logger: Logger):
        self.hostname = self._get_hostname(hostname.rstrip("/"))
        self.base_url = f"https://{self.hostname}"
        self._integration_key = integration_key
        self._secret_key = secret_key
        self.logger = logger
        self.toggle_rate_limiting = True

    def _get_hostname(self, hostname):
        return hostname.replace("https://", "").replace("http://", "")

    def add_user(self, params: dict) -> dict:
        return self.make_json_request(method="POST", path=USERS_ENDPOINT, params=params)

    def delete_user(self, user_id: str) -> bool:
        self.make_json_request(method="DELETE", path=USER_ENDPOINT.format(user_id=user_id))
        return True

    def enroll_user(self, params: dict) -> dict:
        return self.make_json_request(method="POST", path=ENROLL_USER_ENDPOINT, params=params)

    def get_users(self) -> dict:
        return self.make_json_request(
            method="GET",
            path=USERS_ENDPOINT,
        )

    def get_user_by_id(self, user_id: str) -> dict:
        return self.make_json_request(
            method="GET",
            path=USER_ENDPOINT.format(user_id=user_id),
        )

    def get_phones_by_user_id(self, user_id: str) -> dict:
        return self.make_json_request(
            method="GET",
            path=USER_PHONES_ENDPOINT.format(user_id=user_id),
        )

    def get_user_by_username(self, params: dict) -> dict:
        return self.make_json_request(
            method="GET",
            path=USERS_ENDPOINT,
            params=params,
        )

    def modify_user(self, user_id: str, params: dict) -> dict:
        return self.make_json_request(
            method="POST",
            path=USER_ENDPOINT.format(user_id=user_id),
            params=params,
        )

    def get_auth_logs(self, parameters: dict) -> dict:
        return self.make_json_request(method="GET", path=AUTHENTICATION_LOGS_ENDPOINT, params=parameters)

    def get_all_auth_logs(self, parameters: dict) -> list:
        auth_logs = []
        page_size = int(parameters.get("limit", 1000))

        results = self.get_auth_logs(parameters).get("response", {})
        auth_logs.extend(results.get("authlogs", []))
        total_objects_left = results.get("metadata", {}).get("total_objects") - page_size

        while total_objects_left > 0:
            parameters["next_offset"] = results.get("metadata", {}).get("next_offset")
            results = self.get_auth_logs(parameters).get("response", {})
            total_objects_left -= page_size
            auth_logs.extend(results.get("authlogs", []))

        return auth_logs

    def get_admin_logs(self, parameters: dict) -> dict:
        return self.make_json_request(method="GET", path=ADMINISTRATOR_LOGS_ENDPOINT, params=parameters)

    def get_trust_monitor_events(self, parameters: dict) -> dict:
        return self.make_json_request(method="GET", path=TRUST_MONITOR_EVENTS_ENDPOINT, params=parameters)

    def get_headers(self, method: str, host: str, path: str, params: dict = {}) -> dict:
        # create canonical string
        now = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S %z")
        canon = [now, method.upper(), host.lower(), path]
        args = []

        for key, values in sorted(params.items()):
            if isinstance(values, str):
                values = [values]
            for value in values:
                value = quote(value.encode("utf-8"), "~")
                args.append(f"{key}={value}")

        canon.append("&".join(args))
        canon = "\n".join(canon)

        # sign canonical string
        sig = hmac.new(bytes(self._secret_key, encoding="utf-8"), bytes(canon, encoding="utf-8"), hashlib.sha1)
        auth = f"{self._integration_key}:{sig.hexdigest()}"
        hmac_signature = base64.b64encode(bytes(auth, encoding="utf-8")).decode()

        return {"Date": now, "Authorization": f"Basic {hmac_signature}"}

    @rate_limiting(10)
    def make_request(self, method: str, path: str, params: dict = {}) -> requests.Response:
        try:
            response = requests.request(
                method=method.upper(),
                url=f"{self.base_url}{path}",
                params=params,
                headers=self.get_headers(method=method.upper(), host=self.hostname, path=path, params=params),
            )
            #TODO Update to 403
            if response.status_code == 403 and path in TASK_PATHS_ALLOW_403:
                # Special case: A task user who only has permissions for certain endpoints should not error out.
                # Log and return empty response instead
                self.logger.info(f"Request to {path} returned 403 unauthorized. Not raising exception as may be authorized to hit other endpoint(s)")
                self.logger.info(f"Response data returned: {response}")
                #return {"response": {"events": [], "metadata": {}}, "stat": "OK"}
                #return "", 200
                response= {
                    "authlogs": [],
                    "metadata": {}
                }
                return response
            self._handle_exceptions(response, path)
            self.logger.info(f"Response data returned: {response.text}")
            if 200 <= response.status_code < 300:
                return response
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except requests.exceptions.HTTPError as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    def _handle_exceptions(self, response, path):
        if response.status_code == 400:
            raise ApiException(
                preset=PluginException.Preset.BAD_REQUEST,
                status_code=response.status_code,
                data=response.text,
            )
        if response.status_code == 401:
            raise ApiException(
                cause=PluginException.causes[PluginException.Preset.API_KEY],
                assistance=Assistance.VERIFY_AUTH,
                status_code=response.status_code,
                data=response.text,
            )
        if response.status_code == 403:
            raise ApiException(
                cause=PluginException.causes[PluginException.Preset.UNAUTHORIZED],
                assistance=Assistance.VERIFY_AUTH,
                status_code=response.status_code,
                data=response.text,
            )
        if response.status_code == 404:
            raise ApiException(
                cause=Cause.NOT_FOUND,
                assistance=Assistance.VERIFY_INPUT,
                status_code=response.status_code,
                data=response.text,
            )
        if response.status_code == 429:
            raise ApiException(
                preset=PluginException.Preset.RATE_LIMIT,
                status_code=response.status_code,
                data=response.text,
            )
        if 400 < response.status_code < 500:
            raise ApiException(
                preset=PluginException.Preset.UNKNOWN,
                status_code=response.status_code,
                data=response.text,
            )
        if response.status_code >= 500:
            raise ApiException(
                cause=Cause.SERVER_ERROR,
                assistance=Assistance.SERVER_ERROR,
                status_code=response.status_code,
                data=response.text,
            )

    def make_json_request(self, method: str, path: str, params: dict = {}) -> dict:
        try:
            self.logger.info(f"Request to path: {path}")
            response = self.make_request(method=method, path=path, params=params)
            self.logger.info(f"response returned DL DEBUG: {response}")
            self.logger.info(f"response.json(): {response.json()}")
            return response.json()
        except json.decoder.JSONDecodeError as error:
            self.logger.info(f"JSON error occurred decoding response from {path}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)
        except Exception as error:
            self.logger.info("Exception thrown")
            self.logger.info(f"Error {error}")

