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

    def run(self, params={}):
        result = {}

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

        if params.get(Input.USER_VOLUME_ENCRYPTION_ENABLED) and params.get(Input.ROOT_VOLUME_ENCRYPTION_ENABLED):
            raise PluginException(
                cause="Both user and root volume encrypted flags are set.",
                assistance="Only one of the encryption flags can be set.",
            )

        if params.get(Input.USER_VOLUME_ENCRYPTION_ENABLED):
            payload["UserVolumeEncryptionEnabled"] = params.get(Input.USER_VOLUME_ENCRYPTION_ENABLED)
        if params.get(Input.ROOT_VOLUME_ENCRYPTION_ENABLED):
            payload["RootVolumeEncryptionEnabled"] = params.get(Input.ROOT_VOLUME_ENCRYPTION_ENABLED)
        if params.get(Input.USER_VOLUME_ENCRYPTION_ENABLED) or params.get(Input.ROOT_VOLUME_ENCRYPTION_ENABLED):
            if params.get(Input.VOLUME_ENCRYPTION_KEY):
                payload["VolumeEncryptionKey"] = params.get(Input.VOLUME_ENCRYPTION_KEY)
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
