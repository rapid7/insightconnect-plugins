import insightconnect_plugin_runtime

from icon_azure_blob_storage.util.constants import DEFAULT_TIMEOUT, BlobType
from .schema import PutBlobInput, PutBlobOutput, Input, Output, Component


# Custom imports below


class PutBlob(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="put_blob", description=Component.DESCRIPTION, input=PutBlobInput(), output=PutBlobOutput()
        )

    def run(self, params: dict = None):
        timeout = params.get(Input.TIMEOUT)
        if timeout and timeout < 1:
            self.logger.info(f"Provided timeout = {timeout} is incorrect. Setting timeout = {DEFAULT_TIMEOUT}s")
            timeout = DEFAULT_TIMEOUT

        self.connection.api_client.put_blob(
            container_name=params.get(Input.CONTAINER_NAME),
            blob_name=params.get(Input.BLOB_NAME),
            blob_type=params.get(Input.BLOB_TYPE),
            timeout=timeout,
            access_tier=params.get(Input.ACCESS_TIER),
            block_blob_content=params.get(Input.BLOB_CONTENT, ""),
            additional_headers=params.get(Input.ADDITIONAL_HEADERS, {}),
            page_blob_content_length=params.get(Input.BLOB_CONTENT_LENGTH),
        )
        return {Output.SUCCESS: True, Output.MESSAGE: "Blob was successfully created."}
