import komand
from .schema import DownloadFileInput, DownloadFileOutput, Input, Output, Component
from komand.exceptions import PluginException

# Custom imports below
import io
import smb


class DownloadFile(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='download_file',
            description=Component.DESCRIPTION,
            input=DownloadFileInput(),
            output=DownloadFileOutput())

    def run(self, params={}):
        file_path = params.get(Input.FILE_PATH)
        share_name = params.get(Input.SHARE_NAME)
        timeout = params.get(Input.TIMEOUT, 30)

        try:
            file_obj = io.BytesIO()
            self.connection.conn.retrieveFile(share_name, file_path, file_obj, timeout=timeout)
        except smb.smb_structs.OperationFailure as e:
            raise PluginException(cause='Failed to retrieve file content',
                                  assistance='This may occur when the file does not exist.',
                                  data=e)
        except smb.base.SMBTimeout as e:
            raise PluginException(cause='Timeout reached when connecting to SMB endpoint.',
                                  assistance='Validate network connectivity.',
                                  data=e)
        except smb.base.NotReadyError as e:
            raise PluginException(cause='The SMB connection is not authenticated or the authentication has failed.',
                                  assistance='Verify the credentials of the connection in use.',
                                  data=e)

        return {Output.FILE: {"content": file_obj.getvalue().decode("UTF-8"), "filename": file_path}}
