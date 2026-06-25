import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import SubmitThreatFeedInput, SubmitThreatFeedOutput, Input, Output, Component

# Custom imports below


class SubmitThreatFeed(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="submit_threat_feed",
            description=Component.DESCRIPTION,
            input=SubmitThreatFeedInput(),
            output=SubmitThreatFeedOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        description = params.get(Input.DESCRIPTION)
        feed_type = params.get(Input.FEED_TYPE)
        indicators = params.get(Input.INDICATORS)
        # END INPUT BINDING - DO NOT REMOVE

        result = self.connection.zia_client.submit_threat_feed(feed_type, indicators, description)
        return {
            Output.SUCCESS: result.get("success", False),
            Output.SUBMITTED_COUNT: result.get("submitted_count", 0),
        }
