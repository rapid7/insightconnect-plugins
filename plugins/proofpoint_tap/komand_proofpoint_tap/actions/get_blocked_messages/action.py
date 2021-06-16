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

        query_params = {"format": "JSON"}
        threat_type = params.get(Input.THREAT_TYPE)
        threat_status = params.get(Input.THREAT_STATUS)

        if threat_type != "all":
            query_params["threatType"] = threat_type
        if threat_status != "all":
            query_params["threatStatus"] = threat_status

        response = self.connection.client.siem_action(
            Endpoint.get_blocked_messages(),
            SiemUtils.prepare_time_range(params.get(Input.TIME_START), params.get(Input.TIME_END), query_params),
        )
        blocked_messages = response.get("messagesBlocked", [])
        if params.get(Input.SUBJECT) and blocked_messages:
            response["messagesBlocked"] = SiemUtils.search_subject(blocked_messages, params.get(Input.SUBJECT))

        return {Output.RESULTS: insightconnect_plugin_runtime.helper.clean(response)}
