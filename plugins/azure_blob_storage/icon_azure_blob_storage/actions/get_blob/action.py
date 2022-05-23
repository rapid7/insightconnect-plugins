import insightconnect_plugin_runtime
from .schema import GetBlobInput, GetBlobOutput, Input, Output, Component


# Custom imports below


class GetBlob(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_blob", description=Component.DESCRIPTION, input=GetBlobInput(), output=GetBlobOutput()
        )

    def run(self, params: dict = None):
        return {
            Output.DATA: self.connection.api_client.get_blob(
                container_name=params.get(Input.CONTAINER_NAME),
                blob_name=params.get(Input.BLOB_NAME),
                snapshot_id=params.get(Input.SNAPSHOT_ID, None),
                version_id=params.get(Input.VERSION_ID, None),
                byte_to_string=params.get(Input.BYTE_TO_STRING, False),
                additional_headers=params.get(Input.ADDITIONAL_HEADERS, {}),
            )
        }
