import insightconnect_plugin_runtime
from .schema import ListBlobsInput, ListBlobsOutput, Input, Output, Component

# Custom imports below

from icon_azure_blob_storage.util.constants import DEFAULT_MAX_RESULTS, DEFAULT_TIMEOUT, Blob, BlobProperties
from insightconnect_plugin_runtime.helper import clean
from icon_azure_blob_storage.util.helpers import dict_to_list


class ListBlobs(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_blobs", description=Component.DESCRIPTION, input=ListBlobsInput(), output=ListBlobsOutput()
        )

    def run(self, params: dict = None):
        prefix = params.get(Input.PREFIX)
        max_results = params.get(Input.MAX_RESULTS)
        timeout = params.get(Input.TIMEOUT)
        include = params.get(Input.INCLUDE, [])

        if max_results and (max_results < 1 or max_results > DEFAULT_MAX_RESULTS):
            self.logger.info(
                f"Provided max_results = {max_results} is incorrect. Setting max_results = {DEFAULT_MAX_RESULTS}"
            )
            max_results = DEFAULT_MAX_RESULTS
        if timeout and (timeout < 1 or timeout > DEFAULT_TIMEOUT):
            self.logger.info(f"Provided timeout = {timeout} is incorrect. Setting timeout = {DEFAULT_TIMEOUT}s")
            timeout = DEFAULT_TIMEOUT

        json_response = self.connection.api_client.list_blobs(
            container_name=params.get(Input.CONTAINER_NAME),
            prefix=prefix,
            delimiter=params.get(Input.DELIMITER),
            max_results=max_results,
            include=include,
            timeout=timeout,
            additional_headers=params.get(Input.ADDITIONAL_HEADERS, {}),
        )
        return self.clean_blobs_list_output(clean(json_response))

    @staticmethod
    def clean_blobs_list_output(json_response: dict) -> dict:
        new_json_response = {
            Output.PREFIX: json_response.get("Prefix", ""),
            Output.DELIMITER: json_response.get("Delimiter", ""),
            Output.MAX_RESULTS: json_response.get("MaxResults", ""),
            Output.BLOBS: dict_to_list(json_response.get("Blobs", {}).get("Blob", [])),
            Output.BLOBS_WITH_DELIMITER_MATCH: [
                item.get("Name", "") for item in dict_to_list(json_response.get("Blobs", {}).get("BlobPrefix", []))
            ],
        }
        for index, blob in enumerate(new_json_response.get(Output.BLOBS, [])):
            new_blob = {
                Blob.NAME: blob.get("Name", ""),
                Blob.VERSION_ID: blob.get("VersionId", ""),
                Blob.SNAPSHOT_ID: blob.get("Snapshot", ""),
                Blob.IS_CURRENT_VERSION: blob.get("IsCurrentVersion", ""),
                Blob.DELETED: blob.get("Deleted", ""),
                Blob.PROPERTIES: blob.get("Properties", {}),
                Blob.METADATA: blob.get("Metadata", {}),
                Blob.TAGS: dict_to_list(blob.get("Tags", {}).get("TagSet", {}).get("Tag", [])),
            }

            new_properties = {
                BlobProperties.CREATION_TIME: new_blob.get(Blob.PROPERTIES, {}).get("Creation-Time", ""),
                BlobProperties.REMAINING_RETENTION_DAYS: new_blob.get(Blob.PROPERTIES, {}).get(
                    "RemainingRetentionDays", ""
                ),
                BlobProperties.TAG_COUNT: new_blob.get(Blob.PROPERTIES, {}).get("TagCount", ""),
                BlobProperties.SERVER_ENCRYPTED: new_blob.get(Blob.PROPERTIES, {}).get("ServerEncrypted", ""),
                BlobProperties.LAST_MODIFIED: new_blob.get(Blob.PROPERTIES, {}).get("Last-Modified", ""),
                BlobProperties.CONTENT_TYPE: new_blob.get(Blob.PROPERTIES, {}).get("Content-Type", ""),
                BlobProperties.BLOB_TYPE: new_blob.get(Blob.PROPERTIES, {}).get("BlobType", ""),
                BlobProperties.ACCESS_TIER: new_blob.get(Blob.PROPERTIES, {}).get("AccessTier", ""),
                BlobProperties.ETAG: new_blob.get(Blob.PROPERTIES, {}).get("Etag", ""),
            }

            new_blob[Blob.PROPERTIES] = new_properties
            new_json_response[Output.BLOBS][index] = new_blob
        return clean(new_json_response)
