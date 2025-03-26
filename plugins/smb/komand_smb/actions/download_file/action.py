import insightconnect_plugin_runtime
from .schema import DownloadFileInput, DownloadFileOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import chardet
import io
import smb


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
        timeout = params.get(Input.TIMEOUT, 30)

        try:
            file_obj = io.BytesIO()
            self.connection.conn.retrieveFile(share_name, file_path, file_obj, timeout=timeout)
        except smb.smb_structs.OperationFailure as e:  # noqa: c-extension-no-member
            raise PluginException(
                cause="Failed to retrieve file content",
                assistance="This may occur when the file does not exist.",
                data=e,
            )
        except smb.base.SMBTimeout as e:  # noqa: c-extension-no-member
            raise PluginException(
                cause="Timeout reached when connecting to SMB endpoint.",
                assistance="Validate network connectivity.",
                data=e,
            )
        except smb.base.NotReadyError as e:  # noqa: c-extension-no-member
            raise PluginException(
                cause="The SMB connection is not authenticated or the authentication has failed.",
                assistance="Verify the credentials of the connection in use.",
                data=e,
            )
        encoding = chardet.detect(file_obj.getvalue()).get("encoding", "utf-8")  # noqa: c-extension-no-member
        return {Output.FILE: {"content": file_obj.getvalue().decode(encoding), "filename": file_path}}
