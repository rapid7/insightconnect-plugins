import insightconnect_plugin_runtime
from .schema import GetAllThreatsInput, GetAllThreatsOutput, Input, Output, Component

# Custom imports below
from komand_proofpoint_tap.util.api import Endpoint
from komand_proofpoint_tap.util.util import SiemUtils
from komand_proofpoint_tap.util.helpers import clean


class GetAllThreats(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_all_threats",
            description=Component.DESCRIPTION,
            input=GetAllThreatsInput(),
            output=GetAllThreatsOutput(),
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
            Endpoint.get_all_threats(),
            SiemUtils.prepare_time_range(params.get(Input.TIMESTART), params.get(Input.TIMEEND), query_params),
        )

        response["messagesBlocked"] = clean(response.get("messagesBlocked", []))
        response["messagesDelivered"] = clean(response.get("messagesDelivered", []))
        response["clicksBlocked"] = clean(response.get("clicksBlocked", []))
        response["clicksPermitted"] = clean(response.get("clicksPermitted", []))

        return {Output.RESULTS: response}
