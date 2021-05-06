import insightconnect_plugin_runtime
from .schema import GetDeliveredThreatsInput, GetDeliveredThreatsOutput, Input, Output, Component

# Custom imports below
from komand_proofpoint_tap.util.api import Endpoint
from komand_proofpoint_tap.util.util import SiemUtils


class GetDeliveredThreats(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_delivered_threats",
            description=Component.DESCRIPTION,
            input=GetDeliveredThreatsInput(),
            output=GetDeliveredThreatsOutput(),
        )

    def run(self, params={}):
        self.connection.client.check_authorization()

        response = self.connection.client.siem_action(
            Endpoint.get_delivered_threats(),
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
        delivered_messages = response.get("messagesDelivered", [])
        if params.get(Input.SUBJECT) and delivered_messages:
            response["messagesDelivered"] = SiemUtils.search_subject(delivered_messages, params.get(Input.SUBJECT))

        return {Output.RESULTS: insightconnect_plugin_runtime.helper.clean(response)}
