import insightconnect_plugin_runtime
from .schema import GetBlockedMessagesInput, GetBlockedMessagesOutput, Input, Output, Component

# Custom imports below
from komand_proofpoint_tap.util.api import Endpoint
from komand_proofpoint_tap.util.util import SiemUtils
from komand_proofpoint_tap.util.helpers import clean


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
        threat_type = params.get(Input.THREATTYPE)
        threat_status = params.get(Input.THREATSTATUS)

        if threat_type != "all":
            query_params["threatType"] = threat_type
        if threat_status != "all":
            query_params["threatStatus"] = threat_status

        response = self.connection.client.siem_action(
            Endpoint.get_blocked_messages(),
            SiemUtils.prepare_time_range(params.get(Input.TIMESTART), params.get(Input.TIMEEND), query_params),
        )
        blocked_messages = response.get("messagesBlocked", [])
        subject = params.get(Input.SUBJECT)
        if subject and blocked_messages:
            blocked_messages = SiemUtils.search_subject(blocked_messages, subject)

        response["messagesBlocked"] = clean(blocked_messages)

        return {Output.RESULTS: response}
