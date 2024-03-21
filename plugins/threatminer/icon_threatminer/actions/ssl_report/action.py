import insightconnect_plugin_runtime

from .schema import Component, Input, Output, SslReportInput, SslReportOutput

# Custom imports below


class SslReport(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="ssl_report",
            description=Component.DESCRIPTION,
            input=SslReportInput(),
            output=SslReportOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        query = params.get(Input.QUERY, "")
        # END INPUT BINDING - DO NOT REMOVE

        return {Output.RESPONSE: self.connection.api_client.ssl_hosts(query, report=True)}
