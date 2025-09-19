from typing import Any, Dict, List, Tuple, Union
from logging import Logger
from json import JSONDecodeError

import requests
from requests import Response
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean

TIMEOUT = 60.0
LUMINAR_BASE_URL = "https://demo.cyberluminar.com/"
HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
    "accept": "application/json",
}
class LuminarManager:
    """
    Class to manage Luminar API interactions.
    """

    def __init__(
        self,
        cognyte_client_id: str,
        cognyte_client_secret: str,
        cognyte_account_id: str,
        logger: Logger,
        cognyte_base_url: str = LUMINAR_BASE_URL
    ) -> None:
        self.base_url = cognyte_base_url
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
        Raise the correct PluginException based upon the response status code
        :param response: The response object to be reviewed
        :param url: The endpoint URL to be logged out in result of an error
        :return: None
        """
        if response.status_code == 401:
            raise PluginException(preset=PluginException.Preset.API_KEY)
        if response.status_code == 403:
            raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
        if response.status_code == 404:
            raise PluginException(
                cause="No results found.\n",
                assistance="Please provide valid inputs or verify the inputs configured in your plugin.\n",
                data=f"{response.text}\nurl: {url}",
            )
        if 400 <= response.status_code < 500:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        if response.status_code >= 500:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)
    
  
    def access_token(self) -> Tuple[Union[bool, str], str]:
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
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)


    def get_taxi_collections(self) -> Dict[str, str]:
        """
        Fetches TAXII collections from the Cognyte Luminar API and maps collection
         aliases to their IDs.

        Returns:
            Dict[str, str]: A dictionary mapping collection aliases to their IDs.
        """
        taxii_collection_ids = {}
        # try:
        access_token = self.access_token()
        headers = {"Authorization": f"Bearer {access_token}"}
        req_url = f"{self.base_url}/externalApi/taxii/collections/"
        resp = requests.get(req_url, headers=headers, timeout=TIMEOUT)
        self._response_handler(resp, req_url)
        try:
            collections_data = resp.json().get("collections", [])
        except JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=resp.text)
        
        
        # resp.raise_for_status()
        collections_data = resp.json().get("collections", [])

        # self.logger.info("Cognyte Luminar collections: %s", collections_data)

        # Store collection alias and id mapping
        for collection in collections_data:
            taxii_collection_ids[collection.get("alias")] = collection.get("id")
        # except Exception as e:
        #     self.logger.error("Error fetching collections: %s", e)

        return taxii_collection_ids

    def get_collection_objects(
        self, collection: str, params: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """
        Fetches objects from a TAXII collection, handling pagination and token expiration.

        Args:
            # headers (Dict[str, str]): HTTP headers, including authentication tokens.
            collection (str): The TAXII collection ID.
            params (Dict[str, Any]): Query parameters for filtering results.

        Returns:
            List[Dict[str, Any]]: A list of objects retrieved from the collection.
        """

        parameters = params.copy()
        collection_objects = []
        access_token = self.access_token()
        headers = {"Authorization": f"Bearer {access_token}"}

        while True:
            # Send a request to fetch objects from the collection
            resp = requests.get(
                f"{self.base_url}/externalApi/taxii/collections/{collection}/objects/",
                params=parameters,
                headers=headers,
                timeout=TIMEOUT,
            )
            if resp.status_code == 401:
                self.logger.info(
                    "Access token has expired, status_code=%s and response=%s,"
                    " Regenerating token...",
                    resp.status_code,
                    resp.text,
                )

                access_token = self.access_token()
                headers = {"Authorization": f"Bearer {access_token}"}
                continue
                
            self._response_handler(resp, f"{self.base_url}/externalApi/taxii/collections/{collection}/objects/")
            try:
                response_json = resp.json()
            except JSONDecodeError:
                raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=resp.text)
            
            all_objects = response_json.get("objects", [])
            collection_objects.extend(all_objects)
            self.logger.info(
                "Fetched objects from collection: %s", len(collection_objects)
            )

            # Check if there is a "next" page of objects and update the params
            if "next" in response_json:
                parameters["next"] = response_json["next"]
            else:
                break
       
        self.logger.info("Fetched all objects from collection: %s", collection)

        return collection_objects