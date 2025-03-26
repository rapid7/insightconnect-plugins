import insightconnect_plugin_runtime
from .schema import GetAttributesInput, GetAttributesOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import smb
import pytz
from komand_smb.util import utils


class GetAttributes(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_attributes",
            description=Component.DESCRIPTION,
            input=GetAttributesInput(),
            output=GetAttributesOutput(),
        )

    def run(self, params={}):
        file_path = params.get(Input.FILE_PATH)
        share_name = params.get(Input.SHARE_NAME)
        timeout = params.get(Input.TIMEOUT, 30)

        tz_input = params.get(Input.TIMEZONE, "UTC")
        try:
            tz = pytz.timezone(tz_input)
        except pytz.exceptions.UnknownTimeZoneError as e:
            raise PluginException(
                cause=f"{tz_input} is not a valid timezone.",
                assistance="Reference: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones for valid timezone names.",
            ) from e

        try:
            attr = self.connection.conn.getAttributes(share_name, file_path, timeout=timeout)
            file_attributes = {
                "name": attr.filename,
                "short_name": attr.short_name,
                "is_directory": attr.isDirectory,
                "create_time": utils.datetime_with_timezone(attr.create_time, tz).isoformat(),
                "last_access_time": utils.datetime_with_timezone(attr.last_access_time, tz).isoformat(),
                "last_write_time": utils.datetime_with_timezone(attr.last_write_time, tz).isoformat(),
                "file_size": attr.file_size,
            }
            return {Output.ATTRIBUTES: file_attributes}
        except smb.smb_structs.OperationFailure as e:  # noqa: c-extension-no-member
            raise PluginException(
                cause="Failed to get file attributes.", assistance="This may occur when the file does not exist."
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
