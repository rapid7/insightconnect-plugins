import komand
from .schema import ListSharesInput, ListSharesOutput, Input, Output

# Custom imports below
import smb


class ListShares(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_shares",
            description="List shares on remote server",
            input=ListSharesInput(),
            output=ListSharesOutput(),
        )

    def run(self, params={}):
        shares = []
        try:
            shares_list = self.connection.conn.listShares(timeout=params.get(Input.TIMEOUT))
            for s in shares_list:
                shares.append({"name": s.name, "comments": s.comments})
        except smb.smb_structs.OperationFailure as e:
            raise e
        except smb.base.SMBTimeout as e:
            raise Exception(
                "Timeout reached when connecting to SMB endpoint. Validate network connectivity or "
                "extend connection timeout"
            ) from e
        except smb.base.NotReadyError as e:
            raise Exception(
                "The SMB connection is not authenticated or the authentication has failed.  Verify the "
                "credentials of the connection in use."
            ) from e

        self.logger.info(f"Returned {len(shares)} shares from endpoint")
        return {Output.SHARES: shares}
