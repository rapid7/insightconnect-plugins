import insightconnect_plugin_runtime
from .schema import GetFileQuarantineStatusInput, GetFileQuarantineStatusOutput, Input, Output, Component

# Custom imports below
import json


class GetFileQuarantineStatus(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_file_quarantine_status",
            description=Component.DESCRIPTION,
            input=GetFileQuarantineStatusInput(),
            output=GetFileQuarantineStatusOutput(),
        )

    def run(self, params={}):
        endpoint_id = params.get(Input.ENDPOINT_ID)
        file_hash = params.get(Input.FILE_HASH)
        file_path = params.get(Input.FILE_PATH)
        file = {"endpoint_id": endpoint_id, "file_hash": file_hash, "file_path": file_path}
        self.logger.info("Getting file quarantine status for " + json.dumps(file))
        file_quarantine_status = self.connection.xdr_api.get_file_quarantine_status(file)
        output = insightconnect_plugin_runtime.helper.clean(file_quarantine_status)
        self.logger.info("Get file quarantine status complete.")
        return {Output.FILE_IS_QUARANTINED: output["status"]}
