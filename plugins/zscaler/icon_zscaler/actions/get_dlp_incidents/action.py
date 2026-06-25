import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import GetDlpIncidentsInput, GetDlpIncidentsOutput, Input, Output, Component

# Custom imports below
from icon_zscaler.util.helpers import clean_dict


class GetDlpIncidents(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_dlp_incidents",
            description=Component.DESCRIPTION,
            input=GetDlpIncidentsInput(),
            output=GetDlpIncidentsOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        end_time = params.get(Input.END_TIME)
        next_link = params.get(Input.NEXT_LINK)
        start_time = params.get(Input.START_TIME)
        # END INPUT BINDING - DO NOT REMOVE

        result = self.connection.zia_client.get_dlp_incidents(start_time, end_time, next_link or None)
        return clean_dict(
            {
                Output.INCIDENTS: result.get("incidents", []),
                Output.NEXT_LINK: result.get("next_link", ""),
            }
        )
