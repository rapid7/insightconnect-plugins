import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import GetRecordInput, GetRecordOutput, Input, Output, Component

# Custom imports below


class GetRecord(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_record", description=Component.DESCRIPTION, input=GetRecordInput(), output=GetRecordOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        expand = params.get(Input.EXPAND)
        id = params.get(Input.ID)
        record_type = params.get(Input.RECORD_TYPE)
        select = params.get(Input.SELECT)
        # END INPUT BINDING - DO NOT REMOVE
        return {Output.RECORD: self.connection.client.get_record(record_type, id, select=select, expand=expand)}
