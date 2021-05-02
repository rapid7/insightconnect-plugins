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

        response = self.connection.client.siem_action(
            Endpoint.get_permitted_clicks(),
            SiemUtils.prepare_time_range(
                params.get(Input.TIME_START),
                params.get(Input.TIME_END),
                {
                    "format": "JSON",
                    "threatStatus": params.get(Input.THREAT_STATUS),
                },
            ),
        )
        if params.get(Input.URL):
            response["clicksBlocked"] = SiemUtils.search_url(response.get("clicksBlocked"), params.get(Input.URL))

        return {Output.RESULTS: insightconnect_plugin_runtime.helper.clean(response)}
