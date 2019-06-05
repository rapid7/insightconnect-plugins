import komand
from .schema import DeleteFileInput, DeleteFileOutput, Input, Output
# Custom imports below
import smb


class DeleteFile(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_file',
                description='Delete file from share',
                input=DeleteFileInput(),
                output=DeleteFileOutput())

    def run(self, params={}):
        if '*' in params.get(Input.FILE_PATH):
            self.logger.error("The Delete File action does not allow use of wildcards; "
                              "please leverage the Delete Files action")
            return {Output.DELETED: False}

        try:
            self.connection.conn.deleteFiles(params.get(Input.SHARE_NAME),
                                             params.get(Input.FILE_PATH),
                                             timeout=params.get(Input.TIMEOUT))
            return {Output.DELETED: True}
        except smb.smb_structs.OperationFailure as e:
            raise Exception("Failed to delete file. This may occur when the file does not exist.") from e
        except smb.base.SMBTimeout as e:
            raise Exception("Timeout reached when connecting to SMB endpoint. Validate network connectivity or "
                            "extend connection timeout") from e
        except smb.base.NotReadyError as e:
            raise Exception("The SMB connection is not authenticated or the authentication has failed.  Verify the "
                            "credentials of the connection in use.") from e
