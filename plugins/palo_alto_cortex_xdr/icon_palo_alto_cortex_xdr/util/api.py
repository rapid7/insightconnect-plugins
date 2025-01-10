import json
import time
import secrets
import string
import hashlib
from typing import List, Dict, Tuple

import requests
import urllib

from re import match
from datetime import datetime, timezone
from icon_palo_alto_cortex_xdr.util.util import Util
from insightconnect_plugin_runtime.exceptions import (
    PluginException,
    ConnectionTestException,
    ResponseExceptionData,
    HTTPStatusCodes,
    APIException,
)
from insightconnect_plugin_runtime.helper import extract_json, make_request
from requests import Response


class CortexXdrAPI:
    ENDPOINT_ID_TYPE = "endpoint_id_list"
    ENDPOINT_IP_TYPE = "ip_list"
    ENDPOINT_HOSTNAME_TYPE = "hostname"
    DEFAULT_TIMEOUT = 120

    def __init__(self, api_key_id, api_key, fully_qualified_domain_name, security_level, logger):
        # Disable all the too-many-arguments violations in this function.
        # pylint: disable=too-many-arguments
        self.api_key_id = api_key_id
        self.api_key = api_key
        self.fully_qualified_domain_name = fully_qualified_domain_name
        self.logger = logger
        if security_level == "Advanced":
            self.headers = self._advanced_authentication(self.api_key_id, self.api_key)
        else:
            self.headers = self._standard_authentication(self.api_key_id, self.api_key)

    def get_headers(self):
        return self.headers

    def get_url(self):
        return self.fully_qualified_domain_name

    def test_connection(self):
        endpoint = "/api_keys/validate/"
        try:
            self._post_to_api(endpoint, {})
        except Exception as error:
            raise ConnectionTestException(
                cause="Connection Test Failed.",
                assistance="Please check your connection settings and try again.",
                data=error,
            )

    @Util.retry(tries=1, timeout=900, exceptions=PluginException, backoff_seconds=1)
    def start_xql_query(self, query, tenants, start_time_range=None, end_time_range=None) -> int:
        start_xql_query_endpoint = "/public_api/v1/xql/start_xql_query/"
        # Check if 'start_time_range' and 'end_time_range' are present, default to current Unix epoch time if absent
        # Validate 'start_time_range' and 'end_time_range' fields
        current_date_time = int(time.time() * 1000)
        if not start_time_range or not end_time_range:
            time_frame = None
        elif (
            start_time_range >= end_time_range
            or start_time_range > current_date_time
            or end_time_range > current_date_time
            or start_time_range < 1
            or end_time_range < 1
        ):
            raise PluginException(
                cause="Invalid 'Start Time' or 'End Time' time range inputs",
                assistance="'Start Time' or 'End Time' must be valid Unix timestamps in epoch milliseconds, they must be past "
                "timestamps, and 'End Time' must be more recent than 'Start Time'",
                data=f"'From'= {start_time_range}, 'To'= {end_time_range}",
            )
        else:
            time_frame = {"from": start_time_range, "to": end_time_range}

        post_body = {
            "request_data": {
                "query": query,
                "tenants": tenants,
                "timeframe": time_frame,
            }
        }
        self.logger.info("Posting to API...")
        resp_json = self._post_to_api(start_xql_query_endpoint, post_body)
        self.logger.info("Getting reply...")
        execution_id = resp_json.get("reply", None)
        if execution_id is None:
            resp_text = resp_json.text
            raise PluginException(
                cause="API Error. API returned an empty Execution ID",
                assistance="The XQL Query could not be completed. Check input and try again.",
                data=resp_text,
            )
        return execution_id

    @Util.retry(tries=1, timeout=900, exceptions=PluginException, backoff_seconds=1)
    def get_xql_query_results(self, query_id, limit) -> Dict:
        get_xql_query_results_endpoint = "/public_api/v1/xql/get_query_results/"
        # Limit must be between 1 and 1000. Limits of over 1000 require the use of the Get XQL Query Results Stream API
        if limit > 1000 or limit < 1:
            raise PluginException(
                cause=f"A limit of {limit} is an invalid input value",
                assistance="Limit input value must be between 1 and 1000",
            )
        pending_flag = False
        format_ = "json"
        post_body = {
            "request_data": {
                "query_id": query_id,
                "limit": limit,
                "pending_flag": pending_flag,
                "format": format_,
            }
        }
        resp_json = self._post_to_api(get_xql_query_results_endpoint, post_body)
        output_object = {
            "status": resp_json.get("reply").get("status"),
            "number_of_results": resp_json.get("reply").get("number_of_results"),
            "query_cost": resp_json.get("reply").get("query_cost"),
            "remaining_quota": resp_json.get("reply").get("remaining_quota"),
            "results": resp_json.get("reply").get("results"),
        }
        return output_object

    def get_file_quarantine_status(self, file: dict) -> Dict:
        quarantine_status_endpoint = "/public_api/v1/quarantine/status/"
        post_body = {"request_data": {"files": [file]}}
        resp_json = self._post_to_api(quarantine_status_endpoint, post_body)
        file_quarantine_statuses = resp_json.get("reply", [])
        if len(file_quarantine_statuses) < 1:
            return {}

        return file_quarantine_statuses[0]

    def get_endpoint_information(self, endpoint):
        endpoint_type = self._get_endpoint_type(endpoint)
        self.logger.info(f"Endpoint field to look for: {endpoint_type}")

        api_endpoint = "/public_api/v1/endpoints/get_endpoint/"

        request_body = {
            "request_data": {
                "search_from": 0,
                "search_to": 100,
                "sort": {"field": "endpoint_id", "keyword": "ASC"},
                "filters": [{"field": endpoint_type, "operator": "in", "value": [endpoint]}],
            }
        }

        self.logger.info("Posting to API...")
        results = self._post_to_api(api_endpoint, request_body)
        self.logger.info("Getting reply...")

        output_object = {
            "endpoints": results.get("reply").get("endpoints"),
            "total_count": results.get("reply").get("total_count"),
        }

        return output_object

    def isolate_endpoint(self, endpoint, isolation_state):
        endpoint_info = self.get_endpoint_information(endpoint)
        endpoints = endpoint_info.get("endpoints")
        if not endpoints:
            self.logger.error(f"No matching endpoints found. Endpoint: {endpoint}")
            raise PluginException(
                cause="Endpoint not found.",
                assistance=f"The endpoint {endpoint} was not found. Please check your input and try again",
            )

        num_endpoints = len(endpoints)
        self.logger.info(f"Number of endpoints found: {num_endpoints}")

        if num_endpoints > 1:
            self.logger.info("Taking isolation action on multiple endpoints.")
            return self._isolate_multiple_endpoints(endpoints, isolation_state)

        self.logger.info("Taking isolation action on a single endpoint.")
        return self._isolate_endpoint(endpoints, isolation_state)

    def get_alerts(
        self, from_time: int, to_time: int, time_sort_field: str = "creation_time", filters: List = None
    ) -> List[Dict]:
        endpoint = "/public_api/v2/alerts/get_alerts_multi_events/"
        response_alerts_field = "alerts"
        return self._get_items_from_endpoint(
            endpoint, from_time, to_time, response_alerts_field, time_sort_field, filters
        )

    def get_incidents(
        self, from_time: int, to_time: int, time_sort_field: str = "creation_time", filters: List = None
    ) -> List[Dict]:
        endpoint = "/public_api/v1/incidents/get_incidents/"
        response_incidents_field = "incidents"
        return self._get_items_from_endpoint(
            endpoint, from_time, to_time, response_incidents_field, time_sort_field, filters
        )

    def allow_or_block_file(
        self, file_hash: str, comment: str, incident_id: str = None, block_file: bool = True
    ) -> bool:
        if block_file:
            endpoint = "/public_api/v1/hash_exceptions/blocklist/"
        else:
            endpoint = "/public_api/v1/hash_exceptions/allowlist/"

        post_body = {
            "request_data": {
                "hash_list": [file_hash],
                "comment": comment,
            }
        }

        if incident_id:
            post_body["request_data"]["incident_id"] = incident_id

        block_action = "Block" if block_file else "Allow"

        self.logger.info(f"Taking {block_action} action on file: {file_hash}")
        self.logger.info(f"Endpoint: {endpoint}")

        result = self._post_to_api(endpoint, post_body)

        if result.get("reply"):  # reply will be true or false
            self.logger.info(f"{block_action} action was successful")
            return True
        self.logger.warning(f"{block_action} action failed")
        self.logger.warning(f"Result: {result}")
        return False

    ###########################
    # Private Methods
    ###########################
    def _get_items_from_endpoint(
        self,
        endpoint: str,
        from_time: int,
        to_time: int,
        response_item_field: str,
        time_sort_field: str = "creation_time",
        filters: List = None,
    ) -> List[Dict]:
        batch_size = 100
        search_from = 0
        search_to = search_from + batch_size

        filters = filters or []
        # If time constraints have been provided for the request, add them to the post body
        if from_time is not None and to_time is not None:
            filters.append({"field": time_sort_field, "operator": "gte", "value": from_time})
            filters.append({"field": time_sort_field, "operator": "lte", "value": to_time})

        # Request items in ascending order so that we get the oldest items first.
        post_body = {
            "request_data": {
                "search_from": search_from,
                "search_to": search_to,
                "sort": {"field": time_sort_field, "keyword": "asc"},
                "filters": filters,
            }
        }

        done = False
        all_items = []

        while not done:
            resp_json = self._post_to_api(endpoint, post_body)
            if resp_json is not None:
                total_count = resp_json.get("reply", {}).get("total_count", -1)
                all_items.extend(resp_json.get("reply", {}).get(response_item_field, []))

                # If the number of items we have received so far is greater than or equal to the total number of
                # items which match the query, then we can stop paging.
                if len(all_items) >= total_count or total_count < 0:
                    done = True

                # Update the indices of search_from and search_to to we can request the next page
                search_from = search_from + batch_size
                new_to = search_to + batch_size
                search_to = new_to if new_to < total_count else total_count

                # Add the updated page indices to the request body for when we request the next page
                post_body["request_data"]["search_from"] = search_from
                post_body["request_data"]["search_to"] = search_to
            else:
                done = True

            # Back-off between making requests to the API.
            time.sleep(1)

        return all_items

    def _isolate_multiple_endpoints(self, endpoints, isolation_state):
        if isolation_state:
            api_endpoint = "/public_api/v1/endpoints/isolate/"
        else:
            api_endpoint = "/public_api/v1/endpoints/unisolate/"

        endpoint_ids = []
        for ep in endpoints:
            endpoint_ids.append(ep.get("endpoint_id"))

        self.logger.info(f"Isolation: {isolation_state}\nEndpoint IDs:{endpoint_ids}")
        post_body = {
            "request_data": {"filters": [{"field": "endpoint_id_list", "operator": "in", "value": endpoint_ids}]}
        }

        result = self._post_to_api(api_endpoint, post_body)
        return result.get("reply")

    def _isolate_endpoint(self, endpoints, isolation_state):
        if isolation_state:
            api_endpoint = "/public_api/v1/endpoints/isolate/"
        else:
            api_endpoint = "/public_api/v1/endpoints/unisolate/"

        endpoint_id = endpoints[0].get("endpoint_id")

        self.logger.info(f"Isolation: {isolation_state}\nEndpoint ID:{endpoint_id}")
        post_body = {"request_data": {"endpoint_id": endpoint_id}}

        result = self._post_to_api(api_endpoint, post_body)
        return result.get("reply")

    def _standard_authentication(self, api_key_id: int, api_key: str) -> dict:
        return {"x-xdr-auth-id": str(api_key_id), "Authorization": api_key}

    def _advanced_authentication(self, api_key_id: int, api_key: str) -> dict:
        """
        This was generated by Cortex XDR.

        This will create the headers we need to authenticate to the API

        :param api_key_id: ID of the API key we are going to use, shown in the API Keys page (ex. 1, 2, 3)
        :type api_key_id: int
        :param api_key: The API String. This is generated when you create a new API key
        :type api_key: string
        :return: headers object
        :rtype: dict
        """

        # Generate a 64 bytes random string
        nonce = "".join([secrets.choice(string.ascii_letters + string.digits) for _ in range(64)])
        # Get the current timestamp as milliseconds.
        timestamp = int(datetime.now(timezone.utc).timestamp()) * 1000
        # Generate the auth key:
        auth_key = f"{api_key}{nonce}{timestamp}"
        # Convert to bytes object
        auth_key = auth_key.encode("utf-8")
        # Calculate sha256:
        api_key_hash = hashlib.sha256(auth_key).hexdigest()
        # Generate HTTP call headers
        return {
            "x-xdr-timestamp": str(timestamp),
            "x-xdr-nonce": nonce,
            "x-xdr-auth-id": str(api_key_id),
            "Authorization": api_key_hash,
        }

    # Disable all the inconsistent-return-statements violations in this function. Either return or raise an
    # exception. The implicit return of this function is unreachable.
    # pylint: disable=inconsistent-return-statements
    def _post_to_api(self, endpoint, post_body):  # noqa MC0001
        url = urllib.parse.urljoin(self.fully_qualified_domain_name, endpoint)
        try:
            response = requests.post(url=url, json=post_body, headers=self.headers, timeout=self.DEFAULT_TIMEOUT)
            response_text = response.text

            if response.status_code == 400:
                raise PluginException(
                    cause=f"API Error. API returned {response.status_code}",
                    assistance="Bad request, invalid JSON.",
                    data=response_text,
                )
            if response.status_code == 401:
                raise PluginException(
                    cause=f"API Error. API returned {response.status_code}",
                    assistance="Authorization failed. Check your API Key ID & API Key.",
                    data=response_text,
                )
            if response.status_code == 402:
                raise PluginException(
                    cause=f"API Error. API returned {response.status_code}",
                    assistance="Unauthorized access. User does not have the required license type to run this API.",
                    data=response_text,
                )
            if response.status_code == 403:
                raise PluginException(
                    cause=f"API Error. API returned {response.status_code}",
                    assistance="Forbidden. The provided API Key does not have the required RBAC permissions to run this API.",
                    data=response_text,
                )
            if response.status_code == 404:
                raise PluginException(
                    cause=f"API Error. API returned {response.status_code}",
                    assistance=f"The object at {url} does not exist. Check the FQDN connection setting and try again.",
                    data=response_text,
                )
            # Success; no content
            if response.status_code == 204:
                return None
            if 200 <= response.status_code < 300:
                return response.json()

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as error:
            self.logger.info(f"Invalid json: {error}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)
        except requests.exceptions.HTTPError as error:
            self.logger.info(f"Request to {url} failed: {error}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN)

    def _get_endpoint_type(self, endpoint_info):
        # ID
        if len(endpoint_info) == 32:
            try:
                int(endpoint_info, 16)
                return self.ENDPOINT_ID_TYPE
            except Exception:  # noqa B110 - Try except pass
                pass

        # IP
        if match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", endpoint_info):
            return self.ENDPOINT_IP_TYPE

        # Don't know, try hostname
        return self.ENDPOINT_HOSTNAME_TYPE

    def get_response_alerts(self, post_body: dict) -> Tuple[list, int, int]:
        """
        Helper method to make the request in `monitor_alerts` task.

        :param post_body: Object containing the post body (filters etc) to send in the requests

        """

        headers = self._advanced_authentication(self.api_key_id, self.api_key)
        fqdn = self.get_url()
        endpoint = "public_api/v1/alerts/get_alerts"

        url = f"{fqdn}{endpoint}"
        try:
            response = self.build_request(url=url, headers=headers, post_body=post_body)
        except PluginException as error:
            if isinstance(error.data, Response):
                raise APIException(
                    cause=error.cause,
                    assistance=error.assistance,
                    data=error.data.text,
                    status_code=error.data.status_code,
                )
            raise error

        response = self._handle_401(response=response, url=url, post_body=post_body)

        response = extract_json(response)

        total_count = response.get("reply", {}).get("total_count")
        results_count = response.get("reply", {}).get("result_count")
        results = response.get("reply", {}).get("alerts", [])

        # They physically return None so we can't default 0 in .get()
        if total_count is None:
            total_count = 0

        # Also including results count just to be safe.
        if results_count is None:
            results_count = 0

        return results, results_count, total_count

    def _handle_401(self, response: Response, url: str, post_body: dict):
        """
        In the event of 401 after 15 minutes when creds expire,
        re-run the creds generation
        """

        if response.status_code in [401, 403]:
            self.logger.info(f"Received HTTP {response.status_code}, attempting to refresh token")

            new_headers = self._advanced_authentication(api_key=self.api_key, api_key_id=self.api_key_id)
            new_response = self.build_request(url=url, headers=new_headers, post_body=post_body)

            if new_response.status_code in [401, 403]:
                self.logger.info("Token is still invalid, raising exception")
                raise APIException(
                    cause=PluginException.causes.get(PluginException.Preset.API_KEY),
                    assistance=PluginException.assistances.get(PluginException.Preset.API_KEY),
                    status_code=401,
                    data=response.text,
                )

            return new_response

        else:
            return response

    def build_request(self, url: str, headers: dict, post_body: dict) -> Response:
        """
        Helper method to build the request and return response object
        """

        request = requests.Request(method="post", url=url, headers=headers, json=post_body)

        custom_config_exceptions = {
            HTTPStatusCodes.BAD_REQUEST: PluginException(
                cause=PluginException.causes.get(PluginException.Preset.BAD_REQUEST),
                assistance="Bad request, invalid JSON.",
            ),
            HTTPStatusCodes.UNAUTHORIZED: PluginException(
                cause=PluginException.causes.get(PluginException.Preset.INVALID_CREDENTIALS),
                assistance="Authorization failed. Check your API Key ID & API Key.",
            ),
            HTTPStatusCodes.PAYMENT_REQUIRED: PluginException(
                cause=PluginException.causes.get(PluginException.Preset.UNAUTHORIZED),
                assistance="Unauthorized access. User does not have the required license type to run this API.",
            ),
            HTTPStatusCodes.FORBIDDEN: PluginException(
                cause=PluginException.causes.get(PluginException.Preset.UNAUTHORIZED),
                assistance="Forbidden. The provided API Key does not have the required RBAC permissions to run this API.",
            ),
            HTTPStatusCodes.NOT_FOUND: PluginException(
                cause=PluginException.causes.get(PluginException.Preset.NOT_FOUND),
                assistance=f"The object at {url} does not exist. Check the FQDN connection setting and try again.",
            ),
        }

        response = make_request(
            _request=request,
            timeout=60,
            exception_custom_configs=custom_config_exceptions,
            exception_data_location=ResponseExceptionData.RESPONSE,
            allowed_status_codes=[HTTPStatusCodes.UNAUTHORIZED],
        )

        return response
