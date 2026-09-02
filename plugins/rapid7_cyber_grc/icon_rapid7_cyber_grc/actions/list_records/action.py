import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import ListRecordsInput, ListRecordsOutput, Input, Output, Component

# Custom imports below


class ListRecords(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_records", description=Component.DESCRIPTION, input=ListRecordsInput(), output=ListRecordsOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        expand = params.get(Input.EXPAND)
        filter = params.get(Input.FILTER)
        order_by = params.get(Input.ORDER_BY)
        record_type = params.get(Input.RECORD_TYPE)
        select = params.get(Input.SELECT)
        skip = params.get(Input.SKIP)
        top = params.get(Input.TOP)
        # END INPUT BINDING - DO NOT REMOVE
        records = self.connection.client.list_records(
            record_type, filter_=filter, select=select, expand=expand, order_by=order_by, top=top, skip=skip
        )

        return {Output.RECORDS: records, Output.COUNT: len(records)}
