import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from smbprotocol.exceptions import SMBException
from .schema import CreateFileInput, CreateFileOutput, Input, Output, Component

import base64
import binascii
from smbprotocol.open import Open, CreateDisposition, ShareAccess, ImpersonationLevel
from smbprotocol.file_info import FileAttributes


class CreateFile(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_file",
            description=Component.DESCRIPTION,
            input=CreateFileInput(),
            output=CreateFileOutput(),
        )

    def run(self, params={}):  # noqa: MC0001
        connection = self.connection
        if not connection:
            raise PluginException(
                cause="No active connection",
                assistance="Ensure that a valid connection has been established.",
            )

        file_path = params.get(Input.FILE_PATH, "").strip()
        share_name = params.get(Input.SHARE_NAME, "").strip()
        file_content = params.get(Input.FILE_CONTENT)
        overwrite_existing = params.get(Input.OVERWRITE_EXISTING)

        try:
            file_content = base64.b64decode(file_content)
        except binascii.Error:
            raise PluginException(
                cause="Invalid file content provided.",
                assistance="Please ensure the file content is valid before running.",
            )

        try:
            # Calls method to establish a connection
            tree = self.connection._connect_to_smb_share(share_name)  # noqa: E1101

            open_file = Open(tree, file_path)
            open_file.create(
                create_disposition=(
                    CreateDisposition.FILE_OVERWRITE_IF if overwrite_existing else CreateDisposition.FILE_CREATE
                ),
                desired_access=0xF000F,  # access permissions
                file_attributes=FileAttributes.FILE_ATTRIBUTE_NORMAL,
                share_access=ShareAccess.FILE_SHARE_READ | ShareAccess.FILE_SHARE_WRITE,
                create_options=0,
                impersonation_level=ImpersonationLevel.Impersonation,
            )

        except SMBException as error:
            self.logger.error(f"SMBException encountered: {error}")
            if "STATUS_OBJECT_NAME_COLLISION" in str(error) and not overwrite_existing:
                raise PluginException(
                    cause="File already exists and overwrite_existing is set to False.",
                    assistance=f"File: {file_path} already exists, and overwrite_existing is False. Please set overwrite_existing to True if you want to overwrite the file.",
                )
            elif "STATUS_OBJECT_NAME_INVALID" in str(error) or "STATUS_OBJECT_NAME_COLLISION" in str(error):
                raise PluginException(
                    cause=f"The requested file: {file_path} may not be an acceptable file name, or the file content is invalid.",
                    assistance=f"Please ensure the file: {file_path} is not null, contains any illegal filename characters and that the file content is type base64 before trying again.",
                )
            elif "STATUS_BAD_NETWORK_NAME" in str(error):
                raise PluginException(
                    cause=f"The requested share: {share_name} is not a valid share name.",
                    assistance=f"Please ensure the share name: {share_name} is correct and try again.",
                )

            raise PluginException(
                cause="SMB file creation failed.", assistance="Check logs for further information", data=error
            )

        try:
            open_file.write(file_content, 0)
            open_file.flush()
            self.logger.info(f"File {file_path} created successfully")

            open_file.close()
            tree.disconnect()

            return {Output.CREATED: True}

        except PluginException as e:
            raise PluginException(
                cause="Failed to create a file",
                assistance=f"Ensure the share name: {share_name} and file path {file_path} are correct, and that the correct permissions have been granted.",
                data=str(e),
            )
        finally:
            if open_file:
                open_file.close()
