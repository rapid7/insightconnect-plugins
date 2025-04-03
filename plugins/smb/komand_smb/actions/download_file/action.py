import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import DownloadFileInput, DownloadFileOutput, Input, Output, Component

from smbprotocol.open import Open, ImpersonationLevel, CreateDisposition, CreateOptions, ShareAccess
from smbprotocol.file_info import FileAttributes
from smbprotocol.exceptions import SMBException


class DownloadFile(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="download_file",
            description=Component.DESCRIPTION,
            input=DownloadFileInput(),
            output=DownloadFileOutput(),
        )

    def run(self, params={}):
        file_path = params.get(Input.FILE_PATH)
        share_name = params.get(Input.SHARE_NAME)

        try:
            # Calls method to establish a connection
            tree = self.connection._connect_to_smb_share(share_name)  # noqa: E1101

            open_file = Open(tree, file_path)
            open_file.create(
                impersonation_level=ImpersonationLevel.Impersonation,
                file_attributes=FileAttributes.FILE_ATTRIBUTE_NORMAL,
                desired_access=0x1,  # standard read access
                share_access=ShareAccess.FILE_SHARE_READ,
                create_disposition=CreateDisposition.FILE_OPEN,
                create_options=CreateOptions.FILE_NON_DIRECTORY_FILE,
            )

            file_content = open_file.read(0, open_file.end_of_file)

            open_file.close()
            tree.disconnect()

            if not file_content:
                raise PluginException(
                    cause="File is empty or no content returned.",
                    assistance="Ensure the file contains valid content.",
                )

            decoded_content = file_content.decode("utf-8", errors="replace")

            return {Output.FILE: {"content": decoded_content, "filename": file_path}}

        except SMBException as error:
            if "STATUS_BAD_NETWORK_NAME" in str(error):
                raise PluginException(
                    cause=f"The requested share: {share_name} is not a valid share name.",
                    assistance=f"Please ensure the share name: {share_name} is correct and try again.",
                )

            elif "STATUS_OBJECT_NAME_NOT_FOUND" in str(error):
                raise PluginException(
                    cause="File not found.",
                    assistance=f"The file '{file_path}' does not exist in the share '{share_name}'. Please check the path and try again.",
                )

            raise PluginException(
                cause="Failed to download file.",
                assistance="Ensure the file exists and that the correct permissions are set.",
                data=str(error),
            )
