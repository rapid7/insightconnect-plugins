import asyncio
import base64
import json
import re
from typing import Any, Dict, List, Union

import aiohttp
import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean

from komand_rapid7_insightidr.connection import Connection
from komand_rapid7_insightidr.util.constants import DEFAULT_ERROR_MESSAGE


def _get_async_session(headers) -> aiohttp.ClientSession:
    """
    Create and return a new aiohttp ClientSession
    :return: aiohttp ClientSession
    """

    return aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(verify_ssl=False), headers=headers
    )


async def get_label_for_id(
    label_id: str, url: str, session: aiohttp.ClientSession
) -> dict:
    response = await session.get(f"{url}log_search/management/labels/{label_id}")
    if response.status == 200:
        try:
            resp_json = await response.json()
            return {"id": label_id, "name": resp_json.get("label", {}).get("name")}
        except json.JSONDecodeError:
            return {}

    return {}


def get_sort_param(input_string: str) -> str:
    """
    Converts input_string to the sort parameters according to the API docs
    :param input_string: Input string that contains parameter name and sort order i.e. Created Time Ascending
    :return: Str ready to be added as a query parameter
    """
    if not input_string:
        return ""
    sort_directions = {"ascending": "ASC", "descending": "DESC"}
    splitted_input_string = input_string.lower().split(" ")
    direction = splitted_input_string.pop()
    output_string = "_".join(splitted_input_string)
    for key, value in sort_directions.items():
        if key == direction:
            output_string += f",{value}"
            break
    return output_string


def convert_list_to_string(list_of_params: List[str]) -> str:
    """
    Converts list of str parameters into str with those names separated by comma
    :param list_of_params: List of str containing parameters
    :return: str containing priority names separated by comma
    """
    if not list_of_params:
        return ""
    return ",".join(list_of_params)


class ResourceHelper(object):
    """
    Class for helper methods for making requests against the InsightAppSec API. A new instance should
    be instantiated within the action/trigger being developed. New methods should be
    created as instance methods to allow reference of the logger and session passed to
    the __init__ function during instantiation.
    """

    _ERRORS = {
        400: "Bad Request",
        401: "Unauthorized",
        404: "Not Found",
        500: "Internal Server Error",
        503: "Service Unavailable",
        000: "Unknown Status Code",
    }

    def __init__(self, session, logger):
        """
        Creates a new instance of ResourceHelper
        :param session: Session object available to Komand actions/triggers, usually self.connection.session
        :param logger: Logger object available to Komand actions/triggers, usually self.logger
        :return: ResourceHelper object
        """
        self.logger = logger
        self.session = session

    def resource_request(
        self,
        endpoint: str,
        method: str = "get",
        params: dict = None,
        payload: dict = None,
    ) -> dict:
        """
        Sends a request to API with the provided endpoint and optional method/payload
        :param endpoint: Endpoint for the API call defined in endpoints.py
        :param method: HTTP method for the API request
        :param params: URL parameters to append to the request
        :param payload: JSON body for the API request if required
        :return: Dict containing the JSON response body
        """
        try:
            request_method = getattr(self.session, method.lower())
            if not params:
                params = {}
            if not payload:
                response = request_method(url=endpoint, params=params, verify=False)
            else:
                response = request_method(
                    url=endpoint, params=params, json=payload, verify=False
                )
        except requests.RequestException as error:
            self.logger.error(error)
            raise
        if response.status_code in range(200, 299):
            resource = response.text
            return {"resource": resource, "status": response.status_code}
        else:
            try:
                error_response = response.json()
                message = error_response.get("message", DEFAULT_ERROR_MESSAGE)
                correlation_id = error_response.get("correlation_id")
            except json.decoder.JSONDecodeError:
                message, correlation_id = DEFAULT_ERROR_MESSAGE, "None"

            status_code_message = self._ERRORS.get(
                response.status_code, self._ERRORS[000]
            )
            self.logger.error(f"The endpoint is {endpoint}")
            self.logger.error(
                f"{status_code_message} (Status Code: {response.status_code}, Correlation ID: {correlation_id}): {message}"
            )
            raise PluginException(
                f"InsightIDR returned a status code of {response.status_code}: {status_code_message}"
            )

    def _handle_response_status(
        self, response: requests.Response, method: str, path: str
    ) -> None:
        """
        Handles the response status code and raises appropriate exceptions
        :param response: Response object from the request
        :param method: string representing the HTTP method used (GET, POST, etc.)
        :param path: string representing the API endpoint path
        :return: None
        """
        if response.status_code == 400:
            raise PluginException(
                preset=PluginException.Preset.BAD_REQUEST, data=response.text
            )
        if response.status_code in [401, 403]:
            raise PluginException(
                preset=PluginException.Preset.API_KEY, data=response.text
            )
        if response.status_code == 404:
            raise PluginException(
                cause="Resource not found.",
                assistance="Verify your input is correct and not malformed and try again. If the issue persists, "
                "please contact support.",
                data=response.text,
            )
        if 400 < response.status_code < 500:
            raise PluginException(
                preset=PluginException.Preset.UNKNOWN, data=response.text
            )
        if response.status_code >= 500:
            raise PluginException(
                preset=PluginException.Preset.SERVER_ERROR, data=response.text
            )
        if response.status_code == 204:
            return response
        if 200 <= response.status_code < 300:
            if (
                method == "GET"
                and "attachments/" in path
                and not path.endswith("/metadata")
            ):
                return response.content
            return clean(response.json())

    def make_request(  # noqa: C901
        self,
        path: str,
        method: str = "GET",
        params: dict = None,
        json_data: dict = None,
        files: dict = None,
    ):
        try:
            response = self.session.request(
                method=method.upper(),
                url=path,
                json=json_data,
                params=params,
                files=files,
            )
            self._handle_response_status(response, method, path)

            raise PluginException(
                preset=PluginException.Preset.UNKNOWN, data=response.text
            )
        except json.decoder.JSONDecodeError as error:
            raise PluginException(
                preset=PluginException.Preset.INVALID_JSON, data=error
            )
        except requests.exceptions.HTTPError as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    def create_comment(self, endpoint: str, json_data: dict):
        self.session.headers["Accept-version"] = "comments-preview"
        return self.make_request(path=endpoint, method="POST", json_data=json_data)

    def delete_comment(self, endpoint: str):
        self.session.headers["Accept-version"] = "comments-preview"
        return self.make_request(path=endpoint, method="DELETE")

    def list_comments(self, endpoint: str, parameters: dict):
        self.session.headers["Accept-version"] = "comments-preview"
        return self.make_request(path=endpoint, params=parameters)

    def list_attachments(self, endpoint: str, parameters: dict):
        self.session.headers["Accept-version"] = "comments-preview"
        return self.make_request(path=endpoint, params=parameters)

    def delete_attachment(self, endpoint: str):
        self.session.headers["Accept-version"] = "comments-preview"
        return self.make_request(path=endpoint, method="DELETE")

    def download_attachment(self, endpoint: str):
        self.session.headers["Accept-version"] = "comments-preview"
        content = self.make_request(path=endpoint)
        return str(base64.b64encode(content), "utf-8")

    def upload_attachment(self, endpoint: str, files: dict):
        self.session.headers["Accept-version"] = "comments-preview"
        return self.make_request(path=endpoint, method="POST", files=files)

    def get_attachment_information(self, endpoint: str):
        self.session.headers["Accept-version"] = "comments-preview"
        return self.make_request(path=endpoint)

    @staticmethod
    def extract_and_fix_json_all_strings(text: str) -> Dict[str, Any]:
        # Extract JSON-like content (enclosed in curly braces)
        match = re.search(r"\{.*}", text, re.DOTALL)
        if not match:
            raise ValueError("No JSON-like fragment found in the input string")

        json_fragment = match.group()

        # Fix broken stringified arrays and unescaped control characters
        def fix_broken_string_arrays_and_control_chars(fragment: str) -> str:
            def replacer(match: re.Match) -> str:
                key = match.group(1)
                raw_value = match.group(2)

                # If it looks like a broken stringified array (["..."])
                if raw_value.startswith('["') and raw_value.endswith('"]'):
                    inner = raw_value[1:-1]
                    inner = inner.replace('"', '\\"')  # Escape inner quotes
                    inner = inner.replace("\n", "\\n").replace(
                        "\r", "\\r"
                    )  # Escape control characters
                    fixed_value = f'"{inner}"'
                    return f'"{key}":{fixed_value}'

                return match.group(0)  # Leave other values unchanged

            # Match fields where the value is a stringified array (possibly malformed)
            pattern = r'"([^"]+)"\s*:\s*"(\[.*?\])"'
            return re.sub(pattern, replacer, fragment, flags=re.DOTALL)

        fixed_json_str = fix_broken_string_arrays_and_control_chars(json_fragment)

        # Attempt to parse the corrected JSON string
        try:
            return json.loads(fixed_json_str)
        except json.decoder.JSONDecodeError:
            return json.loads(json.dumps(fixed_json_str))

    @staticmethod
    async def _get_log_entries_with_labels(
        connection: Connection, log_entries: [dict]
    ) -> [dict]:  # noqa: C901
        label_ids = set()
        for log_entry in log_entries:
            for label in log_entry.get("labels", []):
                label_ids.add(label.get("id"))

        async with _get_async_session(connection.session.headers) as async_session:
            tasks: [asyncio.Future] = []
            for label_id in label_ids:
                tasks.append(
                    asyncio.ensure_future(
                        get_label_for_id(
                            label_id=label_id, url=connection.url, session=async_session
                        )
                    )
                )

            labels = await asyncio.gather(*tasks)

        labels_by_id = {}
        for label in labels:
            if label:
                labels_by_id[label.get("id")] = label.get("name")

        new_log_entries: [dict] = []
        for log_entry in log_entries:
            new_log_entry = dict(log_entry)
            new_log_entry["message"] = ResourceHelper.extract_and_fix_json_all_strings(
                log_entry.get("message", "{}")
            )

            entry_labels = []
            for label in log_entry.get("labels", []):
                label_id = label.get("id")
                if label_id and labels_by_id.get(label_id):
                    entry_labels.append(labels_by_id[label_id])
            new_log_entry["labels"] = entry_labels
            new_log_entries.append(new_log_entry)

        return new_log_entries

    @staticmethod
    def get_log_entries_with_new_labels(
        connection: Connection, log_entries: [dict]
    ) -> [dict]:
        return asyncio.run(
            ResourceHelper._get_log_entries_with_labels(
                connection=connection, log_entries=log_entries
            )
        )
