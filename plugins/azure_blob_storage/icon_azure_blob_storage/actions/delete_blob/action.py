import insightconnect_plugin_runtime
from .schema import DeleteBlobInput, DeleteBlobOutput, Input, Output, Component


# Custom imports below


class DeleteBlob(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_blob", description=Component.DESCRIPTION, input=DeleteBlobInput(), output=DeleteBlobOutput()
        )

    def run(self, params: dict = None):
        delete_type_permanent = self.connection.api_client.delete_blob(
            container_name=params.get(Input.CONTAINER_NAME),
            blob_name=params.get(Input.BLOB_NAME),
            snapshot_id=params.get(Input.SNAPSHOT_ID, None),
            version_id=params.get(Input.VERSION_ID, None),
            delete_snapshots=params.get(Input.SNAPSHOTS, {}),
            additional_headers=params.get(Input.ADDITIONAL_HEADERS, {}),
        )
        delete_type = "soft" if delete_type_permanent == "false" else "permanent"
        return {
            Output.SUCCESS: True,
            Output.MESSAGE: "Blob deletion was successfully submitted.",
            Output.DELETE_TYPE: delete_type,
        }
