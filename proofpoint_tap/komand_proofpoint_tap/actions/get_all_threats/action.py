import insightconnect_plugin_runtime
from .schema import GetAllThreatsInput, GetAllThreatsOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
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
        try:
            return {
                Output.RESULTS: insightconnect_plugin_runtime.helper.clean(
                    self.connection.client.siem_action(
                        Endpoint.get_all_threats(),
                        SiemUtils.prepare_time_range(
                            params.get(Input.TIME_START),
                            params.get(Input.TIME_END),
                            {
                                "format": "JSON",
                                "threatType": params.get(Input.THREAT_TYPE),
                                "threatStatus": params.get(Input.THREAT_STATUS),
                            },
                        ),
                    )
                )
            }
        except AttributeError as e:
            raise PluginException(
                cause="Proofpoint Tap returned unexpected response.",
                assistance="Please check that the connection required for this action is set up and try again.",
                data=e,
            )
