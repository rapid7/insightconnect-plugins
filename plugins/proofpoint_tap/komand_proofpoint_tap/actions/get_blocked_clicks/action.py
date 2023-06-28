import insightconnect_plugin_runtime
from .schema import GetBlockedClicksInput, GetBlockedClicksOutput, Input, Output, Component

# Custom imports below
from komand_proofpoint_tap.util.api import Endpoint
from komand_proofpoint_tap.util.util import SiemUtils
from komand_proofpoint_tap.util.helpers import clean


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
        threat_status = params.get(Input.THREATSTATUS)

        if threat_status != "all":
            query_params["threatStatus"] = threat_status

        response = self.connection.client.siem_action(
            Endpoint.get_blocked_clicks(),
            SiemUtils.prepare_time_range(params.get(Input.TIMESTART), params.get(Input.TIMEEND), query_params),
        )
        blocked_clicks = response.get("clicksBlocked", [])
        url = params.get(Input.URL)
        if url and blocked_clicks:
            blocked_clicks = SiemUtils.search_url(blocked_clicks, url)

        response["clicksBlocked"] = clean(blocked_clicks)

        return {Output.RESULTS: response}
