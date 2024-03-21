import insightconnect_plugin_runtime

# Custom imports below
from .schema import AvReportInput, AvReportOutput, Component, Input, Output


class AvReport(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="av_report",
            description=Component.DESCRIPTION,
            input=AvReportInput(),
            output=AvReportOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        query = params.get(Input.QUERY, "")
        # END INPUT BINDING - DO NOT REMOVE

        return {Output.RESPONSE: self.connection.api_client.av_detection(query, report=True)}
