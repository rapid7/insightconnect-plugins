import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import GetApplicationSegmentInput, GetApplicationSegmentOutput, Input, Output, Component

# Custom imports below


class GetApplicationSegment(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_application_segment",
            description=Component.DESCRIPTION,
            input=GetApplicationSegmentInput(),
            output=GetApplicationSegmentOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        segment_id = params.get(Input.SEGMENT_ID)
        # END INPUT BINDING - DO NOT REMOVE

        result = self.connection.zpa_client.get_application_segment(segment_id)
        return {
            Output.SEGMENT: result,
        }
