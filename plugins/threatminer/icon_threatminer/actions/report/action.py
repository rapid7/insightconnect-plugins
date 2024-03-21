import insightconnect_plugin_runtime

from .schema import Component, Input, Output, ReportInput, ReportOutput

# Custom imports below


class Report(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="report",
            description=Component.DESCRIPTION,
            input=ReportInput(),
            output=ReportOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        filename = params.get(Input.FILENAME, "")
        year = params.get(Input.YEAR, "")
        query_type = params.get(Input.QUERY_TYPE, "")
        # END INPUT BINDING - DO NOT REMOVE

        return {Output.RESPONSE: self.connection.api_client.report(filename, year, query_type)}
