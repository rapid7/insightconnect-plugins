import insightconnect_plugin_runtime
from .schema import EmailReportInput, EmailReportOutput, Input, Output, Component

# Custom imports below


class EmailReport(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="email_report", description=Component.DESCRIPTION, input=EmailReportInput(), output=EmailReportOutput()
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        email = params.get(Input.EMAIL, "")
        # END INPUT BINDING - DO NOT REMOVE

        return {Output.RESPONSE: self.connection.api_client.email(email, report=True)}
