import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import CreateAuditInput, CreateAuditOutput, Input, Output, Component

# Custom imports below


class CreateAudit(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_audit", description=Component.DESCRIPTION, input=CreateAuditInput(), output=CreateAuditOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        record = params.get(Input.RECORD)
        # END INPUT BINDING - DO NOT REMOVE
        return {Output.AUDIT: self.connection.client.create_record("Audits", record)}
