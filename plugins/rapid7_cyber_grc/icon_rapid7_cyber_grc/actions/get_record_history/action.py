import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import GetRecordHistoryInput, GetRecordHistoryOutput, Input, Output, Component

# Custom imports below


class GetRecordHistory(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_record_history",
            description=Component.DESCRIPTION,
            input=GetRecordHistoryInput(),
            output=GetRecordHistoryOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        record_id = params.get(Input.ID)
        record_type = params.get(Input.RECORD_TYPE)
        # END INPUT BINDING - DO NOT REMOVE
        history = self.connection.client.get_record_history(record_type, record_id)

        return {Output.HISTORY: history, Output.COUNT: len(history)}
