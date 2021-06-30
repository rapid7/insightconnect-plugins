import insightconnect_plugin_runtime
from .schema import GetBlockedClicksInput, GetBlockedClicksOutput, Input, Output, Component

# Custom imports below
from komand_proofpoint_tap.util.api import Endpoint
from komand_proofpoint_tap.util.util import SiemUtils


class GetBlockedClicks(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_blocked_clicks",
            description=Component.DESCRIPTION,
            input=GetBlockedClicksInput(),
            output=GetBlockedClicksOutput(),
        )

    def run(self, params={}):
        self.connection.client.check_authorization()

        query_params = {"format": "JSON"}
        threat_status = params.get(Input.THREAT_STATUS)

        if threat_status != "all":
            query_params["threatStatus"] = threat_status

        response = self.connection.client.siem_action(
            Endpoint.get_blocked_clicks(),
            SiemUtils.prepare_time_range(params.get(Input.TIME_START), params.get(Input.TIME_END), query_params),
        )
        blocked_clicks = response.get("clicksBlocked", [])
        if params.get(Input.URL) and blocked_clicks:
            response["clicksBlocked"] = SiemUtils.search_url(blocked_clicks, params.get(Input.URL))

        return {Output.RESULTS: insightconnect_plugin_runtime.helper.clean(response)}
