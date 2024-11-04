import insightconnect_plugin_runtime
from .schema import CreateWorkspaceInput, CreateWorkspaceOutput, Component, Input, Output

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class CreateWorkspace(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_workspace",
            description=Component.DESCRIPTION,
            input=CreateWorkspaceInput(),
            output=CreateWorkspaceOutput(),
        )

    def build_payload(self, params: dict) -> dict:

        payload = {
            "DirectoryId": params.get(Input.DIRECTORY_ID),
            "UserName": params.get(Input.USERNAME),
            "BundleId": params.get(Input.BUNDLE_ID),
            "Tags": params.get(Input.TAGS),
            "WorkspaceProperties": {
                "ComputeTypeName": params.get(Input.WORKSPACE_PROPERTIES)["compute_type_name"],
                "RootVolumeSizeGib": params.get(Input.WORKSPACE_PROPERTIES)["root_volume_size"],
                "RunningMode": params.get(Input.WORKSPACE_PROPERTIES)["running_mode"],
                "RunningModeAutoStopTimeoutInMinutes": params.get(Input.WORKSPACE_PROPERTIES)[
                    "running_mode_auto_stop_time_out"
                ],
                "UserVolumeSizeGib": params.get(Input.WORKSPACE_PROPERTIES)["user_volume_size"],
            },
        }
        return payload

    def run(self, params={}):
        result = {}
        payload = self.build_payload(params)
        user_volume_encryption_enabled = params.get(Input.USER_VOLUME_ENCRYPTION_ENABLED)
        root_volume_encryption_enabled = params.get(Input.ROOT_VOLUME_ENCRYPTION_ENABLED)
        volume_encryption_key = params.get(Input.VOLUME_ENCRYPTION_KEY)

        if user_volume_encryption_enabled and root_volume_encryption_enabled:
            raise PluginException(
                cause="Both user and root volume encrypted flags are set.",
                assistance="Only one of the encryption flags can be set.",
            )

        if user_volume_encryption_enabled:
            payload["UserVolumeEncryptionEnabled"] = user_volume_encryption_enabled
        if root_volume_encryption_enabled:
            payload["RootVolumeEncryptionEnabled"] = root_volume_encryption_enabled
        if user_volume_encryption_enabled or root_volume_encryption_enabled:
            if volume_encryption_key:
                payload["VolumeEncryptionKey"] = volume_encryption_key
            else:
                raise PluginException(
                    cause="Invalid value for Volume Encryption Key input.",
                    assistance="Please provide a valid value for the input.",
                )

        try:
            result = self.connection.aws.client("workspaces").create_workspaces(Workspaces=[payload])
        except:
            raise PluginException(cause="An unknown error occurred", data=result)

        try:
            if result["FailedRequests"]:
                raise PluginException(
                    cause=result["FailedRequests"][0].get("ErrorCode"),
                    assistance=result["FailedRequests"][0].get("ErrorMessage"),
                    data=result,
                )
        except KeyError:
            raise PluginException(
                cause="The output did not contain expected keys.",
                assistance="Contact support for help.",
                data=result,
            )

        try:
            if result["PendingRequests"][0].get("ErrorCode"):
                raise PluginException(
                    cause=result["PendingRequests"][0].get("ErrorCode"),
                    assistance=result["PendingRequests"][0].get("ErrorMessage"),
                    data=result,
                )
            else:
                result = {
                    "id": result["PendingRequests"][0].get("WorkspaceId"),
                    "state": result["PendingRequests"][0].get("State"),
                }
        except (IndexError, KeyError):
            raise PluginException(
                cause="The output did not contain expected keys.",
                assistance="Contact support for help.",
                data=result,
            )

        return {Output.WORKSPACE_ID_STATE: result}
