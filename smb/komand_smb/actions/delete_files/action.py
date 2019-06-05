import komand
from .schema import DeleteFilesInput, DeleteFilesOutput, Input, Output
# Custom imports below
import smb
smb.smb_structs.SUPPORT_SMB2 = False  # Disable SMB2 support in order to allow deletion with wildcard pattern


class DeleteFiles(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_files',
                description='Delete file(s) from share',
                input=DeleteFilesInput(),
                output=DeleteFilesOutput())

    def run(self, params={}):
        try:
            self.connection.conn.deleteFiles(params.get(Input.SHARE_NAME),
                                             params.get(Input.FILE_PATH),
                                             timeout=params.get(Input.TIMEOUT))
            return {Output.DELETED: True}
        except smb.smb_structs.OperationFailure as e:
            raise Exception("Failed to delete file(s). This may occur when the file does not exist or does not match "
                            "the wildcard pattern.") from e
        except smb.base.SMBTimeout as e:
            raise Exception("Timeout reached when connecting to SMB endpoint. Validate network connectivity or "
                            "extend connection timeout") from e
        except smb.base.NotReadyError as e:
            raise Exception("The SMB connection is not authenticated or the authentication has failed.  Verify the "
                            "credentials of the connection in use.") from e
