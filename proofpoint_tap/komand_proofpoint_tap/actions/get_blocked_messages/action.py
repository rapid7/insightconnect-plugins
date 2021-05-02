import insightconnect_plugin_runtime
from .schema import GetBlockedMessagesInput, GetBlockedMessagesOutput, Input, Output, Component

# Custom imports below
from komand_proofpoint_tap.util.api import Endpoint
from komand_proofpoint_tap.util.util import SiemUtils


class GetBlockedMessages(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_blocked_messages",
            description=Component.DESCRIPTION,
            input=GetBlockedMessagesInput(),
            output=GetBlockedMessagesOutput(),
        )

    def run(self, params={}):
        self.connection.client.check_authorization()

        response = self.connection.client.siem_action(
            Endpoint.get_blocked_messages(),
            SiemUtils.prepare_time_range(
                params.get(Input.TIME_START),
                params.get(Input.TIME_END),
                {
                    "format": "JSON",
                    "threatStatus": params.get(Input.THREAT_STATUS),
                    "threatType": params.get(Input.THREAT_TYPE),
                },
            ),
        )
        if params.get(Input.SUBJECT):
            response["messagesBlocked"] = SiemUtils.search_subject(
                response.get("messagesBlocked"), params.get(Input.SUBJECT)
            )
        return {Output.RESULTS: insightconnect_plugin_runtime.helper.clean(response)}
