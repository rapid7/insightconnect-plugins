from komand.exceptions import PluginException
import requests

import aiohttp
import asyncio
import json
from typing import Optional

from komand_rapid7_insightidr.connection import Connection


def _get_async_session(headers) -> aiohttp.ClientSession:
    """
    Create and return a new aiohttp ClientSession
    :return: aiohttp ClientSession
    """

    return aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False), headers=headers)


async def get_label_for_id(label_id: str, url: str, session: aiohttp.ClientSession) -> dict:
    response = await session.get(f"{url}log_search/management/labels/{label_id}")
    if response.status == 200:
        try:
            resp_json = await response.json()
            return {"id": label_id, "name": resp_json.get("label", {}).get("name")}
        except json.JSONDecodeError:
            return {}

    return {}


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

    def resource_request(self, endpoint: str, method: str = "get", params: dict = None, payload: dict = None) -> dict:
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
                response = request_method(url=endpoint, params=params, json=payload, verify=False)
        except requests.RequestException as e:
            self.logger.error(e)
            raise

        if response.status_code in range(200, 299):
            resource = response.text
            return {"resource": resource, "status": response.status_code}
        else:
            try:
                error = response.json()["message"]
            except KeyError:
                self.logger.error(f"Code: {response.status_code}, message: {error}")
                error = "Unknown error occurred. Please contact support or try again later."

            status_code_message = self._ERRORS.get(response.status_code, self._ERRORS[000])
            self.logger.error(f"{status_code_message} ({response.status_code}): {error}")
            raise PluginException(f"InsightIDR returned a status code of {response.status_code}: {status_code_message}")

    @staticmethod
    async def _get_log_entries_with_labels(connection: Connection, log_entries: [dict]) -> [dict]:
        label_ids = set()
        for log_entry in log_entries:
            for label in log_entry.get("labels", []):
                label_ids.add(label.get("id"))

        async with _get_async_session(connection.session.headers) as async_session:
            tasks: [asyncio.Future] = []
            for label_id in label_ids:
                tasks.append(
                    asyncio.ensure_future(
                        get_label_for_id(label_id=label_id, url=connection.url, session=async_session)
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
            new_log_entry["message"] = json.loads(log_entry.get("message", "{}"))
            entry_labels = []
            for label in log_entry.get("labels", []):
                label_id = label.get("id")
                if label_id and labels_by_id.get(label_id):
                    entry_labels.append(labels_by_id[label_id])
            new_log_entry["labels"] = entry_labels
            new_log_entries.append(new_log_entry)

        return new_log_entries

    @staticmethod
    def get_log_entries_with_new_labels(connection: Connection, log_entries: [dict]) -> [dict]:
        return asyncio.run(ResourceHelper._get_log_entries_with_labels(connection=connection, log_entries=log_entries))
