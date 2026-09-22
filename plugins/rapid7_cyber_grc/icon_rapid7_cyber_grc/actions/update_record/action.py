import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import UpdateRecordInput, UpdateRecordOutput, Input, Output, Component

# Custom imports below


class UpdateRecord(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_record",
            description=Component.DESCRIPTION,
            input=UpdateRecordInput(),
            output=UpdateRecordOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        record_id = params.get(Input.ID)
        record = params.get(Input.RECORD)
        record_type = params.get(Input.RECORD_TYPE)
        # END INPUT BINDING - DO NOT REMOVE
        return {Output.RECORD: self.connection.client.update_record(record_type, record_id, record)}
