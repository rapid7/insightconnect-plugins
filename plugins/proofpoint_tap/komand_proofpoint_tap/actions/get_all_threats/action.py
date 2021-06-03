import insightconnect_plugin_runtime
from .schema import GetAllThreatsInput, GetAllThreatsOutput, Input, Output, Component

# Custom imports below
from komand_proofpoint_tap.util.api import Endpoint
from komand_proofpoint_tap.util.util import SiemUtils


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
        threat_type = params.get(Input.THREAT_TYPE)
        threat_status = params.get(Input.THREAT_STATUS)

        if threat_type != "all":
            query_params["threatType"] = threat_type
        if threat_status != "all":
            query_params["threatStatus"] = threat_status

        return {
            Output.RESULTS: insightconnect_plugin_runtime.helper.clean(
                self.connection.client.siem_action(
                    Endpoint.get_all_threats(),
                    SiemUtils.prepare_time_range(
                        params.get(Input.TIME_START), params.get(Input.TIME_END), query_params
                    ),
                )
            )
        }
