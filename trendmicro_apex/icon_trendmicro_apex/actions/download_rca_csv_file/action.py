import komand
from .schema import DownloadRcaCsvFileInput, DownloadRcaCsvFileOutput, Input, Output, Component
# Custom imports below
from ...util import util


class DownloadRcaCsvFile(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='download_rca_csv_file',
            description=Component.DESCRIPTION,
            input=DownloadRcaCsvFileInput(),
            output=DownloadRcaCsvFileOutput())

    def run(self, params={}):
        return {
            Output.API_RESPONSE: self.connection.api.execute(
                "put",
                "/WebApp/OSCE_iES/OsceIes/ApiEntry",
                {
                    "Url": "V1/Task/ShowFootPrintCsv",
                    "TaskType": util.TaskType.value_of(params.get(Input.TASK_TYPE, util.DEFAULT_TASK_TYPE)),
                    "Payload": {
                        "agentGuid": params.get(Input.AGENT_GUID),
                        "scanSummaryGuid": params.get(Input.SCAN_SUMMARY_GUID),
                        "serverGuid": params.get(Input.SERVER_GUID),
                        "hostIP": params.get(Input.HOST_IP),
                        "hostName": params.get(Input.HOST_NAME)
                    }
                }
            )
        }
