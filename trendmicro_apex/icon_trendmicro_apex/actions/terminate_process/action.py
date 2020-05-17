import komand
from .schema import TerminateProcessInput, TerminateProcessOutput, Input, Component
# Custom imports below


class TerminateProcess(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='terminate_process',
            description=Component.DESCRIPTION,
            input=TerminateProcessInput(),
            output=TerminateProcessOutput())

    def run(self, params={}):
        payload = {
            "Url": "V1/Task/CreateProcessTermination",
            "TaskType": 4,
            "Payload": {
                "serverGuid": params.get(Input.SERVER_GUID, []),
                "agentGuid": params.get(Input.AGENT_GUID, {}),
                "suspiciousObjectName": params.get(Input.SUSPICIOUS_OBJECT_NAME),
                "terminationInfoList": params.get(Input.TERMINATION_INFO_LIST),
                "filter": params.get(Input.FILTER)
            }
        }
        return self.connection.api.execute(
            "post",
            "/WebApp/OSCE_iES/OsceIes/ApiEntry",
            payload
        )
