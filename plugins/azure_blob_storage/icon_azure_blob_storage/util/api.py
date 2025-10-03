import base64
import datetime
import json
import xmltodict
from logging import Logger
import requests
import time

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_azure_blob_storage.util.helpers import xml_to_json
from icon_azure_blob_storage.util.endpoints import (
    COMMON_URI,
    O365_AUTH_ENDPOINT,
    O365_AUTH_RESOURCE,
    LIST_CONTAINERS_ENDPOINT,
    CONTAINER_ENDPOINT,
    BLOB_ENDPOINT,
    LIST_BLOBS_ENDPOINT,
)
from typing import Union
from icon_azure_blob_storage.util.constants import BlobType, HeaderParam, UrlParam


class AzureBlobStorageAPI:
    def __init__(self, client_id: str, client_secret: str, tenant_id: str, account_name: str, logger: Logger) -> None:
        self._tenant_id = tenant_id
        self._client_id = client_id
        self._client_secret = client_secret
        self._account_name = account_name
        self._uri = COMMON_URI.format(account=account_name)
        self._logger = logger
        self._token_expires_on = 0
        self.auth_token = None

    @property
    def auth_token(self) -> str:
        if self._token_expires_on and self._token_expires_on - time.time() > 10:
            return self._auth_token

        request_data = {
            "grant_type": "client_credentials",
            "client_id": self._client_id,
            "resource": O365_AUTH_RESOURCE,
            "client_secret": self._client_secret,
        }

        formatted_endpoint = O365_AUTH_ENDPOINT.format(self._tenant_id)
        self._logger.info(f"Getting token from: {formatted_endpoint}")
        response = requests.request("POST", formatted_endpoint, data=request_data)
        self._logger.info(f"Authentication request status: {str(response.status_code)}")

        if response.status_code != 200:
            self._logger.error(response.text)
            raise PluginException(
                cause="Unable to authorize against Azure Storage API.",
                assistance="The application may not be authorized to connect to the Azure Storage API. "
                "Please contact your Azure administrator.",
                data=response.text,
            )
        response_json = response.json()
        self.auth_token = response_json.get("access_token")
        self._token_expires_on = int(response_json.get("expires_on"))
        self._logger.info(f"Authentication Token: ****************{self._auth_token[-5:]}")

        return self._auth_token

    @auth_token.setter
    def auth_token(self, auth_token) -> None:
        self._auth_token = auth_token

    def _get_headers(self, additional_headers: dict = None) -> dict:
        base_headers = {
            "x-ms-version": "2021-04-10",
            "x-ms-date": datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT"),
            "Authorization": f"Bearer {self.auth_token}",
        }
        if additional_headers:
            return {**base_headers, **additional_headers}
        return base_headers

    def create_container(self, container_name: str, additional_headers: dict = None) -> bool:
        self._logger.info(f"Creating a container named {container_name} for {self._account_name} account...")
        self.make_request(
            method="PUT",
            endpoint=CONTAINER_ENDPOINT.format(container_name=container_name),
            headers=self._get_headers(additional_headers),
        )
        return True

    def list_containers(
        self,
        prefix: str = "",
        max_results: int = None,
        include: [] = None,
        timeout: int = None,
        additional_headers: dict = None,
    ) -> object:
        self._logger.info(f"Listing containers belonging to {self._account_name}...")
        json_response = self.make_json_request(
            method="GET",
            endpoint=LIST_CONTAINERS_ENDPOINT,
            headers=self._get_headers(additional_headers),
            params={
                UrlParam.PREFIX: prefix,
                UrlParam.MAX_RESULTS: max_results,
                UrlParam.INCLUDE: include,
                UrlParam.TIMEOUT: timeout,
            },
        )
        return json_response.get("EnumerationResults", {})

    def delete_container(self, container_name: str, additional_headers: dict = None) -> bool:
        self._logger.info(f"Deleting a container named {container_name} for {self._account_name} account...")
        self.make_request(
            method="DELETE",
            endpoint=CONTAINER_ENDPOINT.format(container_name=container_name),
            headers=self._get_headers(additional_headers),
        )
        return True

    def list_blobs(
        self,
        container_name: str,
        prefix: str = None,
        delimiter: str = None,
        max_results: int = None,
        include: [] = None,
        timeout: int = None,
        additional_headers: dict = None,
    ) -> object:
        self._logger.info(f"Listing blobs in {container_name} container belonging to {self._account_name}...")
        json_response = self.make_json_request(
            method="GET",
            endpoint=LIST_BLOBS_ENDPOINT.format(container_name=container_name),
            headers=self._get_headers(additional_headers),
            params={
                UrlParam.PREFIX: prefix,
                UrlParam.DELIMITER: delimiter,
                UrlParam.MAX_RESULTS: max_results,
                UrlParam.INCLUDE: include,
                UrlParam.TIMEOUT: timeout,
            },
        )
        return json_response.get("EnumerationResults", {})

    def put_blob(
        self,
        container_name: str,
        blob_name: str,
        blob_type: str,
        timeout: int = None,
        block_blob_content: str = None,
        access_tier: str = None,
        additional_headers: dict = None,
        page_blob_content_length: str = None,
    ) -> bool:

        self._logger.info(
            f"Creating a blob named {blob_name} in {container_name} container for {self._account_name} account..."
        )
        block_blob_content, page_blob_content_length = self._parse_put_blob_params(
            blob_type=blob_type,
            block_blob_content=block_blob_content,
            page_blob_content_length=page_blob_content_length,
        )
        headers = self._get_put_blob_headers(
            blob_type=blob_type,
            additional_headers=additional_headers,
            block_blob_content=block_blob_content,
            page_blob_content_length=page_blob_content_length,
            access_tier=access_tier,
        )
        self.make_request(
            method="PUT",
            endpoint=BLOB_ENDPOINT.format(container_name=container_name, blob_name=blob_name),
            headers=headers,
            params={UrlParam.TIMEOUT: timeout},
            data=block_blob_content.encode().decode("unicode_escape").encode("raw_unicode_escape"),
        )
        return True

    def get_blob(
        self,
        container_name: str,
        blob_name: str,
        snapshot_id: str = None,
        version_id: str = None,
        byte_to_string: str = False,
        additional_headers: dict = None,
    ) -> Union[bytes, str]:

        self._logger.info(
            f"Getting a blob named {blob_name} in {container_name} container for {self._account_name} account..."
        )
        response = self.make_request(
            method="GET",
            endpoint=BLOB_ENDPOINT.format(container_name=container_name, blob_name=blob_name),
            headers=self._get_headers(additional_headers),
            params={
                UrlParam.SNAPSHOT_ID: snapshot_id,
                UrlParam.VERSION_ID: version_id,
            },
        )
        if byte_to_string:
            return response.text

        return str(base64.b64encode(response.content), "utf-8")

    def delete_blob(
        self,
        container_name: str,
        blob_name: str,
        snapshot_id: str = None,
        version_id: str = None,
        delete_snapshots: str = None,
        additional_headers: dict = None,
    ) -> str:

        if delete_snapshots:
            additional_headers[HeaderParam.DELETE_SNAPSHOTS] = delete_snapshots
        self._logger.info(
            f"Deleting a blob named {blob_name} in {container_name} container for {self._account_name} account..."
        )
        response = self.make_request(
            method="DELETE",
            endpoint=BLOB_ENDPOINT.format(container_name=container_name, blob_name=blob_name),
            headers=self._get_headers(additional_headers),
            params={UrlParam.SNAPSHOT_ID: snapshot_id, UrlParam.VERSION_ID: version_id},
        )

        return response.headers.get(HeaderParam.DELETE_TYPE_PERMANENT)

    def make_request(  # noqa: MC0001
        self, method: str, endpoint: str, headers: dict, params: dict = None, data: bytes = ""
    ) -> requests.Response:
        try:
            response = requests.request(
                method=method, url=self._uri + endpoint, headers=headers, params=params, data=data
            )

            if response.status_code == 400:
                raise PluginException(
                    cause="Invalid input parameters.",
                    assistance="Please verify inputs and if the issue persists, contact support.",
                    data=xml_to_json(response.text),
                )
            if response.status_code == 401:
                raise PluginException(preset=PluginException.Preset.API_KEY, data=xml_to_json(response.text))
            if response.status_code == 403:
                raise PluginException(
                    cause="Operation is not allowed.",
                    assistance="Please verify inputs and if the issue persists, contact support.",
                    data=xml_to_json(response.text),
                )
            if response.status_code == 404:
                raise PluginException(
                    cause="Resource not found.",
                    assistance="Please verify inputs and if the issue persists, contact support.",
                    data=xml_to_json(response.text),
                )
            if response.status_code == 409:
                raise PluginException(
                    cause="Request made conflicts with an existing resource.",
                    assistance="Please verify inputs and if the issue persists, contact support.",
                    data=xml_to_json(response.text),
                )
            if 400 <= response.status_code < 500:
                raise PluginException(
                    preset=PluginException.Preset.UNKNOWN,
                    data=xml_to_json(response.text),
                )
            if response.status_code >= 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=xml_to_json(response.text))

            if 200 <= response.status_code < 300:
                return response

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except requests.exceptions.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)

    def make_json_request(self, method: str, endpoint: str, headers: dict = None, params: dict = None) -> dict:
        try:
            response = self.make_request(method=method, endpoint=endpoint, params=params, headers=headers)
            return xmltodict.parse(response.text)
        except json.decoder.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=e)

    def _parse_put_blob_params(self, blob_type: str, block_blob_content: str, page_blob_content_length: str):
        if blob_type == BlobType.PAGE_BLOB and not page_blob_content_length:
            raise PluginException(
                cause=f"Blob Content Length parameter is required for {BlobType.PAGE_BLOB}",
                assistance="Please provide this parameter or change Blob Type.",
            )
        if blob_type != BlobType.PAGE_BLOB and page_blob_content_length:
            self._logger.warning(
                f"Blob Content Length param can be used only with {BlobType.PAGE_BLOB}. This parameter will be ignored."
            )
            page_blob_content_length = 0
        if blob_type != BlobType.BLOCK_BLOB and block_blob_content:
            self._logger.warning(
                f"Blob Content param can be used only with {BlobType.BLOCK_BLOB}. Initializing empty {blob_type}."
            )
            block_blob_content = ""
        return block_blob_content, page_blob_content_length

    def _get_put_blob_headers(
        self,
        blob_type: str,
        additional_headers: dict = None,
        block_blob_content: str = "",
        page_blob_content_length: str = None,
        access_tier: str = "",
    ) -> dict:
        additional_headers[HeaderParam.BlobType] = blob_type
        if access_tier:
            additional_headers[HeaderParam.ACCESS_TIER] = access_tier
        if page_blob_content_length:
            additional_headers[HeaderParam.BLOB_CONTENT_LENGTH] = str(page_blob_content_length)
        if block_blob_content:
            additional_headers[HeaderParam.CONTENT_LENGTH] = str(len(block_blob_content))
        return self._get_headers(additional_headers)
