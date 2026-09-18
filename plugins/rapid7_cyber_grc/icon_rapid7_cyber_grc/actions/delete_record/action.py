import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import DeleteRecordInput, DeleteRecordOutput, Input, Output, Component

# Custom imports below


class DeleteRecord(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_record",
            description=Component.DESCRIPTION,
            input=DeleteRecordInput(),
            output=DeleteRecordOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        id = params.get(Input.ID)
        record_type = params.get(Input.RECORD_TYPE)
        # END INPUT BINDING - DO NOT REMOVE
        return {Output.RESULT: self.connection.client.delete_record(record_type, id)}
