import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import CountRecordsInput, CountRecordsOutput, Input, Output, Component

# Custom imports below


class CountRecords(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="count_records",
            description=Component.DESCRIPTION,
            input=CountRecordsInput(),
            output=CountRecordsOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        filter_ = params.get(Input.FILTER)
        record_type = params.get(Input.RECORD_TYPE)
        # END INPUT BINDING - DO NOT REMOVE
        return {Output.COUNT: self.connection.client.count_records(record_type, filter_=filter_)}
