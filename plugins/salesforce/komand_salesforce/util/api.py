import time
from functools import wraps
from json.decoder import JSONDecodeError
from json import loads
from logging import Logger
from typing import Callable, Any, Tuple

import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_salesforce.util.endpoints import (
    PARAMETERIZED_SEARCH_ENDPOINT,
    QUERY_ENDPOINT,
    QUERY_NEXT_PAGE_ENDPOINT,
    SOBJECT_ENDPOINT,
    SOBJECT_RECORD_ENDPOINT,
    SOBJECT_RECORD_EXTERNAL_ID_ENDPOINT,
    SOBJECT_RECORD_FIELD_ENDPOINT,
    SOBJECT_UPDATED_USERS,
)
from komand_salesforce.util.exceptions import ApiException
from requests.exceptions import ConnectionError as DNSError


def rate_limiting(max_tries: int):
    def _decorate(func):
        def _wrapper(*args, **kwargs):
            self = args[0]
            if not self.enable_rate_limiting:
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


def refresh_token(max_tries: int) -> Callable:
    """
    Decorator to refresh the token if expired and retry the function.

    Args:
    - max_tries (int): Maximum number of attempts to refresh the token and retry.

    Returns:
    - Callable: Wrapped function that retries on token expiry.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(self, *args, **kwargs) -> Any:
            for _ in range(max_tries):
                try:
                    return func(self, *args, **kwargs)
                except ApiException as error:
                    cause = PluginException.causes.get(PluginException.Preset.INVALID_CREDENTIALS)
                    if error.cause == cause and "Session expired or invalid" in error.data:
                        self.logger.info("Token expired, renewing token...")
                        self.token = None
                        self.instance_url = None
                    else:
                        raise
            return func(self, *args, **kwargs)

        return wrapper

    return decorator


class SalesforceAPI:
    RETRY_LIMIT = 2
    QUERY_BATCH_SIZE = 2000

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        oauth_url: str,
        username: str,
        password: str,
        security_token: str,
        logger: Logger,
    ):
        self.logger = logger
        self._client_id = client_id
        self._client_secret = client_secret
        self._oauth_url = oauth_url
        self._username = username
        self._password = password
        self._security_token = security_token
        self.enable_rate_limiting = True
        self.token = None
        self.instance_url = None
        self.retry_count = 1

    def simple_search(self, text: str) -> list:
        return self._make_json_request("GET", PARAMETERIZED_SEARCH_ENDPOINT, params={"q": text}).get(
            "searchRecords", []
        )

    def advanced_search(self, query: str) -> list:
        records = []
        next_query_id = None

        while True:
            if next_query_id:
                response = self._make_json_request("GET", QUERY_NEXT_PAGE_ENDPOINT.format(next_query_id=next_query_id))
            else:
                response = self._make_json_request("GET", QUERY_ENDPOINT, params={"q": query})
            records.extend(response.get("records", []))

            next_records_url = response.get("nextRecordsUrl")
            if next_records_url:
                next_query_id = next_records_url[next_records_url.index("query") + len("query") :]
            else:
                break

        return records

    def query(self, query: str, next_page_id: str = None) -> dict:
        if next_page_id:
            response = self._make_json_request("GET", QUERY_NEXT_PAGE_ENDPOINT.format(next_query_id=next_page_id))
        else:
            response = self._make_json_request("GET", QUERY_ENDPOINT, params={"q": query})

        next_records_url = response.get("nextRecordsUrl")
        return {
            "records": response.get("records", []),
            "next_page_id": (
                next_records_url[next_records_url.index("query") + len("query") :] if next_records_url else None
            ),
        }

    def get_updated_users(self, parameters: dict) -> dict:
        return self._make_json_request("GET", SOBJECT_UPDATED_USERS, params=parameters)

    def create_record(self, object_name: dict, object_data: dict) -> dict:
        return self._make_json_request("POST", SOBJECT_ENDPOINT.format(object=object_name), json=object_data)

    def update_record(self, record_id: str, object_name: dict, object_data: dict) -> bool:
        self._make_request(
            "PATCH", SOBJECT_RECORD_ENDPOINT.format(object=object_name, record=record_id), json=object_data
        )
        return True

    def get_record(self, record_id: str, external_id_field_name: str, object_name: str) -> dict:
        if external_id_field_name:
            url = SOBJECT_RECORD_EXTERNAL_ID_ENDPOINT.format(
                object=object_name, external_id=external_id_field_name, record=record_id
            )
        else:
            url = SOBJECT_RECORD_ENDPOINT.format(object=object_name, record=record_id)

        return self._make_json_request("GET", url)

    def delete_record(self, record_id: str, object_name: dict) -> bool:
        self._make_request("DELETE", SOBJECT_RECORD_ENDPOINT.format(object=object_name, record=record_id))
        return True

    def get_fields(self, record_id: str, object_name: str, fields: dict) -> dict:
        return self._make_json_request(
            "GET", SOBJECT_RECORD_ENDPOINT.format(object=object_name, record=record_id), params=fields
        )

    def get_blob_data(self, record_id: str, object_name: str, field_name: str) -> bytes:
        return self._make_request(
            "GET", SOBJECT_RECORD_FIELD_ENDPOINT.format(object=object_name, record=record_id, field=field_name)
        ).content

    def _get_token(
        self, client_id: str, client_secret: str, username: str, password: str, security_token: str, oauth_url: str
    ):
        # A single task run makes multiple API calls to Salesforce, we can keep the token for one task execution
        if self.token and self.instance_url:
            return self.token, self.instance_url

        salesforce_url = "login.salesforce.com" if not oauth_url else oauth_url.strip("/").replace("https://", "")
        client_url = f"https://{salesforce_url}/services/oauth2/token"

        self.logger.info(f"SalesforceAPI: Getting API token from {client_url}... ")

        try:
            response = requests.request(
                method="POST",
                url=client_url,
                data={
                    "grant_type": "password",
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "username": username,
                    "password": password + security_token,
                },
            )
        except DNSError as error_message:
            self.logger.info(f"Network error or DNS resolution failed: {error_message}")
            raise ApiException(
                cause="Network error or DNS resolution failed. Please check the domain entered",
                assistance="Network error or DNS resolution failed. Please check the domain entered",
                status_code=400,
                data="Network error or DNS resolution failed. Please check the domain entered",
            )

        if 400 <= response.status_code <= 504:
            decoded_response = response.content.decode()
            error_status_code = response.status_code
            cause_error, assistance, status_code = self.get_error(decoded_response)
            if status_code:  # get_error returns status code for invalid creds to avoid a retry
                self.logger.info(
                    f"SalesforceAPI: {cause_error}. Received {error_status_code}, but returning {status_code}. "
                    "Not retrying..."
                )
                preset_error = ""
                error_status_code = status_code  # Salesforce returns 400 but change to 401 to reflect true error code
            else:
                if self.retry_count < self.RETRY_LIMIT:
                    retry_sleep = 5
                    self.logger.info(
                        f"SalesforceAPI: Received {error_status_code} status code. "
                        f"Retrying in {retry_sleep} seconds..."
                    )
                    time.sleep(retry_sleep)
                    self.retry_count += 1
                    return self._get_token(client_id, client_secret, username, password, security_token, oauth_url)
                else:
                    self.logger.error(f"SalesforceAPI: Max retry attempts reached ({self.retry_count}). Exiting...")
                    self.logger.error(
                        f"SalesforceAPI: Unknown error occured after 2 retry attempts: {decoded_response}"
                    )
                    preset_error = "" if cause_error else PluginException.Preset.UNKNOWN

            # reset counter back to 1 so the next task execution can try again - some errors could've persisted for
            # the retry logic and not occur on the next run.
            self.retry_count = 1

            self.logger.error(f"SalesforceAPI: {decoded_response}")
            raise ApiException(
                preset=preset_error,
                cause=cause_error,
                assistance=assistance,
                status_code=error_status_code,
                data=response.text,
            )

        resp_json = response.json()
        access_token = resp_json.get("access_token")
        instance_url = f"{resp_json.get('instance_url')}/services/data/"
        self.logger.info("SalesforceAPI: API token received")
        self.token = access_token
        self.instance_url = instance_url
        self.retry_count = 1  # reset on success also
        return access_token, instance_url

    @staticmethod
    def _get_version(instance_url: str) -> str:
        versions = requests.request(method="GET", url=instance_url).json()
        max_version = next(
            v for v in versions if float(v.get("version")) == max(float(v.get("version")) for v in versions)
        )
        instance_url += "v" + max_version.get("version") + "/"
        return instance_url

    @rate_limiting(10)
    @refresh_token(1)
    def _make_request(self, method: str, url: str, params: dict = {}, json: dict = {}):  # noqa: C901
        access_token, instance_url = self._get_token(
            self._client_id, self._client_secret, self._username, self._password, self._security_token, self._oauth_url
        )
        instance_url = self._get_version(instance_url)
        headers = {"Authorization": f"Bearer {access_token}"}

        if "query" in url:
            # enforce batch size so that task output doesn't exceed IDR limit
            headers["Sforce-Query-Options"] = f"batchSize={self.QUERY_BATCH_SIZE}"

        try:
            response = requests.request(
                url=f"{instance_url}{url}",
                method=method,
                params=params,
                json=json,
                headers=headers,
            )
            if response.status_code == 400:
                raise ApiException(
                    preset=PluginException.Preset.BAD_REQUEST,
                    status_code=response.status_code,
                    data=response.text,
                )
            elif response.status_code == 401:
                raise ApiException(
                    preset=PluginException.Preset.INVALID_CREDENTIALS,
                    status_code=response.status_code,
                    data=response.text,
                )
            elif response.status_code == 403:
                raise ApiException(
                    preset=PluginException.Preset.UNAUTHORIZED,
                    status_code=response.status_code,
                    data=response.text,
                )
            elif response.status_code == 404:
                raise ApiException(
                    preset=PluginException.Preset.NOT_FOUND,
                    status_code=response.status_code,
                    data=response.text,
                )
            elif response.status_code == 429:
                raise ApiException(
                    preset=PluginException.Preset.RATE_LIMIT,
                    status_code=response.status_code,
                    data=response.text,
                )
            elif 400 < response.status_code < 500:
                raise ApiException(
                    preset=PluginException.Preset.UNKNOWN,
                    status_code=response.status_code,
                    data=response.text,
                )
            elif 400 <= response.status_code < 500:
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
            elif response.status_code >= 500:
                raise ApiException(
                    preset=PluginException.Preset.SERVER_ERROR,
                    status_code=response.status_code,
                    data=response.text,
                )
            elif 200 <= response.status_code < 300:
                return response
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except requests.exceptions.HTTPError as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    def _make_json_request(self, method: str, url: str, params: dict = {}, json: dict = {}) -> dict:
        self.logger.info(f"Request to path: {url}")
        try:
            response = self._make_request(method=method, url=url, params=params, json=json)
            return response.json()
        except JSONDecodeError as error:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)

    def unset_token(self) -> None:
        """
        Reset API token now that all API calls have been made during the task execution so that on the next trigger
        we will reach out to Salesforce and get a new API token.
        """
        self.token = None

    def get_error(self, response: str) -> Tuple[str, str, int]:
        """
        Small helper method that takes Salesforce content response and attempts to reflect the best error message
        back to the customer on the UI. First check for invalid credential inputs which we know the error values,
        before checking for an error description to bubble. -> cause_error, assistance, status_code
        """
        error_mappings = {
            "invalid_grant": "Invalid password or security token supplied.",
            "invalid_client_id": "Invalid client ID supplied.",
            "invalid_client": "Invalid client secret supplied.",
            "unsupported_grant_type": "Grant type not supported, Please ensure correct login URL is provided",
        }

        try:
            json_response = loads(response)
            error, error_desc = json_response.get("error"), json_response.get("error_description")
            client_error = error_mappings.get(error)
            if client_error:
                return (
                    f"Salesforce error: '{client_error}'",
                    PluginException.assistances[PluginException.Preset.INVALID_CREDENTIALS],
                    401,
                )
            if error_desc:
                status_code = 0
                if "retry your request" in error_desc:
                    status_code = 500
                return (
                    f"Salesforce error: '{error_desc}'",
                    PluginException.assistances[PluginException.Preset.UNKNOWN],
                    status_code,
                )

        except JSONDecodeError:
            pass

        return "", "", 0
