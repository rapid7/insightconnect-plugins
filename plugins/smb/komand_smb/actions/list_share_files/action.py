import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import ListShareFilesInput, ListShareFilesOutput, Input, Output

# Custom imports below
from datetime import datetime, timezone
import pytz
import smb
from komand_smb.util import utils


class ListShareFiles(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_share_files",
            description="List shares on remote server",
            input=ListShareFilesInput(),
            output=ListShareFilesOutput(),
        )

    def run(self, params={}):
        # Validate valid timezone name is input prior to continuing
        tz_input = params.get(Input.TIMEZONE)
        try:
            tz = pytz.timezone(tz_input)
        except pytz.exceptions.UnknownTimeZoneError as e:
            raise PluginException(
                f"{tz_input} is not a valid timezone; "
                f"reference https://en.wikipedia.org/wiki/List_of_tz_database_time_zones for valid "
                f"timezone names"
            ) from e

        files = []
        try:
            files_list = self.connection.conn.listPath(
                params.get(Input.SHARE_NAME),
                params.get(Input.PATH),
                pattern=params.get(Input.PATTERN),
                timeout=params.get(Input.TIMEOUT),
            )

            for f in files_list:
                files.append(
                    {
                        "name": f.filename,
                        "short_name": f.short_name,
                        "is_directory": f.isDirectory,
                        "create_time": utils.datetime_with_timezone(f.create_time, tz).isoformat(),
                        "last_access_time": utils.datetime_with_timezone(f.last_access_time, tz).isoformat(),
                        "last_write_time": utils.datetime_with_timezone(f.last_write_time, tz).isoformat(),
                        "file_size": f.file_size,
                    }
                )
        except smb.smb_structs.OperationFailure as e:  # noqa: c-extension-no-member
            self.logger.error(e)
            raise PluginException(
                "Failed to list files from share. This may occur when the share name or path are not valid."
            ) from e
        except smb.base.SMBTimeout as e:  # noqa: c-extension-no-member
            raise PluginException(
                "Timeout reached when connecting to SMB endpoint. Validate network connectivity or "
                "extend connection timeout"
            ) from e
        except smb.base.NotReadyError as e:  # noqa: c-extension-no-member
            raise PluginException(
                "The SMB connection is not authenticated or the authentication has failed.  Verify the "
                "credentials of the connection in use."
            ) from e

        self.logger.info(f"Returned {len(files)} files from share")
        return {Output.FILES: files}
