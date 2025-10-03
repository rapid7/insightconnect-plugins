import json
import logging
import os
import sys

import insightconnect_plugin_runtime

sys.path.append(os.path.abspath("../"))

from icon_azure_blob_storage.connection import Connection
from icon_azure_blob_storage.connection.schema import Input
from insightconnect_plugin_runtime import Action


class Util:
    @staticmethod
    def default_connector(action: Action, params=None) -> Action:
        if not params:
            params = {
                Input.ACCOUNT: "valid_account",
                Input.CLIENT_ID: "valid_client_id",
                Input.CLIENT_SECRET: {"secretKey": "valid_api_key"},
                Input.TENANT_ID: "valid_tenant_id",
            }
        action.connection = Connection()
        action.connection.meta = "{}"
        action.connection.logger = logging.getLogger("connection logger")
        action.connection.connect(params)
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename: str) -> str:
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), filename),
            "r",
            encoding="utf-8",
        ) as file_reader:
            return file_reader.read()

    @staticmethod
    def read_file_to_dict(filename: str) -> dict:
        return json.loads(Util.read_file_to_string(filename))

    @staticmethod
    def mock_request(*args, **kwargs):
        class MockResponse:
            def __init__(self, status_code: int, filename: str = None) -> None:
                self.status_code = status_code
                self.text = ""
                if filename:
                    if filename == "delete_blob_headers.json.resp":
                        self.headers = Util.read_file_to_dict(f"responses/{filename}")
                    elif "get_blob" in filename:
                        self.content = (
                            Util.read_file_to_string(f"responses/{filename}")
                            .encode()
                            .decode("unicode_escape")
                            .encode("raw_unicode_escape")
                        )
                    else:
                        self.text = Util.read_file_to_string(f"responses/{filename}")

            def json(self):
                return json.loads(self.text)

        if kwargs.get("url") == "https://valid_account.blob.core.windows.net/valid-container-name?restype=container":
            return MockResponse(201)
        if kwargs.get("url") == "https://valid_account.blob.core.windows.net/invalid_container_NAME?restype=container":
            return MockResponse(400, "create_container_invalid_characters.xml.resp")
        if kwargs.get("url") == "https://valid_account.blob.core.windows.net/existing-container-name?restype=container":
            return MockResponse(409, "create_container_container_exists.xml.resp")
        if kwargs.get("url") == "https://valid_account.blob.core.windows.net/?comp=list":
            if kwargs.get("params") == {
                "prefix": "m",
                "maxresults": 20,
                "include": ["metadata", "system", "deleted"],
                "timeout": 30,
            }:
                return MockResponse(200, "list_containers.xml.resp")
            if kwargs.get("params", {}).get("include") == []:
                return MockResponse(200, "list_containers_without_include.xml.resp")
            if kwargs.get("params", {}).get("prefix") == "":
                return MockResponse(200, "list_containers_without_prefix.xml.resp")
            if not kwargs.get("params"):
                return MockResponse(400)
            if kwargs.get("params", {}).get("include") == [
                "metadata",
                "sysxastem",
                "deleted",
            ]:
                return MockResponse(400, "list_containers_invalid_include.xml.resp")
        if kwargs.get("url") == "https://valid_account.blob.core.windows.net/delete_container_name?restype=container":
            return MockResponse(202)
        if (
            kwargs.get("url")
            == "https://valid_account.blob.core.windows.net/delete_invalid_container_NAME?restype=container"
        ):
            return MockResponse(400, "delete_container_invalid_characters.xml.resp")
        if (
            kwargs.get("url")
            == "https://valid_account.blob.core.windows.net/not_existing_container_name?restype=container"
        ):
            return MockResponse(404, "container_not_found.xml.resp")
        if (
            kwargs.get("url")
            == "https://valid_account.blob.core.windows.net/valid-container-name/?restype=container&comp=list"
        ):
            if kwargs.get("params") == {
                "prefix": "my",
                "delimiter": "plugin",
                "maxresults": 20,
                "include": ["tags", "metadata", "copy", "deleted"],
                "timeout": 30,
            }:
                return MockResponse(200, "list_blobs.xml.resp")
            if kwargs.get("params", {}).get("prefix") is None:
                return MockResponse(200, "list_blobs_without_prefix.xml.resp")
            if kwargs.get("params", {}).get("include") == []:
                return MockResponse(200, "list_blobs_without_include.xml.resp")
            if kwargs.get("params", {}).get("delimiter") is None:
                return MockResponse(200, "list_blobs_without_delimiter.xml.resp")
            if kwargs.get("params", {}).get("include") == [
                "taRANDOMgs",
                "metadata",
                "copy",
                "deleted",
            ]:
                return MockResponse(400, "list_blobs_invalid_include.xml.resp")
        if (
            kwargs.get("url")
            == "https://valid_account.blob.core.windows.net/container-not-found/?restype=container&comp=list"
        ):
            return MockResponse(404, "container_not_found.xml.resp")
        if kwargs.get("url") in [
            "https://valid_account.blob.core.windows.net/valid-container-name/page_blob",
            "https://valid_account.blob.core.windows.net/valid-container-name/block_blob",
            "https://valid_account.blob.core.windows.net/valid-container-name/append_blob",
        ]:
            return MockResponse(201)
        if (
            kwargs.get("url")
            == "https://valid_account.blob.core.windows.net/valid-container-name/access_tier_not_supported_blob"
        ):
            return MockResponse(400, "put_blob_access_tier_not_supported.xml.resp")
        if (
            kwargs.get("url")
            == "https://valid_account.blob.core.windows.net/not_found_valid-container-name/append_blob"
        ):
            return MockResponse(404, "container_not_found.xml.resp")
        if (
            kwargs.get("url")
            == "https://valid_account.blob.core.windows.net/valid-container-name/blob_with_incorrect_type"
        ):
            return MockResponse(409, "put_blob_invalid_blob_type.xml.resp")
        if kwargs.get("url", "").startswith(
            "https://valid_account.blob.core.windows.net/valid-container-name/get_blob.PNG"
        ):
            return MockResponse(200, "get_blob.bytes.resp")
        if kwargs.get("url", "").startswith(
            "https://valid_account.blob.core.windows.net/valid-container-name/snapshot_version_blob"
        ):
            return MockResponse(400, "blob_snapshot_version_used_together.xml.resp")
        if kwargs.get("url", "").startswith("https://valid_account.blob.core.windows.net/not-found-container"):
            return MockResponse(404, "container_not_found.xml.resp")
        if kwargs.get("url", "").startswith(
            "https://valid_account.blob.core.windows.net/valid-container-name/not_found_blob.PNG"
        ):
            return MockResponse(404, "blob_not_found.xml.resp")
        if kwargs.get("url", "").startswith(
            "https://valid_account.blob.core.windows.net/valid-container-name/no_snapshots_delete_blob"
        ):
            return MockResponse(409, "delete_blob_no_snapshots.xml.resp")
        if kwargs.get("url", "").startswith(
            "https://valid_account.blob.core.windows.net/valid-container-name/delete_blob"
        ):
            return MockResponse(202, "delete_blob_headers.json.resp")

        if isinstance(kwargs.get("data"), dict):
            if kwargs.get("data", {}).get(Input.CLIENT_SECRET) == "valid_api_key":
                return MockResponse(200, "connection.json.resp")
            if kwargs.get("data", {}).get(Input.CLIENT_SECRET) == "invalid_api_key":
                return MockResponse(400)
        raise NotImplementedError("Not implemented", kwargs)
