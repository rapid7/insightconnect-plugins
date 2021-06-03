import insightconnect_plugin_runtime
from .schema import GetPermittedClicksInput, GetPermittedClicksOutput, Input, Output, Component

# Custom imports below
from komand_proofpoint_tap.util.api import Endpoint
from komand_proofpoint_tap.util.util import SiemUtils


class GetPermittedClicks(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_permitted_clicks",
            description=Component.DESCRIPTION,
            input=GetPermittedClicksInput(),
            output=GetPermittedClicksOutput(),
        )

    def run(self, params={}):
        self.connection.client.check_authorization()

        query_params = {"format": "JSON"}
        threat_status = params.get(Input.THREAT_STATUS)

        if threat_status != "all":
            query_params["threatStatus"] = threat_status

        response = self.connection.client.siem_action(
            Endpoint.get_permitted_clicks(),
            SiemUtils.prepare_time_range(params.get(Input.TIME_START), params.get(Input.TIME_END), query_params),
        )
        permitted_clicks = response.get("clicksPermitted", [])
        if params.get(Input.URL) and permitted_clicks:
            response["clicksPermitted"] = SiemUtils.search_url(permitted_clicks, params.get(Input.URL))

        return {Output.RESULTS: insightconnect_plugin_runtime.helper.clean(response)}
