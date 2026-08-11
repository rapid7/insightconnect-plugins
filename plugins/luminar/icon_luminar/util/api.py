from json import JSONDecodeError
from logging import Logger
from typing import Any, Dict, List

import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from requests import Response

from icon_luminar.util.constants import HEADERS, RETRY_STATUS_CODES, TIMEOUT
from icon_luminar.util.utils import build_base_url


class LuminarManager:
    """
    Class to manage Luminar API interactions.
    """

    def __init__(
        self,
        cognyte_client_id: str,
        cognyte_client_secret: str,
        cognyte_account_id: str,
        cognyte_base_url: str,
        logger: Logger,
    ) -> None:
        self.base_url = build_base_url(cognyte_base_url)
        self.account_id = cognyte_account_id
        self.client_id = cognyte_client_id
        self.client_secret = cognyte_client_secret
        self.payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials",
            "scope": "externalAPI/stix.readonly",
        }
        self.req_headers = HEADERS
        self.logger = logger

    def _response_handler(self, response: Response, url: str) -> None:
        """
        Raise the correct PluginException based on the response status code.
        """
        status = response.status_code

        if status == 200:
            return
        if status == 401:
            raise PluginException(preset=PluginException.Preset.API_KEY)
        if status == 403:
            raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
        if status == 404:
            raise PluginException(
                cause="No results found.",
                assistance="Please provide valid inputs or verify the plugin configuration.",
                data=f"{response.text}\nURL: {url}",
            )
        if 400 <= status < 500:
            raise PluginException(
                preset=PluginException.Preset.UNKNOWN, data=response.text
            )
        if status >= 500:
            raise PluginException(
                preset=PluginException.Preset.SERVER_ERROR, data=response.text
            )
        # Catch unexpected edge cases
        raise PluginException(
            cause="Unexpected response received.",
            assistance="Please contact support.",
            data=f"Status code: {status}\nBody: {response.text}\nURL: {url}",
        )

    def access_token(self) -> str:
        """
        Make a request to the Luminar API.

        :return: Tuple[Union[bool, str], str]
            The access token (if successful) or False (if unsuccessful),
            and a message indicating the status of the
            request.
        """
        req_url = f"{self.base_url}/externalApi/v2/realm/{self.account_id}/token"
        response = requests.post(
            req_url, headers=self.req_headers, data=self.payload, timeout=TIMEOUT
        )
        self._response_handler(response, req_url)
        try:
            return response.json().get("access_token")
        except JSONDecodeError:
            raise PluginException(
                preset=PluginException.Preset.INVALID_JSON, data=response.text
            )

    def get_taxi_collections(self) -> Dict[str, str]:
        """
        Fetch TAXII collections from Luminar API and map aliases to IDs.

        Returns:
            Dict[str, str]: Mapping of collection alias → ID.
        """
        access_token = self.access_token()
        headers = {"Authorization": f"Bearer {access_token}"}
        req_url = f"{self.base_url}/externalApi/taxii/collections/"
        resp = requests.get(req_url, headers=headers, timeout=TIMEOUT)
        self._response_handler(resp, req_url)

        try:
            collections_data = resp.json().get("collections", [])
        except JSONDecodeError:
            raise PluginException(
                preset=PluginException.Preset.INVALID_JSON, data=resp.text
            )

        return {
            c.get("alias"): c.get("id")
            for c in collections_data
            if c.get("alias") and c.get("id")
        }

    def get_collection_objects(
        self, collection: str, params: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """
        Fetch objects from a TAXII collection, handling pagination and retries.

        Args:
            collection (str): The TAXII collection ID.
            params (Dict[str, Any]): Query params.

        Returns:
            List[Dict[str, Any]]: Objects retrieved from the collection.
        """
        collection_objects: List[Dict[str, Any]] = []
        access_token = self.access_token()
        headers = {"Authorization": f"Bearer {access_token}"}
        retries, max_retries = 0, 3

        while retries < max_retries:
            req_url = (
                f"{self.base_url}/externalApi/taxii/collections/{collection}/objects/"
            )
            resp = requests.get(
                req_url, params=params, headers=headers, timeout=TIMEOUT
            )

            if resp.status_code == 401:  # Token expired, refresh and retry
                self.logger.warning(
                    "Access token has expired, status_code=%s and response=%s,"
                    " Regenerating token...",
                    resp.status_code,
                    resp.text,
                )
                access_token = self.access_token()
                headers["Authorization"] = f"Bearer {access_token}"
                continue

            if resp.status_code == 200:
                try:
                    response_json = resp.json()
                except JSONDecodeError:
                    raise PluginException(
                        preset=PluginException.Preset.INVALID_JSON, data=resp.text
                    )

                objects = response_json.get("objects", [])
                collection_objects.extend(objects)
                self.logger.info(
                    "Fetched %d objects so far from collection %s",
                    len(collection_objects),
                    collection,
                )

                if "next" in response_json:
                    params["next"] = response_json["next"]
                else:
                    break

            elif resp.status_code in RETRY_STATUS_CODES:
                retries += 1
                self.logger.warning(
                    "Request failed with status %s. Retrying %d/%d...",
                    resp.status_code,
                    retries,
                    max_retries,
                )
                continue

            else:
                self._response_handler(resp, req_url)

        self.logger.info(
            "Completed fetching %d objects from collection %s",
            len(collection_objects),
            collection,
        )
        return collection_objects
