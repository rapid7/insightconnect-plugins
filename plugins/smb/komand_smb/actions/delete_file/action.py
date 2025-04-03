import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import DeleteFileInput, DeleteFileOutput, Input, Output

from smbprotocol.open import Open, ImpersonationLevel, CreateDisposition, CreateOptions, FilePipePrinterAccessMask
from smbprotocol.file_info import FileAttributes
from smbprotocol.exceptions import SMBException


class DeleteFile(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_file",
            description="Delete a file from an SMB share",
            input=DeleteFileInput(),
            output=DeleteFileOutput(),
        )

    def run(self, params={}):
        file_path = params.get(Input.FILE_PATH)
        share_name = params.get(Input.SHARE_NAME)

        # Prevent wildcard value deletions
        if "*" in file_path:
            self.logger.error("Wildcard deletions are not allowed.")
            return {Output.DELETED: False}

        try:
            self.logger.info(f"Attempting to delete file: {file_path} from share: {share_name}")

            # Calls method to establish a connection
            tree = self.connection._connect_to_smb_share(share_name)  # noqa: E1101

            open_file = Open(tree, file_path)
            open_file.create(
                impersonation_level=ImpersonationLevel.Impersonation,
                file_attributes=FileAttributes.FILE_ATTRIBUTE_NORMAL,
                desired_access=FilePipePrinterAccessMask.GENERIC_READ | FilePipePrinterAccessMask.DELETE,
                share_access=0,
                create_disposition=CreateDisposition.FILE_OPEN,
                create_options=CreateOptions.FILE_NON_DIRECTORY_FILE | CreateOptions.FILE_DELETE_ON_CLOSE,
            )
            open_file.close()

            self.logger.info(f"File '{file_path}' deleted successfully.")
            tree.disconnect()

            return {Output.DELETED: True}

        except SMBException as error:
            if "STATUS_BAD_NETWORK_NAME" in str(error):
                raise PluginException(
                    cause=f"The requested share: {share_name} is not a valid share name.",
                    assistance=f"Please ensure the share name: {share_name} is correct and try again.",
                )
            elif "STATUS_OBJECT_NAME_NOT_FOUND" in str(error):
                raise PluginException(
                    cause=f"File '{file_path}' not found",
                    assistance=f"Please ensure {file_path} file exists before attempting to delete it.",
                )

            raise PluginException(
                cause="Failed to delete file.",
                assistance=f"The file '{file_path}' may not exist or is locked. Ensure it exists and is not in use.",
                data=str(error),
            ) from error
