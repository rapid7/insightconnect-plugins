import insightconnect_plugin_runtime

from .schema import CreateFileInput, CreateFileOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import io
import smb
import base64
import binascii


class CreateFile(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_file", description=Component.DESCRIPTION, input=CreateFileInput(), output=CreateFileOutput()
        )

    def run(self, params={}):  # noqa: MC0001
        file_path = params.get(Input.FILE_PATH)
        share_name = params.get(Input.SHARE_NAME)
        file_content = params.get(Input.FILE_CONTENT)
        overwrite_existing = params.get(Input.OVERWRITE_EXISTING)
        timeout = params.get(Input.TIMEOUT, 30)

        try:
            file_content = base64.b64decode(file_content)
        except binascii.Error as e:  # noqa: F841
            raise PluginException(
                cause="Invalid file content input provided.", assistance="Please double-check the file content input."
            )

        if not overwrite_existing:
            try:
                self.connection.conn.getAttributes(share_name, file_path, timeout=timeout)
                raise PluginException(
                    cause="Cannot overwrite existing file.",
                    assistance="Please set the 'Overwrite Existing' input to true and re-run.",
                )
            except smb.smb_structs.OperationFailure as e:  # noqa: F841
                self.logger.info(f"File {file_path} does not exist. Continuing with file creation...")
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

        try:
            file_obj = io.BytesIO(file_content)
            self.connection.conn.storeFile(share_name, file_path, file_obj, timeout=timeout)
            self.logger.info(f"File {file_path} created successfully")
            return {Output.CREATED: True}
        except smb.smb_structs.OperationFailure as e:  # noqa: c-extension-no-member
            raise PluginException(
                cause="Failed to create a file.", assistance="This may occur when the file does not exist.", data=e
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
        except Exception as e:
            raise PluginException(
                preset=PluginException.Preset.UNKNOWN,
                data=f"Error: {str(e)}.",
            )
